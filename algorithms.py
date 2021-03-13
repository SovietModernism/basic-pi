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
# быстрее, но правильно считает только до 11 знаков после запятой (12 если округлить)
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