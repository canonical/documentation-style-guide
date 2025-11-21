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
from pydantic import BaseModel, Field, ValidationError
from typing import Any, Dict, Iterable, List, Tuple

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_PRIMARY_VALE_CFG = os.path.join(REPO_ROOT, ".vale.ini")
_FALLBACK_VALE_CFG = os.path.join(REPO_ROOT, "vale.ini")
VALE_CONFIG = _PRIMARY_VALE_CFG if os.path.exists(_PRIMARY_VALE_CFG) else _FALLBACK_VALE_CFG
STYLES_DIR = os.path.join(REPO_ROOT, "styles", "Canonical")
MANIFEST_PATH = os.path.join(os.path.dirname(__file__), "data", "manifest.yml")


class ExpectedResult(BaseModel):
    """Expected result portion of a test case.

    triggers: list of exact substrings Vale should flag. Empty list means no findings.
    severity: optional; if provided we assert all findings share this severity.
    message_regex: optional regex that all messages must match.
    """
    triggers: List[str] = Field(default_factory=list)
    severity: str | None = None
    message_regex: str | None = None


class TestCase(BaseModel):
    """A single test case for a rule."""
    id: str
    filetypes: List[str]
    content: str
    expect: ExpectedResult


class RuleDefinition(BaseModel):
    """All test cases for a single Vale rule."""
    name: str
    cases: List[TestCase]


class Manifest(BaseModel):
    """Root manifest model loaded from YAML."""
    rules: List[RuleDefinition]

    @classmethod
    def from_yaml_dict(cls, data: dict) -> "Manifest":
        """Create Manifest from YAML structure where rules is a mapping.

        YAML shape:
        rules:
          <rule_id>:
            cases: [ {id: ..., filetypes: [...], content: ..., expect: {...}}, ... ]
        """
        rules_dict = data.get("rules", {})
        rules = [
            {"name": rule_name, "cases": rule_data.get("cases", [])}
            for rule_name, rule_data in rules_dict.items()
        ]
        return cls(rules=rules)

    def iter_cases(self) -> Iterable[Tuple[str, TestCase]]:
        for rule in self.rules:
            for case in rule.cases:
                yield rule.name, case

    def get_rule_names(self) -> List[str]:
        return [rule.name for rule in self.rules]


def _load_manifest() -> Manifest:
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    try:
        return Manifest.from_yaml_dict(data)
    except ValidationError as e:
        raise ValueError(f"Manifest validation failed: {e}") from e


def _discover_rule_ids() -> List[str]:
    if not os.path.isdir(STYLES_DIR):
        return []
    return sorted(
        f.rsplit(".", 1)[0]
        for f in os.listdir(STYLES_DIR)
        if f.endswith(".yml")
    )


@pytest.fixture(scope="session")
def manifest() -> Manifest:
    """Provide the validated Manifest model."""
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
    missing = set(rule_ids) - set(manifest.get_rule_names())
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


def _iter_cases(manifest: Manifest) -> Iterable[Tuple[str, TestCase]]:
    return manifest.iter_cases()

def _idfn(param):
    rule, case = param
    return f"{rule}::{case.id}"


_ALL_CASES = list(_iter_cases(_load_manifest()))
@pytest.fixture(params=_ALL_CASES, ids=_idfn)
def case_definition(request):
    """Parametrized (rule_id, TestCase) tuple for each case in the manifest."""
    return request.param


@pytest.fixture(params=["md", "rst"], scope="session")
def all_supported_types(request):  # potential future use
    return request.param


@pytest.fixture
def materialized_files(case_definition, tmp_path):
    """Create one file per requested filetype for the test case; return list of paths."""
    rule_id, case = case_definition
    paths: List[str] = []
    for ext in case.filetypes:
        fname = f"{case.id}.{ext}"
        fpath = tmp_path / fname
        fpath.write_text(case.content, encoding="utf-8")
        paths.append(str(fpath))
    return rule_id, case, paths


def _assert_case(rule_id: str, case: TestCase, results: List[ValeResult]):
    expected = case.expect
    # Collect actual trigger list preserving duplicates for counting.
    actual_list = [r.match for r in results]
    expected_list = expected.triggers

    expected_set = set(expected_list)
    actual_set = set(actual_list)

    missing = sorted(expected_set - actual_set)
    unexpected = sorted(actual_set - expected_set)

    # Verify required tokens appear.
    assert not missing, (
        f"Missing expected triggers for {rule_id}/{case.id}: {missing}\n"
        f"Actual: {sorted(actual_set)}"
    )
    # Disallow completely unexpected tokens.
    assert not unexpected, (
        f"Unexpected triggers for {rule_id}/{case.id}: {unexpected}\n"
        f"Expected: {sorted(expected_set)}"
    )

    # For tokens with multiplicity in EXPECTED, ensure counts are met.
    from collections import Counter
    exp_counts = Counter(expected_list)
    act_counts = Counter(actual_list)
    multiplicity_failures = [
        f"{tok} (expected >= {exp_counts[tok]}, got {act_counts.get(tok,0)})"
        for tok in exp_counts
        if exp_counts[tok] > 1 and act_counts.get(tok, 0) < exp_counts[tok]
    ]
    assert not multiplicity_failures, (
        f"Insufficient duplicate occurrences for {rule_id}/{case.id}: "
        + ", ".join(multiplicity_failures)
    )
    if expected.severity:
        for r in results:
            assert r.severity.lower() == expected.severity.lower(), (
                f"Severity mismatch for trigger '{r.match}' in {rule_id}/{case.id}"
            )
    if expected.message_regex:
        pat = re.compile(expected.message_regex)
        for r in results:
            assert pat.search(r.message), (
                f"Message did not match /{expected.message_regex}/: {r.message}"
            )


@pytest.fixture
def vale_runner():
    return _run_vale

@pytest.fixture
def assert_case():
    return _assert_case

@pytest.fixture(scope="session")
def manifest_schema(manifest: Manifest) -> Dict[str, Any]:
    """Provide the JSON schema for the Manifest (Draft generation by Pydantic)."""
    return manifest.model_json_schema()
