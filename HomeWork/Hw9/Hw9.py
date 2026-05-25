#   Описание задачи:
#       Напишите программу, которая извлекает все даты в формате ДД.ММ.ГГГГ из текста.
#       Указания:
#
#           1. Импортируйте модуль re для работы с регулярными выражениями.
#           2. Создайте функцию, которая будет принимать текст и возвращать список
# найденных дат.
#           3. Добавьте пример входных данных.
#           4. Вызовите функцию и выведите результат.
#     Ожидаемый результат:
#         Пример входных данных:
#             text = "Сегодня 25.04.2024, а завтра будет 26.04.2024."
#         Результат:
#             Найденные даты: ['25.04.2024', '26.04.2024']

import re
import sys
import os


def extract_dates(text):
    try:
        if not isinstance(text, str):
            raise TypeError("Ожидается строка (str), получен другой тип данных.")
        pattern = r'\b\d{2}\.\d{2}\.\d{4}\b'
        return re.findall(pattern, text)

    except TypeError as type_error_msg:
        print(f"Ошибка типа данных: {type_error_msg}", file =sys.stderr)
        return []
    except Exception as exception_msg:
        print(f"Непредвиденная ошибка в extract_dates: {exception_msg}", file= sys.stderr)
        return []


def main():
    input_file = "data.txt"


    if not os.path.exists(input_file):
        with open(input_file, "w", encoding = "utf-8") as files:
            files.write("Сегодня 25.04.2024, а завтра будет 26.04.2024.")


    try:
        with open(input_file, "r", encoding = "utf-8") as files:
            text_content = files.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.", file= sys.stderr)
        return
    except PermissionError:
        print(f"Ошибка: Нет прав доступа к файлу '{input_file}'.", file =sys.stderr)
        return
    except UnicodeDecodeError:
        print(f"Ошибка: Не удалось прочитать файл. Убедитесь, что кодировка UTF-8.", file =sys.stderr)
        return
    except Exception as exception_msg:
        print(f"Ошибка при чтении файла: {exception_msg}", file= sys.stderr)
        return


    found_dates = extract_dates(text_content)


    print(f"Найденные даты: {found_dates}")


if __name__ == "__main__":
    main()