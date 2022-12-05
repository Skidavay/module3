number = int(input('Введите четырехзначное число: '))
a = number % 10
b = number % 100 // 10
c = number // 100 % 10
d = number // 1000
number_rev = a * 1000 + b * 100 + c * 10 + d
print(number_rev)
