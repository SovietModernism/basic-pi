import time
import math

from decimal import *
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
    
    # значение Пи с точностью до 100-го знака после запятой
    pi_real = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
    pi_real = str(pi_real)
    
    for i in range(101):
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
    pi = Decimal('0.0')
    x = Decimal('1')
    
    for i in range(n):
        if (i % 2 == 0):
            pi += Decimal('4') / x
        else:
            pi -= Decimal('4') / x
        x += 2

    print (pi)
    return pi


# ряд Мадхавы
def madhava(n):
    pi = Decimal('0.0')
    x = 1
    
    for i in range(n):
        if (i % 2 == 0):
            pi += Decimal('1') / Decimal(x * pow(3, i))
        else:
            pi -= Decimal('1') / Decimal(x * pow(3, i))
        x += 2

    pi *= Decimal('12').sqrt()
    
    print (pi)
    return pi


# ряд Нилаканта
def nilakantha(n):
    pi = Decimal('3.0')
    base = 2
    
    for i in range(n):
        if (i % 2 == 0):
            pi += Decimal('4') / Decimal(base * (base+1) * (base+2))
        else:
            pi -= Decimal('4') / Decimal(base * (base+1) * (base+2))
        base += 2

    print (pi)
    return pi


# формула Виете
def viete(n):
    var = Decimal('2').sqrt()
    pi = var / Decimal('2')

    for i in range(n):
       var = 2 + var
       pi *= var / Decimal('2')

    pi = Decimal('2') / pi

    print (pi)
    return pi


# формула Валлиса
def wallis(n):
    pi = Decimal('1.0')
    x = Decimal('1')
    
    for i in range(1, n):
        pi *= Decimal(4 * x * x) / Decimal(4 * x * x - 1)
        x += 1
    
    pi *= 2
    
    print (pi)
    return pi


# первый метод Эйлера для нахождения суммы ряда
def euler(n):
    pi = Decimal('0.0')
    
    for i in range(1, n):
       pi += Decimal('1') / Decimal(pow(i, 2))
    
    pi *= 6
    pi = Decimal(pi).sqrt()

    print (pi)
    return pi


# формула Мэчина
def machin(n):
    pi = Decimal('0.0')
    arc_1 = Decimal('0.0')
    arc_2 = Decimal('0.0')
    base = Decimal('1')
    
    # раскладываем первый арктангенс в ряд Тейлора
    for i in range(n):
        if (i % 2 == 0):
            arc_1 += pow(Decimal('1') / Decimal('5'), base) / base
        else:
            arc_1 -= pow(Decimal('1') / Decimal('5'), base) / base
        base += 2
    

    # раскладываем второй арктангенс в ряд Тейлора
    base = Decimal('1')
    for i in range(n):
        if (i % 2 == 0):
            arc_2 += pow(Decimal('1') / Decimal('239'), base) / base
        else:
            arc_2 -= pow(Decimal('1') / Decimal('239'), base) / base
        base += 2

    
    pi = 4 * arc_1 - arc_2
    pi *= 4

    print (pi)
    return pi


# формула кратных рядов
def multiple_series(n):
    pi = Decimal('0.0')
    k = 1
    m = 1
    
    for i in range(1, n):
        for j in range(1, n):
            pi += Decimal('1') / Decimal(pow((4 * j - 2), 2 * i))
    
    pi *= 8
    
    print (pi)
    return pi


# формула двойного факториала
def double_factorial(n):
    pi = Decimal('0.0')
    
    for i in range(n):
        pi += Decimal(math.factorial(i)) / Decimal(double_fact_calc(2 * i + 1))
    
    pi *= 2
    
    print (pi)
    return pi
