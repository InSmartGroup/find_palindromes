import dictionary, functions

data = dictionary.read_library()
palindromes = functions.find_palindrome(data)

print(f"There are {len(data)} words in the dictionary.")
print(f"There are {len(palindromes)} palindromes among them.")
print(f"For example: {palindromes[3::8]}.")
