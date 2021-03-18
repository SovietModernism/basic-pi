import time
import math


# вычисление двойного факториала
def double_factorial(n):
     if n <= 0:
         return 1
     else:
         return n * double_factorial(n - 2)


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


# первый метод Эйлера для нахождения суммы ряда
def euler(n):
    pi = 0.0
    
    for i in range(1, n):
       pi += 1 / pow(i, 2)
    
    pi *= 6
    pi = math.sqrt(pi)

    print ('{0:0.52f}'.format(pi))
    return pi


# формула Мэчина
def machin(n):
    pi = 0.0
    arc_1 = 0.0
    arc_2 = 0.0
    base = 1
    
    # раскладываем первый арктангенс в ряд Тейлора
    for i in range(n):
        if (i % 2 == 0):
            arc_1 += pow(1/5, base) / base
        else:
            arc_1 -=pow(1/5, base) / base
        base += 2
    

    # раскладываем второй арктангенс в ряд Тейлора
    base = 1
    for i in range(n):
        if (i % 2 == 0):
            arc_2 += pow(1/239, base) / base
        else:
            arc_2 -=pow(1/239, base) / base
        base += 2

    
    pi = 4 * arc_1 - arc_2
    pi *= 4

    print ('{0:0.52f}'.format(pi))
    return pi


# формула кратных рядов
def multiple_series(n):
    pi = 0.0
    k = 1
    m = 1
    
    for i in range(1, n):
        for j in range(1, n):
            pi += 1 / pow((4 * j - 2), 2 * i)
    
    pi *= 8
    
    print ('{0:0.52f}'.format(pi))
    return pi


# формула двойного факториала
def double_fact(n):
    pi = 0.0
    
    for i in range(n):
        pi += math.factorial(i) / double_factorial(2 * i + 1)
    
    pi *= 2
    
    print ('{0:0.52f}'.format(pi))
    return pi
