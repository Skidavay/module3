print('Задача 6')

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример: 
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79

a = int(input('Введите первое чило: '))
b = int (input('Введите второе чило: '))
c = a % 100
d = b % 100
print(c + d)