#!/usr/bin/env python3
"""
Health check script for python-automation.
Verifies all dependencies are available and the environment is properly configured.
"""

import sys


def check_python_version():
    """Verify Python version is 3.11+."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 11):
        print(f"❌ Python {version.major}.{version.minor} detected. Python 3.11+ required.")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_dependencies():
    """Verify required packages are installed."""
    required = ["dotenv", "requests", "yaml", "pydantic"]
    all_ok = True
    for pkg in required:
        try:
            __import__(pkg)
            print(f"  ✅ {pkg}")
        except ImportError:
            print(f"  ❌ {pkg} not installed")
            all_ok = False
    return all_ok


def main():
    print("=== Python Automation Health Check ===\n")
    checks = [check_python_version(), check_dependencies()]
    print()
    if all(checks):
        print("✅ All health checks passed")
        sys.exit(0)
    else:
        print("❌ Some health checks failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
