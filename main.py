#!/usr/bin/env python3
"""
LIVE_KIT_JARVIS - AI Personal Assistant
Main entry point for the application

This is the main script to run the Friday AI assistant.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.agent import entrypoint
from livekit import agents

if __name__ == "__main__":
    print("🤖 Starting Friday - Your AI Personal Assistant...")
    print("📡 Connecting to LiveKit...")
    
    try:
        agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
    except KeyboardInterrupt:
        print("\n👋 Friday shutting down gracefully...")
    except Exception as e:
        print(f"❌ Error starting Friday: {e}")
        sys.exit(1)
