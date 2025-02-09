from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
from pydantic import BaseModel  # For better input validation

# Initialize the FastAPI app
app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing) to allow requests from other domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (replace with specific domains in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Define a Pydantic model for input validation
class NumberInput(BaseModel):
    number: str  # Input number as a string to handle both integers and invalid inputs

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
    if n < 0:  # Armstrong numbers are defined only for non-negative integers
        return False
    digits = str(n)
    power = len(digits)
    return n == sum(int(digit) ** power for digit in digits)

# Function to determine parity (even or odd)
def find_parity(n: int):
    return "odd" if n % 2 != 0 else "even"

# Updated function: calculate the sum of digits using the absolute value
def digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))

# Function to fetch a fun fact about a number using the Numbers API
def get_fun_fact(n: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math", timeout=5)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "No fun fact available."
    except Exception:
        return "No fun fact available."

# Define the endpoint to classify a number
@app.get("/api/classify-number")
def classify_number(
    number: str = Query(..., description="A valid integer, negative, or floating-point number")
):
    try:
        # Attempt to convert the input to an integer
        n = int(number)
    except ValueError:
        # If conversion fails, return a 400 error with the invalid input
        raise HTTPException(
            status_code=400,
            detail={
                "number": number,
                "error": True,
                "message": "Invalid input. Please provide a valid integer."
            }
        )

    # Calculate number properties
    prime = is_prime(n)
    perfect = is_perfect(n)
    armstrong = is_armstrong(n)
    sum_digits = digit_sum(n)
    parity = find_parity(n)

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

# Optional: Run the app locally using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
