
def calculate_structure_sum(data_structure, *args):
    total_sum = 0

    for item in data_structure:
        if isinstance(item, int) or isinstance(item, float):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, list) or isinstance(item, dict) or isinstance(item, tuple):
            total_sum += calculate_structure_sum(item, *args)

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
