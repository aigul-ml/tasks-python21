list_ = ['Paul', 'George', 'Ringo', 'John']


def getLongestString(list_of_strings):
    
    longest_string = ""

    for string in list_of_strings:
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string

print(getLongestString(list_))