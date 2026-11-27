# Unit-3D Task-12: Factorial of a number using recursion

def factorial(n):
    if n == 0 or n == 1:        # base case
        return 1
    return n * factorial(n - 1)  # recursive case


number = 5
print("Factorial:", factorial(number))
