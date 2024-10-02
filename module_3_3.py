def print_params(a=1, b='text', c=True):
    print(f"a: {a}, b: {b}, c: {c}")

print_params()
print_params(42)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [3.14, 'text', False]
values_dict = {'a': 400, 'b': 'urban', 'c': [7, 8, 9]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'urbanstudent']
print_params(*values_list_2, 42)