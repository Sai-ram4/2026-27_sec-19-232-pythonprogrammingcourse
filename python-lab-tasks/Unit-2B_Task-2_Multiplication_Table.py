# Unit 2B Task 2 - multiplication table

number = int(input("Enter a number: "))

# Approach 1 - for loop
print("Using for loop:")
for multiplier in range(1, 11):
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")

# Approach 2 - while loop
print("Using while loop:")
multiplier = 1
while multiplier <= 10:
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")
    multiplier = multiplier + 1
