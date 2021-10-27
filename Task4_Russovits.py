sum_x = y and sum_y = x#Amicable
x=int(input('Enter first number : '))  
y=int(input('Enter second number : '))  
sum1=0  
sum2=0  
for i in range(1,x):  
    if x%i==0:  
        sum1+=i  
for j in range(1,y):  
    if y%j==0:  
        sum2+=j  
if(sum1==y and sum2==x):  
    print('Given numbers are Amicable!')  
else:  
    print('Given numbers are not Amicable!')


 Number = int(input(" Please Enter any Number: ")) #Perfect
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print(" %d is a Perfect Number" %Number)
else:
    print(" %d is not a Perfect Number" %Number)
