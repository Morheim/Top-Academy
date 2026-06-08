def manage_tasks(task_stack):
    while True:
        print("\nУПРАВЛЕНИЕ ЗАДАЧАМИ (СТЕК)")
        print("1. Добавить задачу")
        print("2. Выполнить последнюю задачу")
        print("3. Посмотреть список задач")
        print("4. Назад в главное меню")

        choice = input("Выберите действие (1-4): ").strip()

        match choice:
            case '1':
                task = input("Введите новую задачу: ").strip()
                if task:
                    task_stack.append(task)
                    print("Задача добавлена.")
                else:
                    print("Задача не может быть пустой.")

            case '2':
                if task_stack:
                    completed_task = task_stack.pop()
                    print(f"Выполнена задача: '{completed_task}'")
                else:
                    print("Список задач пуст.")

            case '3':
                if task_stack:
                    print("Текущие задачи:")
                    for i, task in enumerate(reversed(task_stack), 1):
                        print(f"{i}. {task}")
                else:
                    print("Список задач пуст.")

            case '4':
                break

            case _:
                print("Неверный ввод.")


def manage_help(help_queue):
    while True:
        print("\nУПРАВЛЕНИЕ ПОМОЩЬЮ (ОЧЕРЕДЬ)")
        print("1. Добавить человека в очередь")
        print("2. Оказать помощь первому в очереди")
        print("3. Посмотреть очередь")
        print("4. Назад в главное меню")

        choice = input("Выберите действие (1-4): ").strip()

        match choice:
            case '1':
                person = input("Введите имя: ").strip()
                if person:
                    help_queue.append(person)
                    print("Человек добавлен в очередь.")
                else:
                    print("Имя не может быть пустым.")

            case '2':
                if help_queue:
                    served_person = help_queue.pop(0)
                    print(f"Помощь оказана: {served_person}")
                else:
                    print("Очередь пуста.")

            case '3':
                if help_queue:
                    print("Текущая очередь:")
                    for i, person in enumerate(help_queue, 1):
                        print(f"{i}. {person}")
                else:
                    print("Очередь пуста.")

            case '4':
                break

            case _:
                print("Неверный ввод.")


task_stack = []
help_queue = []

while True:
    print("\nГЛАВНОЕ МЕНЮ")
    print("1. Управление задачами (Стек)")
    print("2. Управление помощью (Очередь)")
    print("3. Выход")

    choice = input("Выберите действие (1-3) или введите 'exit': ").strip().lower()

    match choice:
        case '1':
            manage_tasks(task_stack)
        case '2':
            manage_help(help_queue)
        case '3' | 'exit':
            print("Выход из программы.")
            break
        case _:
            print("Неверный ввод.")
