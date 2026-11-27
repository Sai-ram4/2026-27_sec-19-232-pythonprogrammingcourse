# Unit 2C Task 9 - centered pyramid of stars

rows = int(input("Enter number of rows: "))

for row_loop_var in range(1, rows + 1):
    # spaces before the stars
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")
    # row i has 2*i - 1 stars
    for column_loop_var_dots in range(1, 2 * row_loop_var):
        print("*", end=" ")
    print()
