def is_palindrome(s1):
    reversed = s1[::-1]
    reversed = reversed.upper()
    s1 = s1.upper()

    return reversed == s1
print(is_palindrome("Hannah"))