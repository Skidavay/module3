print('Задача 8. Режем число на части')

# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных

a = int(input('Введите четырехзначное число: '))

number = int(input('Введите четырехзначное число: '))
a = number % 10
b = number % 100 // 10
c = number // 100 % 10
d = number // 1000
print(a,b,c,d)