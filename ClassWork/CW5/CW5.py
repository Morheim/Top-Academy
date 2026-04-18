##https://top-academy.site/iqf4hetpip89srm7pspsggwfsdr3xc8r/?clckid=3dc1d720

##https://top-academy.site/2k5uepuhvbmtvgaxtu55j0n7pt4nnatg/?clckid=57f82c19

"""Уровень 1: Базовый

Задача: напишите программу, которая просит пользователя
ввести его имя и затем выводит его имя в верхнем регистре."""

def CW1():
    input_name = input("Введите ваше имя: ").strip()
    print(input_name.upper())

"""Уровень 2: Средний

Задача: напишите программу, которая должна запрашивать у пользователя
строку и выводить её в обратном порядке."""

def CW2():
    input_str = input("Введите текст: ")

    print(f"Обратная строка через срез: {input_str[::-1]}")

    print("".join(reversed(input_str)))


"""Уровень 3: Продвинутый

Задача: напишите программу, которая просит
пользователя ввести абзац текста.
Затем программа должна выводить количество
гласных и согласных букв в этом абзаце."""

import string

def CW3():
    p = input("Введите текст: ").strip().lower()

    glas = "феёиоуыэюяaeiouy"
    glas_count = 0
    sogl_count = 0
    punct_count = 0

    for char in p:
        if char.isalpha():
            if char in glas:
                glas_count += 1
            else:
                sogl_count += 1
                
        elif char in string.punctuation:
            punct_count += 1

    print(f"длинна строки {len(p)}")
    print(f"Гласных {glas_count}")
    print(f"Согласных {sogl_count}")
    print(f"Пунктуации {punct_count}")


#https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html?clckid=ded756e4

def test():
    n = input("введите номер билета: ").strip()
    
    if len(n) != 6:
        print("Некоректный ввод")
    else:
        sum1 = int(n[0])+int(n[1])+int(n[2])
        sum2 = int(n[3])+int(n[4])+int(n[5])
        if sum1 == sum2:
            print("Билет счастливый")
        else:
            print("Билет несчастливый")
        



























