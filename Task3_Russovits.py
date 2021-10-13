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
int(input(": "))
int(input(": "))
int(input(": "))
K = KuudeArv


print("Month\t\tLoan_Amount\t\tLoan_Payment\t\tInterest_Payment\t\tRepayment_of_Principal\t\tThe_Final_Balance")

for i in range(1,K+1):
    #print(month, "month.\t\t",round(M_LOAN,2), "\t\t",round(M_PAYMENT,2), "\t\t",round(InterestPayment,2), "\t\t",round(x,2), "\t\t",round(M_LB,2), "\t\t")
    
                                                                                            


#laenumakse=(laenu_summa*kuu_intress)/(1-1/(Math.pow((1+kuu_intress), aeg_kuudes)));


