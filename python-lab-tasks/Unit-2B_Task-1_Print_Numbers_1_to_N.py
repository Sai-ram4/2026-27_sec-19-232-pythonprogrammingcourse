# Unit 2B Task 1 - print numbers from 1 to N

n = int(input("Enter the value of N: "))

# Approach 1 - for loop
print("Using for loop:")
for i in range(1, n + 1):
    print(f"{i}")

# Approach 2 - while loop
print("Using while loop:")
i = 1
while i <= n:
    print(f"{i}")
    i = i + 1
