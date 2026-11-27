# Unit-3D Task-14: GCD of two numbers using recursion (Euclidean algorithm)

def gcd(a, b):
    if b == 0:                  # base case
        return a
    return gcd(b, a % b)        # recursive case


x, y = 48, 18
print("GCD:", gcd(x, y))
