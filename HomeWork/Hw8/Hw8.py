def main():
    tasks = ["Сделать домашнюю работу", "Помыть посуду", "Прочитать книгу"]

    task_iter = iter(tasks)

    completed_count = 0

    print("Добро пожаловать в менеджер задач!")
    print("Доступные команды: next, list, exit\n")

    while True:
        command = input("Введите команду > ").strip().lower()

        if command == "next":
            try:
                current_task = next(task_iter)
                print(f"Текущая задача: {current_task}")
                completed_count += 1
            except StopIteration:
                print("Все задачи выполнены!")

        elif command == "list":
            if completed_count < len(tasks):
                print("Оставшиеся задачи:")
                for task in tasks[completed_count:]:
                    print(f"\t*|{task}")
            else:
                print("Список задач пуст. Все задачи уже выполнены!")

        elif command == "exit":
            print("Программа завершена. До свидания!")
            break

        else:
            print("Неизвестная команда. Введите 'next', 'list' или 'exit'.")


if __name__ == "__main__":
    main()