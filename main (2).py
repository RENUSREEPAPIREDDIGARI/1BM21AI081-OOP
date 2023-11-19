def is_palindrome(s):
    return s == s[::-1]

def get_palindrome(text):
    palindromes = []
    words = text.split()

    for word in words:
        if is_palindrome(word):
            palindromes.append(word)

    return palindromes

# Example usage
input_string = "madam refers radar to level noon civic kayak"
result = get_palindrome(input_string)

print("Palindromes in the string:")
print(result)

      