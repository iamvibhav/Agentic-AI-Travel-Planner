#!/usr/bin/env python3
"""
Test script for the AI Trip Planner improvements.
Tests logging, exception handling, and export functionality.
"""

import sys
import os
import tempfile
from pathlib import Path

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_logging():
    """Test the logging functionality."""
    print("🧪 Testing logging functionality...")
    
    try:
        from logger.logging import get_logger, log_info, log_error
        
        # Test basic logging
        logger = get_logger("test")
        logger.info("Test info message")
        logger.error("Test error message")
        
        # Test convenience functions
        log_info("Test convenience info", test_param="value")
        log_error("Test convenience error", error_code="TEST_ERROR")
        
        print("✅ Logging tests passed!")
        return True
    except Exception as e:
        print(f"❌ Logging tests failed: {e}")
        return False

def test_exception_handling():
    """Test the exception handling functionality."""
    print("🧪 Testing exception handling...")
    
    try:
        from exception.exceptiohandling import (
            TripPlannerException, 
            WeatherAPIException, 
            PlacesAPIException,
            handle_exception
        )
        
        # Test basic exception
        try:
            raise TripPlannerException("Test error", "TEST_ERROR")
        except TripPlannerException as e:
            assert e.message == "Test error"
            assert e.error_code == "TEST_ERROR"
        
        # Test API exceptions
        weather_ex = WeatherAPIException("API failed", "London", 500)
        assert "London" in weather_ex.message
        
        places_ex = PlacesAPIException("Search failed", "Paris", "restaurants", 404)
        assert "Paris" in places_ex.message
        
        # Test exception to dict conversion
        ex_dict = weather_ex.to_dict()
        assert ex_dict["error"] == True
        assert ex_dict["message"] == weather_ex.message
        
        print("✅ Exception handling tests passed!")
        return True
    except Exception as e:
        print(f"❌ Exception handling tests failed: {e}")
        return False

def test_export_functionality():
    """Test the export functionality."""
    print("🧪 Testing export functionality...")
    
    try:
        from utils.export_utils import TravelPlanExporter, export_travel_plan
        
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
        
        # Test exporter initialization
        with tempfile.TemporaryDirectory() as temp_dir:
            exporter = TravelPlanExporter(temp_dir)
            
            # Test markdown export
            md_path = exporter.export_to_markdown(test_plan)
            assert Path(md_path).exists()
            assert Path(md_path).suffix == ".md"
            
            # Test text export
            txt_path = exporter.export_to_txt(test_plan)
            assert Path(txt_path).exists()
            assert Path(txt_path).suffix == ".txt"
            
            # Test JSON export
            plan_data = {"content": test_plan, "sections": {"day1": "Arrive in Paris"}}
            json_path = exporter.export_to_json(plan_data)
            assert Path(json_path).exists()
            assert Path(json_path).suffix == ".json"
        
        print("✅ Export functionality tests passed!")
        return True
    except Exception as e:
        print(f"❌ Export functionality tests failed: {e}")
        return False

def test_integration():
    """Test integration of all components."""
    print("🧪 Testing component integration...")
    
    try:
        from logger.logging import get_logger
        from exception.exceptiohandling import TripPlannerException
        from utils.export_utils import TravelPlanExporter
        
        # Test that all modules can be imported together
        logger = get_logger("integration_test")
        logger.info("Integration test started")
        
        # Test exception with logging
        try:
            raise TripPlannerException("Integration test error", "INTEGRATION_ERROR")
        except TripPlannerException as e:
            logger.error("Caught expected exception", extra_fields={"error": e.message})
        
        # Test export with logging
        with tempfile.TemporaryDirectory() as temp_dir:
            exporter = TravelPlanExporter(temp_dir)
            test_plan = "# Test Plan\nThis is a test."
            md_path = exporter.export_to_markdown(test_plan)
            logger.info("Export completed", extra_fields={"file_path": md_path})
        
        print("✅ Integration tests passed!")
        return True
    except Exception as e:
        print(f"❌ Integration tests failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Starting AI Trip Planner improvement tests...\n")
    
    tests = [
        ("Logging", test_logging),
        ("Exception Handling", test_exception_handling),
        ("Export Functionality", test_export_functionality),
        ("Integration", test_integration)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"Running {test_name} Tests")
        print('='*50)
        
        if test_func():
            passed += 1
        else:
            print(f"⚠️  {test_name} tests failed")
    
    print(f"\n{'='*50}")
    print(f"Test Results: {passed}/{total} test suites passed")
    print('='*50)
    
    if passed == total:
        print("🎉 All tests passed! The improvements are working correctly.")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
        return 1

if __name__ == "__main__":
    exit(main()) 