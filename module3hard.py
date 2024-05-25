data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):

    total = 0

    for data in args:
        if isinstance(data, list) or isinstance(data, set) or isinstance(data, tuple):
            for item in data:
                total += calculate_structure_sum(item)

        else:
            if isinstance(data, (int, float)):
                total += data
            elif isinstance(data, str):
                total += len(data)
            elif isinstance(data, dict):
                for keys in data.keys():
                    if isinstance(keys, (int, float)):
                        total += keys
                    elif isinstance(keys, str):
                        total += len(keys)
                for value in data.values():
                    if isinstance(value, (int, float)):
                        total += value
                    elif isinstance(value, str):
                        total += len(value)
    return total


result = calculate_structure_sum(data_structure)
print(result)