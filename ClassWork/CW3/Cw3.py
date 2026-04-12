#https://top-academy.site/3uruic4p9dcbekwsseda2jj0cxdkpbgj/?clckid=95fc2ab2

#https://top-academy.site/asgtzuyssebymg23xksdroatgip5dtgh/?clckid=3e020f02

def cw1():

    summ = 0

    while True:
        num = float(input("Введите число: "))
        if num == 0:
            break
        if num > 0:
            summ += num

    print(f"Сумма: {summ}")


def cw2():
    count = 0

    while True:
        batch = input("Введите кол-во товаров в партии: ")
        if not batch.isdigit():
            print("Кол-во должно быль беззнаковым числом")
            continue
        batch = int(batch)
        if batch == 0:
            break
        count += batch

    print(f"Кол-во товаров: {count}")


def cw3():
    count = 0
    
    days = int(input("Введите кол-во дней: "))
    while not days.isdigit():
        print("Кол-во дней должно быть не отрецательным")
        days = int(input("Введите кол-во дней: "))


    for day in range(days):
        print(f"День №{day+1}")
        batch = input("Введите кол-во товаров в партии: ")

        while not batch.isdigit():
            print("Некоректный ввод, введите ещё раз")
            batch = input("Введите кол-во товаров в партии: ")

        batch = int(batch)
        count += batch
        
    print(f"Кол-во товаров: {count}")

    





















