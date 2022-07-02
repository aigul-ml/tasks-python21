def is_palindrome(str_):
    return str_[::-1].lower() == str_.lower()

print(is_palindrome('Tenet'))