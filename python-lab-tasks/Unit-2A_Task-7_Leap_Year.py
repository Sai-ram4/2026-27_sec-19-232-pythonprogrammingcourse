# Unit 2A Task 7 - leap year
# rules: divisible by 400 -> leap year
#        divisible by 100 (but not 400) -> not a leap year
#        divisible by 4 (but not 100) -> leap year
#        otherwise -> not a leap year

year = int(input("Enter a year: "))

# Approach 1 - nested if-else
print("Approach 1 (nested if-else):")
if year % 400 == 0:
    print(f"{year} is a leap year")
else:
    if year % 100 == 0:
        print(f"{year} is not a leap year")
    else:
        if year % 4 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")

# Approach 2 - if-elif-else ladder
print("Approach 2 (if-elif-else ladder):")
if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Approach 3 - single if condition
print("Approach 3 (single condition):")
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
