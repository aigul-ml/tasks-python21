def is_palindrome(str_):
    str_ = str_.lower()
    return True if str_[::-1] == str_ else False

print(is_palindrome('Tenet'))