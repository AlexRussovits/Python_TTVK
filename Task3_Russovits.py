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

import math
#2 
# Интресс
ls = float(input("Введите ссуду, которую вы хотите взять: "))
ka = int(input("Введите на какой промежуток времени хотите взять ссуду(месяцы): "))
pa = int(input("Введите процент, на который вы хотите взять ссуду: "))
months = ka
ki = pa / 1200
laj = ls
lm = (ls*ki)/(1-1/(math.pow((1+ki),ka)))
llj = ls

print("Month\t\tLoan_Amount\t\t\tLoan_Payment\t\t\tInterest_Payment\t\t\tRepayment_of_Principal\t\tThe_Final_Balance")

for month in range(1,months+1):
    laj = llj
    im = laj*ki
    ptm = lm-im
    llj*=1+ki
    llj-=lm

    print(month, "month.\t\t   ",round(laj,2),"\t\t\t ",round(lm,2), "\t\t\t    ",round(im,2), "\t\t\t   ",round(ptm,2), "       \t\t\t",round(llj,2), "     \t\t")
    print()
    #print(sep = '-')                                                                                            
#laenumakse=(laenu_summa*kuu_intress)/(1-1/(Math.pow((1+kuu_intress), aeg_kuudes)));


