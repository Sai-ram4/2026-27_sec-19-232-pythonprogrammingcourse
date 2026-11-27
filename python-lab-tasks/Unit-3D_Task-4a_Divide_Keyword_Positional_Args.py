# Unit-3D Task-4a: Keyword arguments vs positional arguments

def divide(a, b):
    return a / b


result = divide(b=10, a=20)     # keyword arguments: a=20, b=10
print(result)

result = divide(10, 20)         # positional arguments: a=10, b=20
print(result)
