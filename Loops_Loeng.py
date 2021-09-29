#1 Нарисовать Квадрат
import random
'''
row = int(input('Количество строк: '))
col = int(input('Количество столбцов: '))
          
for i in range(row):
    for j in range(col):
        print('*', end = " ")
    print()
'''

'''
#2 Угадай число

number = random.randint(1,10)
tries = 0
print("I am thinking a number between 1 and 10")
print("You have to guess a number in three tries")

guess = input("Guess a number: ")
guess = int(guess)
tries += 1

if guess>number:
    print("Guess Lower...")
if guess<number:
    print("Guess Higher...")
while guess!=number and tries<3:
    guess = input("Try again: ")
    guess = int(guess)
    tries+=1

    if guess>number:
        print("Guess Lower...")
    if guess<number:
        print("Guess Higher...")

    if guess == number:
        print("You won!")
        print(f"Number of tries: {tries}")
    else:
        print("You Lost!")
        
'''

'''
#3 Гипотеза Сиракуза

nn = ''

#Проверка состоит ли строка из цифр и чтобы цифра не была меньше 
while not nn.isdigit() or int(nn) < 1:
    nn = input('Задайте любое натуральное число = ')
nn = int(nn)
print(nn, end = ' ')
while nn!=1:
    if nn%2==0:
        nn = nn/2
    elif nn%2!=0:
        nn = nn*3
        nn = nn + 1
        nn /= 2
    print(int(nn), end = ' ')



#4 Числа Фибоначчи
#Через While

n_terms = int(input("Сколько хочет чисел напечатать пользователь? "))

#Первые два значения

a = 0
b = 1
count = 0

# Проверка на положитиельное число
if n_terms <= 0:
    print("Пожалуйста введдите положительное число")
# Если одно значение, то вернёт a    
elif n_terms == 1:
    print("Последовательность чисел Фибоначчи до", n_terms, ":")
    print(a)
else:
    print("Последовательность чисел Фибоначчи: ")
    while count < n_terms:
        print(a)
        #Обновляем значения
        c = a + b
        a = b
        b = c
        count += 1



#For 
n = int(input("Введите номер диапазона для чисел Фибоначчи: "))

v_1 = 0
v_2 = 1

if n == 1:
    print(v_1)
else:
    print(v_1)
    print(v_2)
    for i in range(2,n):
        v_3 = v_1 + v_2
        v_1 = v_2
        v_2 = v_3
        print(v_3)        
'''        
