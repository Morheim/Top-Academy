"""Домашнее задание 9
        Описание задачи:
    Создайте программу, которая генерирует последовательность чисел. Пользователь
может выбрать, хочет ли он получить последовательность всех чисел, только чётных
или только нечётных чисел в заданном диапазоне.
        Указания:
    1. Программа должна включать функцию-генератор number_sequence(start, end,
even=True), которая генерирует числа в заданном диапазоне:
        • Если even=True, возвращаются только чётные числа.
        • Если even=False, возвращаются только нечётные числа.
    2. Основная программа должна запрашивать у пользователя:
        • Начало и конец диапазона (start и end).
        • Тип последовательности: чётные или нечётные.
    3. Программа должна вывести числа, сгенерированные функцией.
        Ожидаемый результат:
Программа запрашивает ввод пользователя, а затем выводит последовательность чисел в
зависимости от выбора."""


def number_sequence(start: int, end: int, type_step: bool = True):
    for num in range(start, end + 1):
        if type_step and num % 2 == 0:
            yield num
        elif not type_step and num % 2 != 0:
            yield num


def main():
    print("=== Генератор последовательности чисел ===")
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))

        # от выстрела себе в ногу
        if start > end:
            start, end = end, start
            print(f"Диапазон скорректирован: {start} -> {end}")

        print("\nВыберите тип последовательности:")
        print("1. Все числа")
        print("2. Только чётные")
        print("3. Только нечётные")
        choice = input("Ваш выбор (1/2/3): ").strip()

        print("\nРезультат:")
        if choice == '1':
            seq = range(start, end + 1)
        elif choice == '2':
            seq = number_sequence(start, end, type_step=True)
        elif choice == '3':
            seq = number_sequence(start, end, type_step=False)
        else:
            print("Неверный выбор. По умолчанию выведены чётные числа.")
            seq = number_sequence(start, end, type_step=True)

        # Для удобного вывода в одну строку
        result = list(seq)

        if result:
            print(*result)
        else:
            print("В заданном диапазоне нет подходящих чисел.")

    except ValueError:
        print("Ошибка: пожалуйста, введите корректные целые числа.")


if __name__ == "__main__":
    main()