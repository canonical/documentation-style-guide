"""Pytest configuration and fixtures for Vale rule testing.

Initial version: focuses on a subset of rules with a data-driven manifest.
Extensible: add new rules/cases via `tests/data/manifest.yml`.
Set environment variable VALE_ENFORCE_COVERAGE=1 to enforce full rule coverage.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import shutil
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Tuple

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_PRIMARY_VALE_CFG = os.path.join(REPO_ROOT, ".vale.ini")
_FALLBACK_VALE_CFG = os.path.join(REPO_ROOT, "vale.ini")
VALE_CONFIG = _PRIMARY_VALE_CFG if os.path.exists(_PRIMARY_VALE_CFG) else _FALLBACK_VALE_CFG
STYLES_DIR = os.path.join(REPO_ROOT, "styles", "Canonical")
MANIFEST_PATH = os.path.join(os.path.dirname(__file__), "data", "manifest.yml")


def _load_manifest() -> Dict[str, Any]:
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    data.setdefault("rules", {})
    return data


def _discover_rule_ids() -> List[str]:
    if not os.path.isdir(STYLES_DIR):
        return []
    return sorted(
        f.rsplit(".", 1)[0]
        for f in os.listdir(STYLES_DIR)
        if f.endswith(".yml")
    )


@pytest.fixture(scope="session")
def manifest() -> Dict[str, Any]:
    return _load_manifest()


@pytest.fixture(scope="session")
def rule_ids() -> List[str]:
    return _discover_rule_ids()


def pytest_sessionstart(session):
    """pytest hook: optionally enforce coverage once at session start.

    If VALE_ENFORCE_COVERAGE=1, fail the session when any style rule lacks
    a manifest entry. Otherwise, emit a single informational message.
    """
    manifest = _load_manifest()
    rule_ids = _discover_rule_ids()
    missing = set(rule_ids) - set(manifest["rules"].keys())
    if os.environ.get("VALE_ENFORCE_COVERAGE") == "1":
        assert not missing, (
            "Rules without test coverage (enable by adding to manifest.yml): "
            + ", ".join(sorted(missing))
        )
    else:
        if missing:
            print(
                f"[vale-tests] Coverage relaxed. Missing manifest entries for: {sorted(missing)}"
            )


@dataclass
class ValeResult:
    match: str
    message: str
    severity: str
    line: int | None
    span: Tuple[int, int] | None


def _run_vale(target_file: str, rule_id: str) -> List[ValeResult]:
    """Run vale on a single file filtered to the given rule.

    Accepts exit codes 0 (no issues) and 1 (issues found). Raises on others.
    """
    filt = f'.Name=="Canonical.{rule_id}"'
    vale_bin = shutil.which("vale")
    if not vale_bin:
        pytest.skip("'vale' binary not found on PATH; skipping rule tests.")
    cmd = [
        vale_bin,
        "--config",
        VALE_CONFIG,
        "--filter",
        filt,
        "--output",
        "JSON",
        target_file,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    # Vale returns 0 (no issues) or 1 (issues found). Other codes indicate errors.
    if proc.returncode not in (0, 1):
        # Gracefully skip known RST parser runtime errors if detected.
        try:
            err_data = json.loads(proc.stderr)
        except json.JSONDecodeError:
            err_data = {}
        if err_data.get("Code") == "E100" and "callRst" in err_data.get("Text", ""):
            pytest.skip("Vale RST processing unavailable (E100 callRst); skipping RST case.")
        raise RuntimeError(
            f"Vale invocation failed (rc={proc.returncode}).\nSTDERR:\n{proc.stderr}\nSTDOUT:\n{proc.stdout}"
        )
    try:
        data = json.loads(proc.stdout or "{}")
    except json.JSONDecodeError as e:
        raise RuntimeError(
            f"Invalid JSON from vale for {target_file}: {e}\nRaw: {proc.stdout[:200]}"
        ) from e
    raw_hits = data.get(target_file, [])
    results: List[ValeResult] = []
    for h in raw_hits:
        span = None
        if 'Span' in h and isinstance(h.get('Span'), list):
            span_list = h.get("Span")
            if isinstance(span_list, list) and len(span_list) == 2:
                span = (span_list[0], span_list[1])
        results.append(
            ValeResult(
                match=h.get("Match", ""),
                message=h.get("Message", ""),
                severity=h.get("Severity", ""),
                line=h.get("Line"),
                span=span,
            )
        )
    return results


def _iter_cases(manifest: Dict[str, Any]) -> Iterable[Tuple[str, Dict[str, Any]]]:
    for rule, payload in manifest["rules"].items():
        for case in payload.get("cases", []):
            yield rule, case


def _idfn(param):
    rule, case = param
    return f"{rule}::{case['id']}"


_ALL_CASES = list(_iter_cases(_load_manifest()))
@pytest.fixture(params=_ALL_CASES, ids=_idfn)
def case_definition(request):
    return request.param  # (rule_id, case_dict)


@pytest.fixture(params=["md", "rst"], scope="session")
def all_supported_types(request):  # potential future use
    return request.param


@pytest.fixture
def materialized_files(case_definition, tmp_path):
    """Create one file per requested filetype for the test case; return list of paths."""
    rule_id, case = case_definition
    paths = []
    for ext in case.get("filetypes", []):
        fname = f"{case['id']}.{ext}"
        fpath = tmp_path / fname
        fpath.write_text(case["content"], encoding="utf-8")
        paths.append(str(fpath))
    return rule_id, case, paths


def _assert_case(rule_id: str, case: Dict[str, Any], results: List[ValeResult]):
    expected = case["expect"]
    expected_triggers = sorted(expected.get("triggers", []))
    actual_triggers = sorted(r.match for r in results)
    assert actual_triggers == expected_triggers, (
        f"Trigger mismatch for {rule_id}/{case['id']}\n"
        f"Expected: {expected_triggers}\nGot:      {actual_triggers}"
    )
    severity = expected.get("severity")
    if severity:
        for r in results:
            assert r.severity.lower() == severity.lower(), (
                f"Severity mismatch for trigger '{r.match}' in {rule_id}/{case['id']}"
            )
    msg_regex = expected.get("message_regex")
    if msg_regex:
        pat = re.compile(msg_regex)
        for r in results:
            assert pat.search(r.message), (
                f"Message did not match /{msg_regex}/: {r.message}"
            )


@pytest.fixture
def vale_runner():
    return _run_vale

@pytest.fixture
def assert_case():
    return _assert_case
