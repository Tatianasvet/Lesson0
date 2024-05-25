def test_function(a):
    b = a*3

    def inner_function(a):
        print("Я в области видимости функции test_function")
    inner_function(a)

    return b


a = 5
print(test_function(a))  # 'Я в области видимости функции test_function' и '15'

test_function(a)  # 'Я в области видимости функции test_function'

#inner_function(a)  - ошибка name 'inner_function' is not defined