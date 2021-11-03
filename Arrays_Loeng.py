import random
import math
#1
def array_digits(start_values, end_values, count_random_values=10):
    
    arr = []
    i = 0
    for i in range(count_random_values):        
        arr.append(random.randint(start_values,end_values))
    return arr
    
#a = array_digits(0,100,10)
#print(a)

#2
def arr_functions():
    c = array_digits(0,100)
    print(c)
    print(sum(c))
    print(max(c))
    print(min(c))
#arr_functions()

#3
def sub_value():
    d = array_digits(0,100)
    print(d)
    value = int(input('Введите число: '))
    i = 0
    while i < len(d):
        if d[i] < value:
            d[i] = value        
        i += 1
    return d  
#print(sub_value())

#4
def multiple_value():
    e = array_digits(0,100)
    print(e)
    s = []
    for i in range(len(e)):
        if e[i] % 9 == 0:
            s.append(e[i])    
    print(s)
    print(sum(s))
    if sum(s) >= 10 and sum(s) < 100:
        print('Сумма элементов является двухзначным числом')
    else:
        print('Не является двухзначным числом')
#multiple_value()
            
#5
def index_array():
    f = array_digits(0,100,20)
    g = []
    print(f) 
    for i in range(len(f)):
        if f[i] % 2 == 1:
            print(i, end = " ")
            g.append(i)
    print()
    print(len(g))
#index_array()

#6
def input_range():
    h = array_digits(0,100)
    print(h)
    interval1 = int(input('Введите первый интервал: '))
    interval2 = int(input('Введите второй интервал: '))
    for i in range(len(h)):
        if h[i] >= interval1 and h[i] <= interval2:
            print(h[i])
#input_range()

            
#7
def range_and_even_numbers():
    v = array_digits(0,100)
    print(v)
    inter1 = 15
    inter2 = 50
    for i in range(len(v)):
        if v[i] % 2 == 0:
            print(v[i], end = " ")
        elif v[i] >= inter1 and v[i] <= inter2:               
            print('Сумма квадратов чётных чисел: ',sum(v[i]**2))
range_and_even_numbers()
                
