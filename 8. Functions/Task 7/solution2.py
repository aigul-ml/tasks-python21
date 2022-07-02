def is_palindrome(str_):
    str_ = str_.lower()
    if str_[::-1] == str_:
        return True
    else:
        return False

print(is_palindrome('Tenet'))