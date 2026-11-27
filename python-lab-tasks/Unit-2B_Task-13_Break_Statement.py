# Unit 2B Task 13 - break statement (stop the loop at 5)

n = int(input("Enter N (print until N, stop early at 5): "))

# Approach 1 - for loop
for i in range(1, n + 1):
    if i == 5:
        print(f"Breaking for loop at number {i} (N was {n})")
        break
    print(f"for loop number = {i} (up to {n})")

# Approach 2 - while loop
i = 1
while i <= n:
    if i == 5:
        print(f"Breaking while loop at number {i} (N was {n})")
        break
    print(f"while loop number = {i} (up to {n})")
    i = i + 1
