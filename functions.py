def find_palindrome(data):
    palindromes = []

    for i in data:
        if i.lower() == i[::-1].lower():
            palindromes.append(i.lower())

    return palindromes