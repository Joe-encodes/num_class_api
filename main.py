from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse  # For consistent JSON responses
import requests

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to check if a number is prime
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# Function to check if a number is an Armstrong number
def is_armstrong(n: int) -> bool:
    digits = str(n)
    power = len(digits)
    return n == sum(int(digit) ** power for digit in digits)

# Function to calculate the sum of digits
def digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(n))

# Function to fetch a fun fact about a number
def get_fun_fact(n: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math", timeout=5)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "No fun fact available."
    except Exception:
        return "No fun fact available."

# Endpoint to classify a number
@app.get("/api/classify-number")
def classify_number(number: str = Query(..., description="A valid integer number")):
    try:
        # Attempt to convert the input to an integer
        n = int(number)
    except ValueError:
        # If conversion fails, return a 400 error with the invalid input
        return JSONResponse(
            status_code=400,
            content={
                "number": number,  # Include the invalid input
                "error": True,
                "message": "Invalid input. Please provide a valid integer."
            }
        )
    
    # Calculate number properties
    prime = is_prime(n)
    perfect = is_perfect(n)
    armstrong = is_armstrong(n)
    sum_digits = digit_sum(n)
    
    # Determine parity (even or odd)
    parity = "odd" if n % 2 != 0 else "even"
    
    # Build properties array based on Armstrong and parity
    properties = ["armstrong"] if armstrong else []
    properties.append(parity)
    
    # Get a fun fact using the Numbers API
    fun_fact = get_fun_fact(n)
    
    # Build and return the JSON response
    return {
        "number": n,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit_sum": sum_digits,
        "fun_fact": fun_fact
    }

# Run the app locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
