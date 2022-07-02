dict_ = {
    'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
    'Olga': {'history': 92, 'math': 96, 'literature': 81}, 
    'Nik': {'history': 84, 'math': 85, 'literature': 87}
}

new_dict = {key1: [key2 for key2, val2 in val1.items() if val2 == max(val1.values())][0] for key1, val1 in dict_.items()}

print(new_dict)