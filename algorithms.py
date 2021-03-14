import time
import math


# измерение скорости работы алгоритма
def measure(func, n):
    start = time.time()

    if (n == None):
        func()
    else:
        func(n)

    final = time.time() - start
    
    print ("Выполнение алгоритма занято", '{0:0.23f}'.format(final), "секунд.")
    return final


# измерение точности результата
def compare(func, n):
    if (n == None):
        pi = func()
    else:
        pi = func(n)

    count = 0
    
    for i in range(50):
        if str('{0:0.60f}'.format(pi))[i] == str('{0:0.60f}'.format(math.pi))[i]:
            count += 1
        else:
            break
    
    if (count > 2):
        print ("Точность составляет", count - 2, "знаков после запятой.")
        return count - 2
    elif (count == 2):
        print ("Результат совпадает с Pi только в целой части.")
        return 0
    else:
        print ("Число совсем не совпадает с Pi.")
        return 0


# ряд Лейбница
def leibniz(n):
    pi = 0.0
    x = 1
    
    for i in range(n):
        if (i % 2 == 0):
            pi += 4 / x
        else:
            pi -= 4 / x
        x += 2

    print ('{0:0.52f}'.format(pi))
    return pi


# ряд Мадхавы
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
    
    print ('{0:0.52f}'.format(pi))
    return pi


# ряд Нилаканта
def nilakantha(n):
    pi = 3.0
    base = 2
    
    for i in range(n):
        if (i % 2 == 0):
            pi += 4 / (base * (base+1) * (base+2))
        else:
            pi -= 4 / (base * (base+1) * (base+2))
        base += 2

    print ('{0:0.52f}'.format(pi))
    return pi


# формула Виете
def viete(n):
    pi = math.sqrt(2) / 2
    var = math.sqrt(2)

    for i in range(n):
       var = math.sqrt(2 + var)
       pi *= var / 2

    pi = 2 / pi

    print ('{0:0.52f}'.format(pi))
    return pi


# формула Валлиса
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
    
    pi += 2
    
    print ('{0:0.52f}'.format(pi))
    return pi


# базовая формула Мэчина
def machin():
    pi = 4 * math.atan(1 / 5) - math.atan(1 / 239)
    pi *= 4

    print ('{0:0.52f}'.format(pi))
    return pi