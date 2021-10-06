#1 Найти pi
# по ряду Лейбница
'''
# Инициализировать знаменатель
k = 1
# Инициализировать сумму
s = 0

for i in range(1000000):
    # четные элементы индекса положительны
    if i % 2 == 0:
        s += 4/k
    else:
        # нечетные элементы индекса отрицательны
        s -= 4/k 
    # знаменатель нечетный
    k += 2     
print('Pi = ',s)


# по ряду Нилаканта

iterations = 1000000
multiplier = 1.0
start_denominator = 2.0
pi = 3.0
for i in range(1, iterations + 1):    
    pi += ( (4.0 / (start_denominator * (start_denominator + 1.0) * (start_denominator + 2.0)) ) * multiplier)
    start_denominator += 2.0
    multiplier *= -1.0

print("Pi = ",pi)    
'''

#2 
# Интресс
'''
M = int(input('Введите сумму, которую хотите занять: '))
P = float(input('Введите проценты: '))
K = int(input('Введите на сколько месяцев, хотите взять кредит: '))
P_MONTH = P // 12

#laenumakse=(laenu_summa*kuu_intress)/(1-1/(Math.pow((1+kuu_intress), aeg_kuudes)));

'''


su = float(input(" Ввести счёт данной суммы: "))
intress = int(input(" Ввести процент интресса: "))
'''
# Первый вариант
su = su + su*(intress/100)
print ("Первый год: " + str(round(su,2)))
su = su + su*(intress/100)
print ("Второй год: " + str(round(su,2)))
su = su + su*(intress/100)
print ("Третий год: " + str(round(su,2)))
su = su + su*(intress/100)
print ("Четвёртый год: " + str(round(su,2)))
su = su + su*(intress/100)
print ("Пятый год: " + str(round(su,2)))
print ("После пяти лет: " + str(round(su,2)))
'''


# Второй вариант
su = su*(1 + intress/100)**12
print("После одного года: " + str(round(su,2)))

