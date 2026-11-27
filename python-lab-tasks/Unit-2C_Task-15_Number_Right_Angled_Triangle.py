# Unit 2C Task 15 - number right angled triangle

rows = int(input("Enter number of rows: "))

for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, row_loop_var + 1):
        print(column_loop_var, end=" ")
    print()
