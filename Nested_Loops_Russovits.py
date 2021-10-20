'''
row = int(input('Введите количество строк: '))
col = int(input('Введите количество столбцов: '))
for i in range(row):
    for j in range(col):
        print('*', end = " ")
    print()
   

for i in range(6):
    for j in range(i+1):
            print('', end=" ")
    print('*', end=" ")
    print()    


a = 2
b = 1000
for n in range(a,b):
    R = 0
    for a in range(1,n+1):
        if(n%a) == 0:
            R+=1
    if R==2:
        print(n, end="\t")
print("\n")
print()

a = 1
n = int(input('Введите число: '))
for i in range(a,n):
    R=0
    for a in range(1, i+1):
        if(i%a) == 0:
            R+=1
    print(i,R*"+")
print("\n")
print()
'''

'''
summa = 0
while x>0:
    x = input("Введите число: ")
    if x == "stop":
        break
    x = int(x)
    max(x)
    n = x // 10
    x  // 10
print("Сумма чисел равна: ", summa)
input()
'''

print("Меню")
print("1.Прямоугольник \n2. Пирамида \n3.Простое число \n4.Делители")
while True:
    s=input("Номер события: ")
    if s=="1":
        row = int(input('Введите количество строк: '))
        col = int(input('Введите количество столбцов: '))
        for i in range(row):
            for j in range(col):
                print('*', end = " ")
            print()
    if n=="2":
        for i in range(6):
            for j in range(i+1):
                print('', end=" ")
        print('*', end=" ")
        print()
    if s=="3":
        a = 2
        b = 1000
        for n in range(a,b):
            R = 0
            for a in range(1,n+1):
                if(n%a) == 0:
                    R+=1
            if R==2:
                print(n, end="\t")
        print("\n")
        print()
     if s=="4":
         a = 1
         n = int(input('Введите число: '))
         for i in range(a,n):
            R=0
            for a in range(1, i+1):
                if(i%a) == 0:
                    R+=1
            print(i,R*"+")
        print("\n")
        print()
        
