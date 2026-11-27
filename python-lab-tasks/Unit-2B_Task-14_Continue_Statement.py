# Unit 2B Task 14 - continue statement (skip even numbers)

n = int(input("Enter N (print 1 to N, skip even numbers): "))

# Approach 1 - for loop
for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"Skipping even number {i} with continue (N is {n})")
        continue
    print(f"for loop odd number = {i} (up to {n})")

# Approach 2 - while loop
i = 1
while i <= n:
    if i % 2 == 0:
        print(f"Skipping even number {i} with continue (N is {n})")
        i = i + 1   # have to increase before continue, otherwise infinite loop
        continue
    print(f"while loop odd number = {i} (up to {n})")
    i = i + 1
