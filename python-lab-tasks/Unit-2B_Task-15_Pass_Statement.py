# Unit 2B Task 15 - pass statement (for multiples of 3)

n = int(input("Enter N (use pass for multiples of 3): "))

# Approach 1 - for loop
for i in range(1, n + 1):
    if i % 3 == 0:
        pass
        print(f"Used pass for multiple of 3: {i} (N is {n})")
    else:
        print(f"for loop number = {i} (up to {n})")

# Approach 2 - while loop
i = 1
while i <= n:
    if i % 3 == 0:
        pass
        print(f"Used pass for multiple of 3: {i} (N is {n})")
    else:
        print(f"while loop number = {i} (up to {n})")
    i = i + 1
