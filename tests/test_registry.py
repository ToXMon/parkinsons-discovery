"""The seed registry must stay consistent and must not claim a cure."""

import os
import subprocess
import sys
from pathlib import Path

from parkinsons_discovery.models import CLINICAL_STATUSES, Status
from parkinsons_discovery.registry import hypotheses, validate

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


def test_registry_is_internally_consistent():
    assert validate() == []
    ids = [item.id for item in hypotheses()]
    assert len(ids) == len(set(ids))
    assert len(ids) >= 10


def test_no_row_is_marked_active_or_curative():
    for item in hypotheses():
        if item.status in CLINICAL_STATUSES:
            assert item.leads
        assert item.status != Status.ACTIVE
        assert "cure" not in item.statement.lower()
        assert item.what_would_falsify
        assert item.do_not_assume


def test_cli_check_and_unknown_id():
    env = os.environ.copy()
    env["PYTHONPATH"] = str(SRC)
    ok = subprocess.run(
        [sys.executable, "-m", "parkinsons_discovery", "check"],
        cwd=ROOT, env=env, capture_output=True, text=True,
    )
    assert ok.returncode == 0, ok.stderr
    assert "ok:" in ok.stdout

    missing = subprocess.run(
        [sys.executable, "-m", "parkinsons_discovery", "show", "H-NOT-REAL"],
        cwd=ROOT, env=env, capture_output=True, text=True,
    )
    assert missing.returncode == 1
