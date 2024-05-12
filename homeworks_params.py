def print_params(a=1, b='str', c=True):
    print(a, b, c)

print_params()  # 1 str True
print_params(4)  # 4 str True
print_params(1, 'hello', False)  # 1 hello False
print_params(b=25)  # 1 25 True
print_params(c=[1, 2, 3])  # 1 str [1, 2, 3]


values_list = [34, 'STA', True]
values_dict = {'a': 55, 'b': 'my', 'c': False}

print_params(*values_list)  # 34 STA True
print_params(**values_dict)  # 55 my False

values_list_2 = ['good by', 11]
print_params(*values_list_2, 42)  # good by 11 42