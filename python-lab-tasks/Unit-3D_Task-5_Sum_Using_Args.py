# Unit-3D Task-5: Sum of any number of values using *args

def sum_values(*args):
    total = 0
    for value in args:
        total = total + value
    return total               # alternative: return sum(args)


print(sum_values(1, 2, 3))
print(sum_values(10, 20, 30, 40))
