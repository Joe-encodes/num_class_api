# FastAPI Number Classification API - HNG12 Assignment Stage 1 Task

[![Python Version](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)](https://fastapi.tiangolo.com/)
[![Deployed on Render](https://img.shields.io/badge/deploy%20on-Render-46C3D2)](https://render.com)

A public API built with FastAPI for the HNG12 Backend Internship Stage 0. Classifies a number and returns its properties, including whether it is prime, perfect, or an Armstrong number, along with a fun fact.

**Live Demo**: [https://your-app-name.onrender.com](https://your-app-name.onrender.com)

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
  - [Prerequisites](#prerequisites)
  - [Local Setup](#local-setup)
- [API Documentation](#api-documentation)
  - [Endpoint](#endpoint)
  - [Response Format](#response-format)
- [Deployment](#deployment)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Features

- **Number Classification**: Determines if a number is prime, perfect, or an Armstrong number.
- **Digit Sum Calculation**: Returns the sum of the digits of the number.
- **Fun Fact Integration**: Fetches a fun fact about the number using the Numbers API.
- **CORS Support**: Preconfigured middleware for cross-origin requests.
- **Auto-Generated Docs**: Interactive Swagger/OpenAPI documentation at `/docs`.
- **Scalable**: Ready for deployment on Render (or similar platforms).

---

## Tech Stack

- **Language**: Python 3.12
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Deployment**: Render
- **Version Control**: Git & GitHub

---

## Quick Start

### Prerequisites

- Python 3.11+
- Git
- Render account (free tier)

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/fastapi-number-classification.git
   cd fastapi-number-classification
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv  # Create virtual environment
   source venv/bin/activate  # Activate on Linux/macOS
   venv\Scripts\activate  # Activate on Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API locally**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**:
   - API Root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Documentation

### Endpoint

- **GET /api/classify-number** – Classifies a number and returns its properties.

#### Query Parameters:
- `number` (required): A valid integer, negative, or floating-point number.

#### Example Request:
```
GET /api/classify-number?number=28
```

### Response Format

```json
{
  "number": 28,
  "is_prime": false,
  "is_perfect": true,
  "properties": ["even"],
  "digit_sum": 10,
  "fun_fact": "28 is the 2nd perfect number."
}
```

---

## Deployment

### Deploy on Render

1. **Connect your GitHub repo to Render**
2. **Configure settings**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
3. **Deploy and monitor logs in the Render dashboard**

---

## Testing

### Manual Testing

```bash
curl https://your-app-name.onrender.com/api/classify-number?number=28
```

### Automated Testing (with pytest)

#### `tests/test_main.py`

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_classify_number():
    response = client.get("/api/classify-number?number=28")
    assert response.status_code == 200
    assert "number" in response.json()
    assert "is_prime" in response.json()
    assert "is_perfect" in response.json()
    assert "properties" in response.json()
    assert "digit_sum" in response.json()
    assert "fun_fact" in response.json()
```

### Run tests:

```bash
pytest -v
```

---

## Contributing

Pull requests are welcome! For major changes, open an issue first.

---

## License

GNU

---

## Acknowledgments

- HNG Internship for the project brief.
- FastAPI Documentation for best practices.
- Numbers API for providing fun facts.

---

## Contact

- **Email**: your-email@example.com  
- **GitHub**: https://github.com/your-username
- **LinkedIn**: linkedin.com/in/your-profile

## To Hire Other Developers like me

- **Python**: https://hng.tech/hire/python-developers
