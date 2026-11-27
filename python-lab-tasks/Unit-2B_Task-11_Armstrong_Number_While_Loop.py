# Unit 2B Task 11 - armstrong number (3 digits)
# eg: 153 = 1^3 + 5^3 + 3^3

number = int(input("Enter a 3-digit number: "))
original_number = number
armstrong_sum = 0

while number > 0:
    digit = number % 10
    armstrong_sum = armstrong_sum + digit ** 3
    number = number // 10

if armstrong_sum == original_number:
    print(f"{original_number} is an Armstrong number (sum of cubes of digits is {armstrong_sum})")
else:
    print(f"{original_number} is not an Armstrong number (sum of cubes of digits is {armstrong_sum})")
