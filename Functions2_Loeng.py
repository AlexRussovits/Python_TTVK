import math
import random
#1
'''
def Quadratic_equation():
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    D = math.pow(b,2) - 4*a*c
    print(D)
    if D < 0:
        print('Корней нет')
    elif D == 0:
        x1=x2=(-b)/2*a
        print('Корень: ', x1)
    else:
        x1=(-b + math.sqrt(D)) / 2*a
        x2 =(-b - math.sqrt(D)) / 2*a
        print('Первый корень: ', x1)
        print('Второй корень: ', x2)
Quadratic_equation()
'''
#2
'''
def Addition_Two_Fractions():
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    d = int(input('d = '))
    y = (a*d + c*b) / (b*d)
    e = int(y)
    l = round(y - e,2)
    print("Ответ: ", e,"/",l)
Addition_Two_Fractions()
'''

'''
#3
def Finding_Square():
    a = int(input('a = '))
    b = int(input('b = '))
    if a>b:
        S1 = math.pow(a,2)
        S2 = math.pow(b,2)
        S = S1-S2
    else:
        print('Не соответствует условию задачи')        
    print('Площадь данной фигуры',S)
Finding_Square()
'''
#4
'''
count = 0
def Calculator():
    for i in range(5):
        a = random.randint(1,9)
        b = random.randint(1,9)
        print(a,'*',b, end =' = ')
        res = int(input(''))
        if res ==a*b:
            global count       
            count += 1
        print('Количество правильных ответов: ',count)
    if count == 5:
        print('Молодец!')
    if count == 4 or count == 3:
        print('Надо бы ещё поучить!')
    if count < 2:
        print('Срочно нужно учить таблицу умножения!')
Calculator()                
'''

#5
'''
def circle_square():
    r = int(input('Введите радиус: '))
    S = round(math.pi*math.pow(r,2),2)
    print('Площадь круга: ',S)
    
def rectangle_square():
    a = int(input('Введите длину прямоугольника: '))
    b = int(input('Введите ширину прямоугольника: '))
    S = a*b
    print('Площадь прямоугольника: ',S)
def triangle_square():
    a = int(input('Первая сторона треугольника: '))
    b = int(input('Вторая сторона треугольника: '))
    c = int(input('Третья сторона треугольника: '))
    p = (a+b+c)/2
    S = round(math.sqrt(p*(p-a)*(p-b)*(p-c)),2)
    print('Площадь треугольника: ',S)

print('Площадь какой фигуры вы хотите найти?\n 1. Площадь круга\n 2. Площадь прямоугольника\n 3. Площадь треугольника')
task = int(input(''))

if task == 1:
    circle_square()
if task == 2:
    rectangle_square()
if task == 3:
    triangle_square()
'''
#6
'''
def digits(n):
    i = 0
    while n > 0:
        n = n//10
        i += 1
    return i
num = abs(int(input('Введите число: ')))
print('Количество разрядов: ', digits(num))
'''

'''
#7
def sum_digits(n,summands):
    #n = int(input('n =  '))
    su = 0
    summand = int(input('Сколько слагаемых хотите сложить? '))
    for i in range(n,n+10):
        su += n
        i+=1
    return i
print(sum_digits(10,6))                    
'''

#8

