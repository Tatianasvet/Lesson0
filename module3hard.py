
def sum_(component):
    i = 0
    if isinstance(component, (int, float)):
        i += component
    elif isinstance(component, str):
        i += len(component)
        return i
pass

def calculate_structure_sum(*args):
    total = 0

    for component in args:
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

        # elif isinstance(component, list):
        #     for item in component:
        #         if isinstance(item, (int, float)):
        #             total += item
        #         elif isinstance(item, str):
        #             total += len(item)
        #         elif isinstance(item, dict):
        #             for keys in item.keys():
        #                 if isinstance(keys, (int, float)):
        #                     total += keys
        #                 elif isinstance(keys, str):
        #                     total += len(keys)
        #             for value in item.values():
        #                 if isinstance(value, (int, float)):
        #                     total += value
        #                 elif isinstance(value, str):
        #                     total += len(value)

        elif isinstance(component, tuple):
            return calculate_structure_sum(*component)
        elif isinstance(component,list):
            return calculate_structure_sum(*component)
        elif isinstance(component,set):
            return calculate_structure_sum(*component)




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


