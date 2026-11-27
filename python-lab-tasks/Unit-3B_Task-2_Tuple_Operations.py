# Unit-3B Task-2: Tuple operations (concatenation, slicing, unpacking)

tuple_data = (1, 2, 3)
tuple_extra = (4, 5)

joined = tuple_data + tuple_extra       # concatenation
print("Joined:", joined)

print("Slice first two:", tuple_data[:2])   # slicing

a, b, c = tuple_data                    # unpacking
print("Unpacked:", a, b, c)
