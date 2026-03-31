def task(HW = 0, Task = 0):
    print("""__________________________________________________
    Home Work""",HW,"""
    Task """, Task,"""
++++++++++++++++++++++++++++++++++++++++++++++++++""")

def sum(A=0,B=0):
    return A+B

def diff(A=0,B=0):
    return A-B

def product(A=0,B=0):
    return A*B

def divisionInt(A=0,B=0):
    return A//B

def divisionFloat(A=0,B=0):
    return A/B


def dz1_3(A=0,B=0):
    print("A + B = ",sum(A,B))
    print("A - B = ",diff(A,B))
    print("A * B = ",product(A,B))

def dz1_4():
    print()
    value = int(input("Введите число: "))
    print("Введите процент от числа(",value,") %",end = "")
    percent = int(input())
    print("Результат равен: ", divisionFloat(product(value, percent), 100))

def dz1_5():
    width = int(input("Введите ширину прямоугольника: "))
    height = int(input("Введите высоту прямоугольника: "))
    print("Площадь вашего прямоугольника равна :",product(width, height))


task(1,2)
print(""" "Anyone who
   stops
     learning is old,
       whether at twenty or eighty".
                               Henry Ford""")

task(1,3)
dz1_3(2,3)

task(1,4)
dz1_4()

task(1,5)
dz1_5()
