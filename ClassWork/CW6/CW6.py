def mnojestva():
    a = {1,2,3,3,3,4,5,6}
    a.discard(5)
    print(a)

    b = set([1,2,3,4,5,6,0])
    b.remove(2)
    print(b)

    c = set()
    c.add
    print(c)

    a.clear()
    print(f"очистить а ({a})")

    b1 = b.copy()#создание копии списка
    b.clear()
    print(b1)

    print(len(b1))#количество элементов

def operacii_mnojestv():
    qwe1={1,2,3}
    qwe2={1,2,6}

    print(qwe1.union(qwe2))
    print(qwe1|qwe2)

    print(qwe1.intersection(qwe2))#return совпадений
    print(qwe1&qwe2)# return совпадений побитовый метод

    print(qwe1.difference(qwe2))#Возврат уникальных элементы одного множества
    print(qwe1-qwe2)#Возврат уникальных элементов одного множества побитовый метод 

    print(qwe1.simetric_difference(qwe2))#Возврат уникальных элементов всех множеств
    print(qwe1^qwe2)#Возврат уникальных элементов всех множеств побитовый метод

    
    
def CW1():
    
    """
Уровень 1: Базовый
Задача: создайте программу,
которая определяет количество уникальных
символов в строке, введённой пользователем."""

    a = {1,2,3,7}
    b = {1,2,3,4,5}
    print(len(a^b))




def CW2():
    """Уровень 2: Средний

Задача: напишите программу,
которая принимает список чисел от пользователя
и определяет, есть ли в этом
списке одинаковые элементы (дубликаты)."""

    my_str = input("Введите элемент списка через пробел: ")
    my_list = my_str.split(' ')

    for i in range(len(my_list)):
        a = int(my_list[i])
        my_list[i] = a
    
    my_set = set()

    pov_list = []
    for i in range(len(my_list)-1):
        my_set.add(my_list[i])
        try:
            my_set.remove(my_list[i+1])
            pov_list.append(my_list[i+1])
        except:
            continue
    print(f"Список повторов {pov_list}")


def CW3():
    """Уровень 3: Продвинутый

Задача: напишите программу,
которая принимает список слов от пользователя и определяет,
есть ли среди них анаграммы (слова, составленные из одних и тех же букв).
Если такие слова есть, программа должна вывести все группы анаграмм."""

    my_str = input("Введите слова через пробел: ")
    my_list = my_str.split(' ')
        
    new_list = []
    
    for i in my_list:
        new_list.append(set(list(i)))
    
    for i in range(len(new_list)):
        for j in range(len(new_list)):
            try:
                if new_list[i] == new_list[j+1]:
                    print(f"{my_list[i]} анограмма {my_list[j+1]}")
            except:
                continue



CW1()
CW2()
CW3()
        

    


    
















