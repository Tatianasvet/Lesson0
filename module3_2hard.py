def flatten_list(data):
    result = []
    for item in data:
        if isinstance(item, tuple) or isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

data = ((), [{(2, 'urban', ('urban2', 35))}])
flat_data = flatten_list(data)
print(flat_data)
