def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(3, 3, [])
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [10, 'Точка', False]
values_dict = {"a": 101, "b": 'Кочка', "c": False}
print_params(*values_list)
print_params (**values_dict)

values_list_2 = ["Prosto", True]
print_params(*values_list_2, 42)