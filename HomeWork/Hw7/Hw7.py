def main_menu():
    def text_menu(pause = True, text_menu = True):
        if pause:
            input("Для продолжения нажмите Enter...")

        if text_menu:
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Введите номер задания от 1 до 7 или 0 для выхода из программы")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    text_menu(False, True)

    while True:
        dz = input("\nВыберите задание : ").strip()
        if dz.isdigit():
            dz = int(dz)

        match dz:
            case 1:
                dz1()
                text_menu()
            case 2:
                dz2()
                text_menu()
            case 3:
                dz3()
                text_menu()
            case 4:
                dz4()
                text_menu()
            case 5:
                dz5()
                text_menu()
            case 6:
                dz6()
                text_menu()
            case 7:
                dz7()
                text_menu()
            case 0:
                print("Завершение работы программы")
                break
            case _:
                print("Не верный выбор")
                text_menu(False, False)
                continue



def input_int(Text):
    while True:
        try:
            val = int(input(f"{Text}: "))
            if val > 0:
                return val
            print("Число должно быть больше нуля.\n")
        except ValueError:
            print("Введите корректное целое число.\n")

def dz1():
    """Задание 1
        Напишите функцию, которая отображает на экран
    форматированный текст, указанный ниже:
    “Don't compare yourself with anyone in this world…
    if you do so, you are insulting yourself.”
                                                Bill Gates"""

    print("""“Don't compare yourself with anyone in this world…
    if you do so, you are insulting yourself.”
                                                Bill Gates""")


def dz2():
    """Задание 2
        Напишите функцию, которая принимает два числа
    в качестве параметра и отображает все четные числа
    между ними."""

    def even_numbers(start,end):
        if start > end:
            start, end = end, start

        if start % 2 != 0:
            start += 1

        for i in range(start, end + 1, 2):
            print(i)

    even_numbers(input_int("Введите число 1:"), input_int("Введите число 2:"))


def dz3():
    """Задание 3
        Напишите функцию, которая отображает пустой или
    заполненный квадрат из некоторого символа. Функция
    принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
        ■ если она равна True, квадрат заполненный;
        ■ если False, квадрат пустой."""

    def draw_square(side_length, char, filled):
        if side_length <= 0:
            print("Ошибка: сторона квадрата должна быть больше 0.")
            return

        if filled:
            for _ in range(side_length):
                print(char * side_length)
        else:
            if side_length == 1:
                print(char)
            else:
                top_bottom = char * side_length
                print(top_bottom)  # Верхняя строка
                for _ in range(side_length - 2):
                    # Средние строки: символ + пробелы + символ
                    print(char + ' ' * (side_length - 2) + char)
                print(top_bottom)  # Нижняя строка

    def input_char():
        while True:
            val = input("Введите символ для отрисовки (например, #, *, @): ").strip()
            if val:
                return val[0]  # Берём только первый символ
            print("Поле не может быть пустым.\n")

    def input_filled_flag():
        while True:
            val = input("Квадрат заполненный? (True/False, да/нет, 1/0): ").strip().lower()
            if val in ('true', 'да', '1', 'y', 'yes', '+'):
                return True
            elif val in ('false', 'нет', '0', 'n', 'no', '-'):
                return False
            print("ведите одно из: True/False, да/нет, 1/0, y/n.\n")

    draw_square(input_int("Введите длину стороны квадрата (целое число > 0)"), input_char(), input_filled_flag())

def dz4():
    """Задание 4
        Напишитефункцию, которая возвращает минимальное
    из пяти чисел. Числа передаются в качестве параметров."""

    def min_numbers(a,b,c,d,f):
        temp_list = [a,b,c,d,f]
        numbers = list(set(temp_list))
        return numbers[0]

    val1 = input_int("Введите число 1")
    val2 = input_int("Введите число 2")
    val3 = input_int("Введите число 3")
    val4 = input_int("Введите число 4")
    val5 = input_int("Введите число 5")

    print(f"Минимальное число {min_numbers(val1,val2,val3,val4,val5)}")


def dz5():
    """Задание 5
    Напишите функцию, которая возвращает произведение чисел в указанном диапазоне.
    Границы диапазона передаются в качестве параметров.
     Если границы диапазона перепутаны
     (например, 5-верхняя граница, 25-нижняя граница), их нужно поменять местами."""

    def product_of_numbers(start, end):
        if start > end:
            start, end = end, start

        result = 1
        for num in range(start, end + 1):
            result *= num
        return result

    print(product_of_numbers(input_int("Введите число 1"), input_int("Введите число 2")))


def dz6():
    """Задание 6
        Напишите функцию, которая считает количество
    цифр в числе. Число передаётся в качестве параметра. Из
    функции нужно вернуть полученное количество цифр.
    Например, если передали 3456, количество цифр будет 4."""

    def how_many_numbers(number):
        tuple_of_digits = tuple(str(abs(number)))
        return len(tuple_of_digits)

    print(how_many_numbers(input_int("Введите число")))

def dz7():
    """Задание 7
        Напишите функцию, которая проверяет является ли
    число палиндромом. Число передаётся в качестве параметра.
    Если число палиндром нужно вернуть из функции
    true, иначе false.
        «Палиндром» — это число, у которого первая часть
    цифр равна второй перевернутой части цифр. Например,
    123321—палиндром(первая часть 123, вторая 321, которая
    после переворота становится 123),
    546645 — палиндром, а 421987 — не палиндром"""

    def palindrome(nums):
        s = str(nums)
        if len(s) != 6:
            raise ValueError("Дурак введи 6 цифр!")

        return s[0] == s[5] and s[1] == s[4] and s[2] == s[3]

    print(f"{palindrome(input('Введите число из 6 цифр: '))}")





if __name__ == "__main__":
    main_menu()