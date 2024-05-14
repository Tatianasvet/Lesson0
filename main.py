def test(params, *args, name="Tan", **kwargs):
    print('number: ', params)
    print('versions: ', args)
    print('name:', name)
    print(kwargs)

test(21, 5, 7, 9, name='Tatiana', surname='Svet')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(7))