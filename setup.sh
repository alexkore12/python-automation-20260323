#!/bin/bash
# Setup script for python-automation
set -e

echo "=== Python Automation Setup ==="

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
mkdir -p /tmp/backups
mkdir -p logs

# Copy .env if it doesn't exist
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "Created .env from .env.example — please edit it!"
fi

echo "✅ Setup complete!"
echo ""
echo "Activate the virtual environment:"
echo "  source venv/bin/activate"
echo ""
echo "Run the automation:"
echo "  python main.py --task healthcheck"
