import time
import math


# ряд лейбница сходится очень медленно (8 после запятой при 1.000.000.000)
def leibniz(n):
    pi = 0.0
    x = 1
    
    for i in range(n):
        if (i % 2 == 0):
            pi += 4 / x
        else:
            pi -= 4 / x
        x += 2

    print(pi)


# ряд мадхавы является доработанной версией ряда лейбница и работает
# быстрее, но правильно считает только до 10 знаков после запятой (11 если округлить)
def madhava(n):
    pi = 0.0
    x = 1
    
    for i in range(n):
        if (i % 2 == 0):
            pi += 1 / (x * pow(3, i))
        else:
            pi -= 1 / (x * pow(3, i))
        x += 2

    pi *= math.sqrt(12)
    
    print(pi)


# ряд нилаканта сложнее, но работает гораздо быстрее
def nilakantha(n):
    pi = 3.0
    base = 2
    
    for i in range(n):
        if (i % 2 == 0):
            pi += 4 / (base * (base+1) * (base+2))
        else:
            pi -= 4 / (base * (base+1) * (base+2))
        base += 2

    print(pi)


# формула виете по точности аналогична нилаканте
def viete(n):
    pi = math.sqrt(2) / 2
    var = math.sqrt(2)

    for i in range(n):
       var = math.sqrt(2 + var)
       pi *= var / 2

    print (2 / pi)


# формула валлиса сходится очень медленно и по эффективности сходна с рядом лейбница
def wallis(n):
    pi = 1.0
    x = 2
    y = 1
    
    for i in range(n):
        if (i > 0) and (i % 2 == 0):
            x += 2
        
        if (i % 2 != 0):
            y += 2

        pi *= x / y
    
    print (pi * 2)


# формула мэчина
def machin():
    pi = 4 * math.atan(1 / 5) - math.atan(1 / 239)
    
    print (pi * 4)