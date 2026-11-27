# Unit 2B Task 5 - factorial of a number

number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print(f"Factorial of {number} is {factorial}")
