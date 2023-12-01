def keywords(first=1, second=2):
   '''Default values assigned'''
   print(f"first: {first}")
   print(f"second: {second}")

print(f"keyworks(0): {keywords(0)}")
print(f"keywords(6, 9): {keywords(6, 9)}")
print(f"keywords(second='one', first='two'): {keywords(second='one', first='two')}")