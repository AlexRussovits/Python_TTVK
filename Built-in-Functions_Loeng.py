'''

#Built-in functions

#1
a = int(input('Номер символа: '))
print('Символ по таблице Unicode: ',chr(a)) #символ
'''

'''
#2
a = input('Введите строку: ')
s = len(a) #длина строки
print('Длина строки: ', s)
'''

'''
#3
a = float(input('Введите десятичное число: '))
print('Число после округления: ', round(a))
'''

'''
#4

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
c = pow(a,b)
print('Число после возведения в степень: ', c)        
'''

'''
#5

a = input('Введите строку: ')
b = a.lower()
c = a.upper()
print('Строка в нижнем регистре: ', b, ' Строка в верхнем регистре: ',c)
'''

'''
#6
a = float(input('Введите первое десятичное число: '))
b = float(input('Введите второе десятичное число: '))
c = float(input('Введите третье десятичное число: '))
d = float(input('Введите четвёртое десятичное число: '))
e = float(input('Введите пятое десятичное число: '))
f = float(input('Введите шестое десятичное число: '))
print('Максимальное десятичное число: ',round(max(a,b,c,d,e,f),2), ' Минимальное десятичное число: ' ,round(min(a,b,c,d,e,f),2))
'''

# Mathematics functions
#1
import math

'''
a = math.sin(math.pi/4) #используем константу пи
b = math.sin(math.radians(45)) # конвертируем градусы в радианы
print('Первый вариант: ', round(a,4), ' Второй вариант: ', round(b,4))
'''

'''
#2
a = math.radians(60) # радианы
x = math.cos(2*a)
y = math.pow(math.cos(a),2) - math.pow(math.sin(a),2)
s
