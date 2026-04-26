"""Задание 1
Напишите функцию, которая отображает на экран
форматированный текст, указанный ниже:

“Don't let the noise of others' opinions
drown out your own inner voice.”
                            Steve Jobs"""


def func1():
    print("""“Don't let the noise of others' opinions
drown out your own inner voice.”
                            Steve Jobs
""")

##func1()


"""Задание 2
Напишите функцию, которая принимает два числа
в качестве параметра и отображает все нечетные числа
между ними."""

##val1 = int(input("Введите число "))
##val2 = int(input("Введите число "))


def func2(a, b):
    if a>b:
        a,b=b,a
        
    for i in range(a, b+1):
        if i % 2 != 0 :
            print(i,end=" ")


##func2(val1,val2)

"""Задание 3
Напишите функцию, которая отображает
горизонтальную или вертикальную линию из некоторого символа.
Функция принимает в качестве параметра: длину линии,
направление, символ.

"""

def func3(lens,nap,sim):
    if nap == 1:
        print(sim*lens)
    elif b == 2:
        for i in range(lans):
            print(sim)
    else:
        print("Ошибка")

##v1 = int(input("Длинна линии "))
##v2 = int(input("1- горизонт, 2 - вертекаль "))
##v3 = input("Введите символ ")

##func3(v1,v2,v3)

"""Задание 4
Напишите функцию,
которая возвращает максимальное из четырёх чисел.
Числа передаются в качестве
параметров."""

##a = int(input("Введите число a "))
##b = int(input("Введите число b "))
##c = int(input("Введите число c "))
##d = int(input("Введите число d "))

def func4(a,b,c,d):
    numbers = [a, b, c, d]
    maximum = max(numbers)
    return (maximum)

##print(f"Большее число {func4(a,b,c,d)}")


"""Задание 5
Напишитефункцию, которая возвращает сумму чисел
в указанном диапазоне. Границы диапазона передаются
в качестве параметров"""

##a = int(input("Введите число a "))
##b = int(input("Введите число b "))

def func5(a, b):
    summ = 0
    for i in range(a, b + 1):
        summ = summ + i
        
    return summ

##func5(a,b)

"""Задание 6
Напишите функцию, которая проверяет является ли
число простым. Число передаётся в качестве параметра.
Если число простое нужно вернуть из метода true, иначе
false"""


def func6(value):
    for i in range(2,value):
        if vlaue % i == 0:
            return True
    return False

    
##while True:
##    val = int(input("Введите число "))    
##    print(f"{func6(val)}")

"""Задание 7
Напишите функцию, которая проверяет являетсяли
шестизначное число «счастливым».
Число передаётся в качестве параметра.
Если число счастливое нужно вернуть true, иначе false
    «Счастливое шестизначное число» — это число у которого
    сумма первых трёх цифр равна сумме трёх вторыхцифр.
Например, 123420 – счастливое 1+2+3 = 4+2+0,
а 723422 - 
"""


def func7(a):
    if len(str(a)) != 6:
        return("Дурак введи 6 цифр")
    
    a1=str(a)[0]
    a2=str(a)[1]
    a3=str(a)[2]
    a4=str(a)[3]
    a5=str(a)[4]
    a6=str(a)[5]
    if int(a1)+int(a2)+int(a3)==int(a4)+int(a5)+int(a6):
        return True
    else:
        return False

while True:
    print(func7(int(input("6 "))))
    
    













































