# Unit 2C Task 11 - hollow diamond of stars

rows = int(input("Enter number of rows (half diamond): "))

# upper half
for row_loop_var in range(1, rows + 1):
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")
    for column_loop_var_dots in range(1, 2 * row_loop_var):
        # print star only at first and last position of the row
        if column_loop_var_dots == 1 or column_loop_var_dots == 2 * row_loop_var - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# lower half
for row_loop_var in range(rows - 1, 0, -1):
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")
    for column_loop_var_dots in range(1, 2 * row_loop_var):
        if column_loop_var_dots == 1 or column_loop_var_dots == 2 * row_loop_var - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
