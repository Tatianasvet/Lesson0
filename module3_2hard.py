def sum_data_structure(*args):
    total_sum = 0


    for arg in args:
        if isinstance(arg, int):
            total_sum += arg
        elif isinstance(arg, str):
            total_sum += len(arg)
        elif isinstance(arg, list) or isinstance(arg, tuple):
            sub_sum, sub_len = sum_data_structure(*arg)
            total_sum += sub_sum
            total_sum += sub_len
        elif isinstance(arg, dict):
            sub_sum, sub_len = sum_data_structure(*arg.values())
            total_sum += sub_sum
            total_sum += sub_len

    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "hello",
    ((), [{(2, 'urban', ('urban2', 35))}]

result = sum_data_structure(data_structure)

print(result)
