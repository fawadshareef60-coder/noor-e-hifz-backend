#!/bin/bash

# Noor-e-Hifz AI Digital Madrasa
# Automated System Boot Configuration Script

echo "===================================================="
echo "⚡ Starting Noor-e-Hifz API Backend Gateway Engine... ⚡"
echo "===================================================="

# 1. Automatic installation audit check for dynamic package sync
echo "⏳ Step 1: Checking and syncing application dependencies..."
pip install -r requirements.txt

# 2. Launching the ASGI Application Server wrapper
echo "🚀 Step 2: Launching Uvicorn production server routing framework..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
