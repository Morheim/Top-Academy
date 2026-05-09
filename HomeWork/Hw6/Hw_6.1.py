"""
   Описание задачи:
Создайте программу для управления реестром участников мероприятия, используя
кортежи, множества и словари. Пользователь должен иметь возможность
регистрировать новых участников, удалять их из реестра и просматривать полный
список с деталями.


    Указания:
1. Программа должна начинаться с пустого словаря участников.

2. Ключом в словаре должен быть кортеж, состоящий из имени и фамилии
участника, а значением — множество с их интересами.

3. Пользователь может добавить нового участника в реестр, используя команду
add.

4. Пользователь может удалить участника из реестра, используя команду remove.

5. Пользователь может просмотреть всех участников с их интересами, используя
команду list.

6. Пользователь может выйти из программы, используя команду exit.

7. Программа должна обеспечивать обработку ошибок ввода, таких как запрос
удаления несуществующего участника.


    Ожидаемый результат:
Программа циклически запрашивает у пользователя команду (add, remove, list или exit
для выхода), выполняет ее и затем снова запрашивает команду. Программа должна
корректно обрабатывать каждую команду и выдавать соответствующие сообщения о
статусе операции."""


def main_menu():
    registry = {}

    invalid_action_message = str("Невозможно выполнить действие, попробуйте выбрать другой вариант")

    def text_menu(pause = True, text_menu = True):
        if pause:
            input("Для продолжения нажмите Enter...")

        if text_menu:
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Консольное меню:")
            print("\t\t 1. Вывести список участников")
            print("\t\t 2. Добавить участников")
            print("\t\t 3. Удалить участника")
            print("\t\t 0. Выход")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    text_menu(False)

    while True:
        input_user = input("\nВыберите действие: ").strip()

        match input_user:
            case "1":
                if get_all_participants(registry) == False:
                    print(invalid_action_message)
                else:
                    text_menu()
            case "2":
                add_participant(registry)
                text_menu(False,True)
            case "3":
                if not get_all_participants(registry):
                    print(invalid_action_message)
                else:
                    remove_participant(registry)
                    text_menu()
            case "0":
                print("Завершение работы программы !\n")
                break
            case _:
                print("Не верный ввод\n")
                continue


def add_participant(registry):
    first_name = input("Введите имя: ").strip().title()
    last_name = input("Введите фамилию: ").strip().title()

    if not first_name or not last_name:
        print("Ошибка: Имя и фамилия не могут быть пустыми.")
        return

    key = (first_name, last_name)
    if key in registry:
        print(f"Внимание: Участник {first_name} {last_name} уже зарегистрирован.")
        return

    interests_input = input("Введите интересы через запятую (или оставьте пустым): ").strip()
    if interests_input:
        interests = set(i.strip() for i in interests_input.split(',') if i.strip())
    else:
        interests = set()

    registry[key] = interests
    print(f"Участник {first_name} {last_name} успешно добавлен в реестр.")


def remove_participant(registry):
    first_name = input("Введите имя участника для удаления: ").strip().title()
    last_name = input("Введите фамилию участника для удаления: ").strip().title()
    key = (first_name, last_name)

    if key in registry:
        del registry[key]
        print(f"Участник {first_name} {last_name} удален из реестра.")
    else:
        print(f"Ошибка: Участник {first_name} {last_name} не найден в реестре.")


def get_all_participants(registry):
    if not registry:
        print("Cписок участников пуст.")
        return False
    else:
        print("\nПолный список участников:")
        for (f_name, l_name), interests in registry.items():
            interests_str = ", ".join(sorted(interests)) if interests else "Не указаны"
            print(f"  {f_name} {l_name} | Интересы: {interests_str}")
        print()
        return True



if __name__ == "__main__":
    main_menu()
