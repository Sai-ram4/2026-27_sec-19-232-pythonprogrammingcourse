# Unit-3D Task-9: A local variable does not change a global variable with the same name

x = 10                  # global variable


def demo():
    x = 20              # local variable (separate from the global x)
    print("Inside function, x =", x)


demo()
print("Outside function, x =", x)
