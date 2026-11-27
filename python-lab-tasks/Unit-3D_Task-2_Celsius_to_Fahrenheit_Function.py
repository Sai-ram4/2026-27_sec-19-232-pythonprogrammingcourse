# Unit-3D Task-2: Function to convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


celsius = 37
fahrenheit = celsius_to_fahrenheit(celsius)
print("Fahrenheit:", fahrenheit)
