print('Задача 5. Часы')

# Напишите программу, 
# которая получает на вход число n — количество минут, — затем считает,
# сколько это будет в часах и сколько минут останется,
# и выводит на экран эти два результата.

n = int(input('Введите количество минут: '))
a, b = n // 60, n % 60
print('Количество часов:', a, 'количество оставшихся минут:', b)