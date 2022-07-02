list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude']

new_list = ['shorter' if sum([1 for _ in name]) < 5 else 'longer' for name in list_name]

print(new_list)