#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$SCRIPT_DIR"

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
fi

echo "Installing test dependencies..."
pip install -r requirements.txt

echo "Running tests..."
pytest -v --tb=short

deactivate
