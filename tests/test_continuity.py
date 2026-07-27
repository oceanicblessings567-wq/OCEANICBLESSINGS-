from omega import continuity_summary


def test_continuity_summary_includes_expected_documents():
    summary = continuity_summary()

    assert "artifact_count" in summary
    assert summary["artifact_count"] >= 4
    assert "missing_artifacts" in summary
    assert summary["keyword_checks"]["charter"]["living agnostic"] is True
    assert summary["keyword_checks"]["continuity_pack"]["preserve the living charter"] is True
