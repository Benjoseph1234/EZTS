import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)

print('hello'.endswith('o'))
print('hello'.startswith('h'))
print('hello'.replace('l','t'))

print('100'.isdigit())
print('abc'.isalpha())
print('72'.isdecimal())
print('ab72'.isalnum())
print('HELLO WORLD'.istitle())

print('python programing'.capitalize())
print('python cython'.find('th'))
print('python cython'.rfind('th'))
print('python cython'.count('th'))
