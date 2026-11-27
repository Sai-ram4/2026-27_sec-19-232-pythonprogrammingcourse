# Unit-3C Task-3: Remove duplicates from a list using sets
# Note: a set does not guarantee the original order.

list_data = [1, 2, 2, 3, 1, 4, 3]

unique_set = set(list_data)
unique_list = list(unique_set)

print("Original:", list_data)
print("Unique set:", unique_set)
print("Unique list:", unique_list)
