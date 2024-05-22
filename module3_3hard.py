def sum_str(component):
    i = 0
    i += len(component)
    return i

def sum_dict(component):
    sum_ = 0
    for keys in component.keys():
        sum_ += len(keys)
    for value in component.values():
        sum_ += value
    return sum_


def calculate_structure_sum(*args):
    total = 0

    for component in args:
        if isinstance(component, (int, float)):
            total += component

        elif isinstance(component, str):
            sum_str(component)

        elif isinstance(component, dict):
            sum_dict(component)