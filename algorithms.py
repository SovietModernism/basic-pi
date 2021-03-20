import time
import math

from decimal import Decimal, getcontext
getcontext().prec = 100


# вычисление двойного факториала
def double_fact_calc(n):
     if n <= 0:
         return 1
     else:
         return n * double_fact_calc(n - 2)


# измерение скорости работы алгоритма
def measure(func, n):
    start = Decimal(time.time())

    if (n == None):
        func()
    else:
        func(n)

    final = Decimal(time.time()) - start
    
    if (final == 0):
        print("Алгоритм выполнился менее, чем за 0E-20 секунд.")
    else:
        print ("Выполнение алгоритма занято", final, "секунд.")
    return final


# измерение точности результата
def compare(func, n):
    if (n == None):
        pi = func()
    else:
        pi = func(n)

    count = 0
    pi = str(pi)
    pi_real = str(Decimal(math.pi))
    
    for i in range(100):
        if pi[i] == pi_real[i]:
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
    pi = Decimal(0.0)
    x = 1
    
    for i in range(n):
        if (i % 2 == 0):
            pi += Decimal(4 / x)
        else:
            pi -= Decimal(4 / x)
        x += 2

    print (pi)
    return pi


# ряд Мадхавы
def madhava(n):
    pi = Decimal(0.0)
    x = 1
    
    for i in range(n):
        if (i % 2 == 0):
            pi += Decimal(1 / (x * pow(3, i)))
        else:
            pi -= Decimal(1 / (x * pow(3, i)))
        x += 2

    pi *= Decimal(math.sqrt(12))
    
    print (pi)
    return pi


# ряд Нилаканта
def nilakantha(n):
    pi = Decimal(3.0)
    base = 2
    
    for i in range(n):
        if (i % 2 == 0):
            pi += Decimal(4 / (base * (base+1) * (base+2)))
        else:
            pi -= Decimal(4 / (base * (base+1) * (base+2)))
        base += 2

    print (pi)
    return pi


# формула Виете
def viete(n):
    var = Decimal(math.sqrt(2))
    pi = Decimal(var / 2)

    for i in range(n):
       var = Decimal(math.sqrt(2 + var))
       pi *= Decimal(var / 2)

    pi = Decimal(2 / pi)

    print (pi)
    return pi


# формула Валлиса
def wallis(n):
    pi = Decimal(1.0)
    x = 2
    y = 1
    
    for i in range(n):
        if (i > 0) and (i % 2 == 0):
            x += 2
        
        if (i % 2 != 0):
            y += 2

        pi *= Decimal(x / y)
    
    pi += 2
    
    print (pi)
    return pi


# первый метод Эйлера для нахождения суммы ряда
def euler(n):
    pi = Decimal(0.0)
    
    for i in range(1, n):
       pi += Decimal(1 / pow(i, 2))
    
    pi *= 6
    pi = Decimal(math.sqrt(pi))

    print (pi)
    return pi


# формула Мэчина
def machin(n):
    pi = Decimal(0.0)
    arc_1 = Decimal(0.0)
    arc_2 = Decimal(0.0)
    base = 1
    
    # раскладываем первый арктангенс в ряд Тейлора
    for i in range(n):
        if (i % 2 == 0):
            arc_1 += Decimal(pow(1/5, base)) / base
        else:
            arc_1 -= Decimal(pow(1/5, base)) / base
        base += 2
    

    # раскладываем второй арктангенс в ряд Тейлора
    base = 1
    for i in range(n):
        if (i % 2 == 0):
            arc_2 += Decimal(Decimal(pow(1/239, base)) / base)
        else:
            arc_2 -= Decimal(Decimal(pow(1/239, base)) / base)
        base += 2

    
    pi = 4 * arc_1 - arc_2
    pi *= 4

    print (pi)
    return pi


# формула кратных рядов
def multiple_series(n):
    pi = Decimal(0.0)
    k = 1
    m = 1
    
    for i in range(1, n):
        for j in range(1, n):
            pi += Decimal(1 / pow((4 * j - 2), 2 * i))
    
    pi *= 8
    
    print (pi)
    return pi


# формула двойного факториала
def double_factorial(n):
    pi = Decimal(0.0)
    
    for i in range(n):
        pi += Decimal(math.factorial(i) / double_fact_calc(2 * i + 1))
    
    pi *= 2
    
    print (pi)
    return pi
