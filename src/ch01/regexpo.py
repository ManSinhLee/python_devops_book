import re

# Literal Characters: Match the characters themselves.
pattern = re.compile("cat")
result = pattern.search("The cat is black.")
print(result.group())  # Output: cat

# Character Classes: Match any one of a set of characters.
pattern = re.compile("[aeiou]")
result = pattern.findall("Hello, World!")
print(result)  # Output: ['e', 'o', 'o']

# Quantifiers: Indicate the number of occurrences.
pattern = re.compile("a{2,3}")
result = pattern.search("baaaaanana")
print(result.group())  # Output: aaa

# Dot (.): Matches any character except a newline.
pattern = re.compile("c.t")
result = pattern.search("cat")
print(result.group())  # Output: cat

# Caret (^) and Dollar ($): Match the start and end of a line, respectively.
pattern = re.compile("^start.*end$")
result = pattern.match("start and end")
print(result.group())  # Output: start and end

# Backslash (): Escape special characters or introduce special sequences.
pattern = re.compile("\d{3}-\d{2}-\d{4}")
result = pattern.search("Social Security Number: 123-45-6789")
print(result.group())  # Output: 123-45-6789

# Search and Match:
pattern = re.compile("apple")
result = pattern.search("I like apples.")
if result:
    print("Found:", result.group())

# Find All Matches:
pattern = re.compile("\d+")
result = pattern.findall("There are 42 apples and 13 bananas.")
print(result)  # Output: ['42', '13']

# Substitute:
pattern = re.compile("apple")
result = pattern.sub("orange", "I like apples.")
print(result)  # Output: I like oranges.

cc_list = '''Ezra Koenig <ekoenig@vpwk.com>, Rostam Batmanglij <rostam@vpwk.com>, Chris Tomson <ctomson@vpwk.com,Bobbi Baio <bbaio@vpwk.com'''
print(f"Rostam in cc_list: {re.search(r'Rostam', cc_list)}")

if re.search(r'Rostam', cc_list):
    print('Found Rostam')

print(f"Character sets: {re.search(r'[R,B]obb[i,y]', cc_list)}")
print(f"Search ranges: {re.search(r'Chr[a-z][a-z]', cc_list)}")
print(f"Match: {re.search(r'[A-Za-z]+', cc_list)}")
print(f"Match ranges and position: {re.search(r'[A-Za-z]{6}', cc_list)}")
print(f"Find email address: {0}", re.search(r'[A-Za-z]+@[a-z]+\.[a-z]+', cc_list))

print(f"Character sets: {0}", re.search(r'\w+', cc_list))
print(f"Character sets: {0}", re.search(r'\w+\@\w+\.\w+', cc_list))




