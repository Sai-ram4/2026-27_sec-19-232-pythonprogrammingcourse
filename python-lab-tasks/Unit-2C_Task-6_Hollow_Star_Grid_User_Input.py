# Unit 2C Task 6 - hollow star grid (size from user)

rows = int(input("Enter grid size (rows and columns): "))

for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, rows + 1):
        # star only on the border
        if row_loop_var == 1 or row_loop_var == rows or column_loop_var == 1 or column_loop_var == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
