items = [10, 20, 10, 30, 20, 40]
unique = []

for item in items:
    if item not in unique:
        unique.append(item)

print(unique)
# This code removes duplicates from the 'items' list and prints the list of unique items.