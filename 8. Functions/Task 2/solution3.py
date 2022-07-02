import collections

def get_string_length(string):
    string = string.replace(' ', '')
    count_dict = dict(collections.Counter(string))
    length = sum(count_dict.values())
    return length