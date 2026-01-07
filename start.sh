#!/bin/bash

# Quick start script for Thiên Cơ Đại Tướng Quân

echo "🔮 Thiên Cơ Đại Tướng Quân - Quick Start"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies if needed
if ! python -c "import telegram" 2>/dev/null; then
    echo "📥 Installing dependencies..."
    pip install -r requirements.txt
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ Error: .env file not found!"
    echo "Please copy .env.example to .env and fill in your credentials."
    exit 1
fi

echo ""
echo "✅ Ready to start!"
echo ""
echo "Starting bot..."
echo "========================================"
echo ""

# Start the bot
python main.py
