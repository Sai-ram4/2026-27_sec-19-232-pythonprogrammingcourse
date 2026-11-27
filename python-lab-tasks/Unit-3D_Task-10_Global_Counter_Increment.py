# Unit-3D Task-10 (Optional): Increment a global counter using the global keyword

counter = 0


def increment():
    global counter
    counter = counter + 1
    print("Inside function, counter =", counter)


print("Before:", counter)
increment()
print("After:", counter)
