def sum_data_structure(*args):
    total_sum = 0
    total_len = 0

    for arg in args:
        if isinstance(arg, int):
            total_sum += arg
        elif isinstance(arg, str):
            total_len += len(arg)
        elif isinstance(arg, list) or isinstance(arg, tuple):
            sub_sum, sub_len = sum_data_structure(*arg)
            total_sum += sub_sum
            total_len += sub_len
        elif isinstance(arg, dict):
            sub_sum, sub_len = sum_data_structure(*arg.values())
            total_sum += sub_sum
            total_len += sub_len

    return total_sum, total_len

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_sum, total_len = sum_data_structure(*data_structure)
result = total_sum + total_len
print("Total sum of all numbers:", total_sum)
print("Total length of all strings:", total_len)
print(result)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = sum_data_structure(data_structure)

print(result)
