
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    res = 0
    print(args)
    for i in args:
        if isinstance(i, int):
           res += i
        elif isinstance(i, str):
            res += len(i)
        elif isinstance(i, list):
            k = [i]
            for k in i:
            if isinstance(k, int):
                res += k
            elif isinstance(k, str):
                res += len(k)

        elif isinstance(i, dict):
            for key in i.items():
                print(key)
    print(res)

    return res



calculate_structure_sum(*data_structure)







