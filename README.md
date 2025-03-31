# Test Automation

## Backend API Test Automation with FastAPI and Requests

This guide covers how to automate backend API testing using **FastAPI** for the server and **Requests** for testing.

## **Table of Contents**
1. **Setting Up the FastAPI Server**
2. **Running the Server**
3. **Writing Automated Tests using Requests**
4. **Enhancing Tests with Pytest**
5. **Expanding the Idea for Real-World Projects**

---

## **1. Setting Up the FastAPI Server**
We'll create a simple API with three endpoints: **add, subtract, and multiply**.

### **Install FastAPI and Uvicorn**
```sh
pip install fastapi uvicorn
```

### **`apiserver.py`**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    return {"result": num1 + num2}

@app.get("/subtract/{num1}/{num2}")
def subtract(num1: int, num2: int):
    return {"result": num1 - num2}

@app.get("/multiply/{num1}/{num2}")
def multiply(num1: int, num2: int):
    return {"result": num1 * num2}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("apiserver:app", host="0.0.0.0", port=8000, reload=True)
```

---

## **2. Writing Automated Tests using Requests**

### **`testAutomation.py`**
```python
import requests

testcases = [
    {"url": "http://localhost:8000/add/2/2", "expected": 4, "description": "Addition test"},
    {"url": "http://localhost:8000/subtract/2/2", "expected": 0, "description": "Subtraction test"},
    {"url": "http://localhost:8000/multiply/2/2", "expected": 4, "description": "Multiplication test"}
]

def test():
    for case in testcases:
        response = requests.get(case["url"])
        result = response.json()["result"]
        assert result == case["expected"], f"Test failed: {case['description']}"
        print(f"Test passed: {case['description']}")
    print("All tests passed!")

test()
```

---

## **3. Enhancing Tests with Pytest**

### **`automation_test_pytest.py`**
```python
import pytest
import requests

testcases = [
    ("http://localhost:8000/add/2/2", 4, "Addition test"),
    ("http://localhost:8000/subtract/2/2", 0, "Subtraction test"),
    ("http://localhost:8000/multiply/2/2", 4, "Multiplication test"),
]

@pytest.mark.parametrize("url, expected, description", testcases)
def test_api(url, expected, description):
    response = requests.get(url)
    result = response.json()["result"]
    print(f"{description}. Expected {expected}, got {result}")
    assert result == expected

if __name__ == "__main__":
    pytest.main()
```

---

## **4. Expanding the Idea for Real-World Projects**

### **1. Database Integration**
- Connect FastAPI to **PostgreSQL** or **MongoDB**.
- Validate API responses against stored data.

### **2. Authentication and Authorization**
- Implement **OAuth2, JWT, API keys**.
- Test unauthorized access cases.

### **3. CI/CD Integration**
Use **GitHub Actions / Jenkins** to automate tests.

#### **GitHub Action for Pytest**
```yaml
name: API Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.10"
      
      - name: Install dependencies
        run: |
          pip install fastapi uvicorn pytest requests
      
      - name: Start FastAPI server
        run: |
          python apiserver.py &
        env:
          PYTHONUNBUFFERED: 1
      
      - name: Wait for server
        run: sleep 5
      
      - name: Run tests
        run: pytest automation_test_pytest.py
```

### **4. Performance Testing**
Use **`locust` or `k6`** for load testing.

### **5. Logging & Monitoring**
- Implement **CloudWatch** or **Elastic Stack** for logs.

---

## **Final Thoughts**
✅ Built a **FastAPI server**
✅ Wrote **automated tests** using `requests` and `pytest`
✅ Integrated **CI/CD pipelines**
✅ Discussed **real-world applications**
