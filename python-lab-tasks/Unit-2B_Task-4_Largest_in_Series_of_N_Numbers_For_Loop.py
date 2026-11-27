# Unit 2B Task 4 - largest in a series of N numbers

total_input_numbers = int(input("Enter how many numbers: "))

# take the first number as largest, then compare with the rest
largest = float(input("Enter a number: "))

for i in range(total_input_numbers - 1):
    num = float(input("Enter a number: "))
    if num > largest:
        largest = num

print(f"Largest among {total_input_numbers} numbers is {largest}")
