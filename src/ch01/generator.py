import sys

list_o_nums = [x for x in range(10)]
gen_o_nums = (x for x in range(10))

print(f"List of numbers: {list_o_nums}")
print(f"Generator of numbers: {gen_o_nums}")
print(f"Size of list: {sys.getsizeof(list_o_nums)}")
print(f"Size of generator: {sys.getsizeof(gen_o_nums)}")