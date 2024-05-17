
def calculate_structure_sum(data_structure):
    total = 0

    for component in  data_structure:
        if isinstance(component, (int, float)):
            total += component
        elif isinstance(component, str):
            total += len(component)



    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

