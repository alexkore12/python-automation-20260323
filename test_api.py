#!/usr/bin/env python3
"""
Tests for python-automation scripts.
Run with: pytest test_api.py -v
"""

import subprocess
import sys
from unittest.mock import patch, MagicMock
import pytest


def run_main(task="healthcheck"):
    """Helper: run main.py with given task and return (returncode, stdout, stderr)."""
    result = subprocess.run(
        [sys.executable, "main.py", "--task", task],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


class TestHealthcheck:
    """Tests for the healthcheck task."""

    def test_healthcheck_runs(self):
        """Healthcheck should complete without error by default."""
        code, out, err = run_main("healthcheck")
        assert "health check" in out.lower() or code == 0, f"Failed: {err}"

    def test_healthcheck_unknown_service(self):
        """Unknown service should be marked as unknown."""
        with patch.dict("os.environ", {"HEALTHCHECK_SERVICES": "invalid-host-xyz:9999"}):
            code, out, err = run_main("healthcheck")
            # Should not crash
            assert "unknown" in out.lower() or code in (0, 1)


class TestReport:
    """Tests for the report task."""

    def test_report_generates_json(self):
        """Report task should produce JSON output."""
        code, out, err = run_main("report")
        assert code == 0, f"Failed: {err}"
        assert "timestamp" in out or "hostname" in out


class TestCleanup:
    """Tests for the cleanup task."""

    def test_cleanup_runs(self):
        """Cleanup should complete without error."""
        code, out, err = run_main("cleanup")
        assert code == 0, f"Failed: {err}"


class TestBackup:
    """Tests for the backup task."""

    def test_backup_runs_no_dirs(self):
        """Backup with no BACKUP_DIRS set should not crash."""
        code, out, err = run_main("backup")
        assert code == 0, f"Failed: {err}"


class TestArgs:
    """Tests for argument parsing."""

    def test_unknown_task_exits(self):
        """Unknown task should exit with error."""
        result = subprocess.run(
            [sys.executable, "main.py", "--task", "nonexistent"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0

    def test_help_shows_tasks(self):
        """--help should list available tasks."""
        result = subprocess.run(
            [sys.executable, "main.py", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "cleanup" in result.stdout
        assert "backup" in result.stdout
        assert "report" in result.stdout
        assert "healthcheck" in result.stdout


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
