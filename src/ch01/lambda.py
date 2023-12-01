items = [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]
print(f"Sorted default item[0]: {sorted(items)}")

def second(item):
   '''return second entry'''
   return item[1]

print(f"Sorted second keys: {sorted(items, key=second)}")
print(f"Sorted item[1] keys: {sorted(items, key=lambda item: item[1])}")
print(f"Sorted item[2] keys: {sorted(items, key=lambda item: item[2])}")