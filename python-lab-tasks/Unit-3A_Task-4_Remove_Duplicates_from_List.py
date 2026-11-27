# Unit-3A Task-4: Remove duplicate elements from a list (keeps original order)

list_data = [1, 2, 2, 3, 1, 4, 3]

unique = []
for item in list_data:
    if item not in unique:
        unique.append(item)

print("Original:", list_data)
print("Without duplicates:", unique)
