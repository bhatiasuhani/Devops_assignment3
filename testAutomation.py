import requests
import time

# Wait for server to start (only needed if running server in same script)
time.sleep(2)

testcases = [
    {"url": "http://localhost:8000/add/2/2", "expected": 4, "description": "Test addition of 2 and 2"},
    # ... other test cases ...
]

def test():
    for case in testcases:
        try:
            response = requests.get(case["url"])
            response.raise_for_status()  # Raises exception for 4XX/5XX errors
            result = response.json()["result"]
            assert result == case["expected"], f"Test failed: {case['description']}. Expected {case['expected']}, got {result}"
            print(f"Test passed: {case['description']}")
        except requests.exceptions.RequestException as e:
            print(f"Connection error testing {case['url']}: {str(e)}")
            raise

    print("All tests passed!")

if __name__ == "__main__":
    test()