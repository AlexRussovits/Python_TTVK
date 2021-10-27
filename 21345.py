import math
def Leng(xA, yA, xB, yB):
    AB = math.sqrt((xA-xB)**2+(yA-yB)**2)
    return abs(AB)
print(Leng(3,4,5,7))
