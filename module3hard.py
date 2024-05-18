
def calculate_structure_sum(*args):
    total = 0

    for component in  args:
        if isinstance(component, (int, float)):
            total += component
        elif isinstance(component, str):
            total += len(component)
        elif isinstance(component, dict):
            for keys in component.keys():
                if isinstance(keys, (int, float)):
                    total += keys
                elif isinstance(keys, str):
                    total += len(keys)
            for value in component.values():
                if isinstance(value, (int, float)):
                    total += value
                elif isinstance(value, str):
                    total += len(value)



    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)

