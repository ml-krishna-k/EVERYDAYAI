#!/usr/bin/env python3
"""
Simple test script to verify API endpoints are working correctly.
Run this after starting the server locally.
"""

import requests
import json
import sys

# Base URL for the API
BASE_URL = "http://localhost:8000"

def test_health_endpoints():
    """Test health check endpoints"""
    print("Testing health endpoints...")
    
    # Test root endpoint
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✓ Root endpoint: {response.status_code}")
        print(f"  Response: {response.json()}")
    except Exception as e:
        print(f"✗ Root endpoint failed: {e}")
        return False
    
    # Test health endpoint
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"✓ Health endpoint: {response.status_code}")
        print(f"  Response: {response.json()}")
    except Exception as e:
        print(f"✗ Health endpoint failed: {e}")
        return False
    
    return True

def test_fitness_endpoint():
    """Test fitness planning endpoint"""
    print("\nTesting fitness endpoint...")
    
    test_data = {
        "age": "25",
        "weight": "70",
        "height": "175",
        "fitness_goal": "lose weight",
        "fitness_level": "beginner",
        "available_days": "3"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/fitness", json=test_data)
        print(f"✓ Fitness endpoint: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"  Response contains result: {'result' in result}")
        else:
            print(f"  Error: {response.text}")
    except Exception as e:
        print(f"✗ Fitness endpoint failed: {e}")
        return False
    
    return True

def test_recipe_endpoint():
    """Test recipe generation endpoint"""
    print("\nTesting recipe endpoint...")
    
    test_data = {
        "query": "chicken curry with coconut milk"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/recipe", json=test_data)
        print(f"✓ Recipe endpoint: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"  Response contains result: {'result' in result}")
        else:
            print(f"  Error: {response.text}")
    except Exception as e:
        print(f"✗ Recipe endpoint failed: {e}")
        return False
    
    return True

def test_taskplan_endpoint():
    """Test task planning endpoint"""
    print("\nTesting taskplan endpoint...")
    
    test_data = {
        "user_name": "Test User",
        "tasks": ["Prepare presentation", "Gym workout", "Buy groceries"]
    }
    
    try:
        response = requests.post(f"{BASE_URL}/taskplan", json=test_data)
        print(f"✓ Taskplan endpoint: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"  Response contains result: {'result' in result}")
        else:
            print(f"  Error: {response.text}")
    except Exception as e:
        print(f"✗ Taskplan endpoint failed: {e}")
        return False
    
    return True

def main():
    """Run all tests"""
    print("EverydayAI Backend API Test Suite")
    print("=" * 40)
    
    # Check if server is running
    try:
        response = requests.get(f"{BASE_URL}/")
        print("✓ Server is running")
    except requests.exceptions.ConnectionError:
        print("✗ Server is not running. Please start the server first:")
        print("  python main.py")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error connecting to server: {e}")
        sys.exit(1)
    
    # Run tests
    tests = [
        test_health_endpoints,
        test_fitness_endpoint,
        test_recipe_endpoint,
        test_taskplan_endpoint
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\nTest Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All tests passed! API is ready for deployment.")
    else:
        print("✗ Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
