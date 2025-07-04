import random

class RandomError(Exception):
    """Custom Exception for random errors"""
    def __init__(self, message="An error occurred due to randomness"):
        self.message = message
        super().__init__(self.message)

try:
    a = random.random()
    print(f"Generated random value: {a}")

    # Raise exception if the number is less than 0.5
    if a < 0.5:
        raise RandomError("Random number was less than 0.5!")

except RandomError as e:
    print(f"Unable to fetch: {e}")
