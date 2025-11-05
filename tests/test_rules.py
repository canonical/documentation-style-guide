"""Data-driven tests for Vale rules.

This initial suite covers a subset of rules; expand `manifest.yml` to scale.
"""
from __future__ import annotations

def test_rule_cases(materialized_files, vale_runner, assert_case):
    rule_id, case, paths = materialized_files
    for path in paths:
        results = vale_runner(path, rule_id)
        assert_case(rule_id, case, results)


def test_manifest_has_positive_example(manifest):
    missing = [
        rule
        for rule, meta in manifest["rules"].items()
        if not any(c["expect"].get("triggers") for c in meta.get("cases", []))
    ]
    assert not missing, (
        "Each rule should have at least one positive (triggering) case. Missing: "
        + ", ".join(missing)
    )
