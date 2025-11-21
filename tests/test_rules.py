"""Data-driven tests for Vale rules using Pydantic models."""
from __future__ import annotations

from typing import Any, Dict


def test_rule_cases(materialized_files, vale_runner, assert_case):
    """Run vale on each materialized file for every test case and assert expectations."""
    rule_id, case, paths = materialized_files
    for path in paths:
        results = vale_runner(path, rule_id)
        assert_case(rule_id, case, results)


def test_manifest_has_positive_example(manifest):
    """Ensure each rule has at least one test case that triggers something."""
    missing = [
        rule.name
        for rule in manifest.rules
        if not any(c.expect.triggers for c in rule.cases)
    ]
    assert not missing, (
        "Each rule should have at least one positive (triggering) case. Missing: "
        + ", ".join(missing)
    )


def test_manifest_json_schema(manifest_schema: Dict[str, Any]):
    """Basic sanity checks on generated JSON Schema for the Manifest model."""
    # Top-level required should include 'rules'
    assert 'rules' in manifest_schema.get('properties', {}), "Schema missing 'rules' property"
    # Definition for rule cases should mention triggers
    # Pydantic v2 structure: look through schema for 'triggers'
    def _find_key(d: Dict[str, Any], key: str) -> bool:
        if key in d:
            return True
        for v in d.values():
            if isinstance(v, dict) and _find_key(v, key):
                return True
        return False

    assert _find_key(manifest_schema, 'triggers'), "Schema does not describe 'triggers'"
