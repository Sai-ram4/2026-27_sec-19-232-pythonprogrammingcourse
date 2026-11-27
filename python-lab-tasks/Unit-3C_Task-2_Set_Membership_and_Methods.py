# Unit-3C Task-2: Set membership testing and methods (add, remove, discard)

set_data = {10, 20, 30}
print("Set:", set_data)

print("20 in set?", 20 in set_data)
print("40 not in set?", 40 not in set_data)

set_data.add(40)
print("After add:", set_data)

set_data.remove(10)          # raises KeyError if item is missing
print("After remove:", set_data)

set_data.discard(99)         # no error even though 99 is not present
print("After discard:", set_data)
