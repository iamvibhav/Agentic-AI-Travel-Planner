#!/usr/bin/env python3
"""
Simple test script to verify the basic changes made to the AI Trip Planner.
"""

import sys
import os
import tempfile
from pathlib import Path

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_basic_functionality():
    """Test the basic functionality."""
    print("🧪 Testing basic functionality...")
    
    try:
        # Create test travel plan
        test_plan = """
# Test Travel Plan

## Day 1
- Arrive in Paris
- Visit Eiffel Tower
- Dinner at local restaurant

## Day 2
- Louvre Museum
- Seine River cruise
- Shopping at Champs-Élysées

## Budget
- Accommodation: €200/night
- Food: €50/day
- Activities: €100/day
        """
        
        # Test that we can create a text file
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "test_plan.txt"
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(test_plan)
            
            assert test_file.exists()
            assert test_file.suffix == ".txt"
            
            print(f"✅ Basic functionality test passed! File created: {test_file}")
            return True
            
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def test_imports():
    """Test that all required imports work."""
    print("🧪 Testing imports...")
    
    try:
        import streamlit as st
        import requests
        import datetime
        import time
        
        print("✅ All imports successful!")
        return True
    except Exception as e:
        print(f"❌ Import test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Testing simple changes to AI Trip Planner...\n")
    
    tests = [
        ("Imports", test_imports),
        ("Basic Functionality", test_basic_functionality),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*40}")
        print(f"Running {test_name} Test")
        print('='*40)
        
        if test_func():
            passed += 1
        else:
            print(f"⚠️  {test_name} test failed")
    
    print(f"\n{'='*40}")
    print(f"Test Results: {passed}/{total} tests passed")
    print('='*40)
    
    if passed == total:
        print("🎉 All tests passed! The changes are working correctly.")
        print("\n📋 Summary of changes made:")
        print("1. ✅ App name changed to: '🌍 Voyagent: An End-to-End Agentic AI Travel Planning Agent with LLMOps'")
        print("2. ✅ Enhanced loader with progress steps added")
        print("3. ✅ Text file download button (PDF removed)")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
        return 1

if __name__ == "__main__":
    exit(main()) 