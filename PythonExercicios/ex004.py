a = input('Digite alguma coisa: ')
print('O tipo primitivo de "{}" é'.format(a), type(a))
print('"{}" só tem espaços?'.format(a), a.isspace())
print('"{}" é alfabético?'.format(a), a.isalpha())
print('"{}" está em maiusculas?'.format(a), a.isupper())
print('"{}" está em minusculas?'.format(a), a.islower())
print('"{}" é alfanumérico?:'.format(a), a.isalnum())
print('"{}" é um número?:'.format(a), a.isnumeric())
print('"{}" é decimal?'.format(a), a.isdecimal())
print('"{}" está captalizada?:'.format(a), a.istitle())