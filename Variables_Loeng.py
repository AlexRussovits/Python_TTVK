import math
'''
#Практика
numberInt = 10
numberFloat = 8.4
text = "Yes"
numberNotInt = numberInt * 3.5
numberFloat -= 1
numberInt / numberFloat
text = '"' + "No"*2 + "_" + "Yes"*3 + '"'  
print(numberInt, numberNotInt,numberFloat, text)

print('----------------------------------')
#Задание 1
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
s = a + b + c
m = a * b * c
avg = (a+b+c)/3
print('Результат: ',s)
print('Результат: ', m) 
print('Результат: ', round(avg,2))
#-----------------------------------------------
print('-----------------------------------------')

#Задание 2
####1
a = int(input('a = '))
b = int(input('b = '))
summa = a + b
subt = a - b
m = a*b
d = a/b
q = a**b
v = a%b
h = a//b

print('Сумма: ', summa,'Разность: ', subt, 'Произведение: ', m, 'Частное: ',round(d,2), 'Возведение в степень: ', q,
      'Остаток от деления',round(v,2), 'Целочисленное деление: ', h)
      
#####2
side = int(input('Введите сторону квадрата: '))
p = 4 * side
print('Периметр квадрата: ', p)

#####3

a = int(input('Введите значение первой стороны прямоугольника: '))
b = int(input('Введите значение второй стороны прямоугольника: '))
p = 2 * (a + b)
s = a * b
print('Периметр прямоугольника: ', p)
print('Площадь прямоугольника: ', s)

#####4

r = int(input('Введите радиус круга: '))
C = 2*math.pi*r
S = math.pi*r**2
print('Длина окружности: ', round(C,2))
print('Площадь круга: ', round(S,2))
'''

#####5

a = float(input('Введите цену первого товара: '))
b = float(input('Введите цену второго товара: '))
c = float(input('Введите цену третьего товара: '))
summa = a + b + c
avg = (a+b+c)/3
print('Общая сумма трёх товаров: ', summa)
print('Средняя цена товаров: ', round(avg,2))


