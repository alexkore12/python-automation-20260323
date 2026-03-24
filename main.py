#!/usr/bin/env python3
"""
⚙️ Python Automation Scripts — Main Entry Point

Usage:
    python main.py [--task TASK_NAME] [--verbose]

Tasks:
    cleanup     - Clean up temporary files and old logs
    backup      - Create backups of important directories
    report      - Generate system status report
    healthcheck - Run health checks on configured services
"""

import argparse
import logging
import os
import sys
import json
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("/tmp/python_automation.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


def task_cleanup():
    """Clean up temporary files and old logs."""
    import glob
    import shutil

    patterns = ["/tmp/*.tmp", "/tmp/*.log", "/var/tmp/*.tmp"]
    removed = 0
    for pattern in patterns:
        for f in glob.glob(pattern):
            try:
                os.remove(f)
                logger.info(f"Removed: {f}")
                removed += 1
            except OSError as e:
                logger.warning(f"Could not remove {f}: {e}")
    logger.info(f"Cleanup complete. Removed {removed} files.")


def task_backup():
    """Create backups of important directories."""
    import shutil

    backup_dir = os.environ.get("BACKUP_DIR", "/tmp/backups")
    os.makedirs(backup_dir, exist_ok=True)

    dirs_to_backup = os.environ.get("BACKUP_DIRS", "").split(",")
    dirs_to_backup = [d.strip() for d in dirs_to_backup if d.strip()]

    if not dirs_to_backup:
        logger.info("No directories configured for backup (set BACKUP_DIRS in .env)")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    for src in dirs_to_backup:
        if not os.path.exists(src):
            logger.warning(f"Source directory not found: {src}")
            continue
        name = os.path.basename(src.rstrip("/"))
        backup_path = os.path.join(backup_dir, f"{name}_{timestamp}")
        try:
            shutil.copytree(src, backup_path)
            logger.info(f"Backed up {src} → {backup_path}")
        except Exception as e:
            logger.error(f"Backup failed for {src}: {e}")


def task_report():
    """Generate a system status report."""
    import platform

    report = {
        "timestamp": datetime.now().isoformat(),
        "hostname": platform.node(),
        "python_version": sys.version,
        "platform": platform.platform(),
        "environment": {
            k: v for k, v in os.environ.items()
            if not any(x in k.lower() for x in ["key", "secret", "password", "token"])
        },
    }
    report_path = "/tmp/python_automation_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    logger.info(f"Report saved to: {report_path}")
    print(json.dumps(report, indent=2))


def task_healthcheck():
    """Run health checks on configured services."""
    checks = []
    services = os.environ.get("HEALTHCHECK_SERVICES", "").split(",")
    services = [s.strip() for s in services if s.strip()]

    if not services:
        services = ["localhost"]

    for service in services:
        try:
            # Basic TCP connectivity check
            import socket
            host, port = service.split(":") if ":" in service else (service, 80)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((host, int(port)))
            sock.close()
            status = "healthy" if result == 0 else "unhealthy"
            checks.append({"service": service, "status": status})
            logger.info(f"{service}: {status}")
        except Exception as e:
            checks.append({"service": service, "status": "unknown", "error": str(e)})
            logger.warning(f"{service}: unknown ({e})")

    all_healthy = all(c["status"] == "healthy" for c in checks)
    if all_healthy:
        print("✅ All health checks passed")
    else:
        print("⚠️  Some health checks failed")
        sys.exit(1)


TASKS = {
    "cleanup": task_cleanup,
    "backup": task_backup,
    "report": task_report,
    "healthcheck": task_healthcheck,
}


def main():
    parser = argparse.ArgumentParser(
        description="⚙️ Python Automation Scripts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--task",
        default="healthcheck",
        choices=list(TASKS.keys()),
        help="Task to run (default: healthcheck)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    task_fn = TASKS.get(args.task)
    if task_fn:
        task_fn()
    else:
        logger.error(f"Unknown task: {args.task}")
        sys.exit(1)


if __name__ == "__main__":
    main()
