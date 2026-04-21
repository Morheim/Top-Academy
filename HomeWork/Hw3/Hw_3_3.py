task_list = list()

def input_menu():
    text_menu = True
    while True:
        if text_menu == True:
            print("\nКонсольное меню:", end = "")
            print(" 1. Вывести список задач")
            print("\t\t 2. Добавить задачи")
            print("\t\t 3. Удалить задачу")
            print("\t\t 0. Выход")
            text_menu = False
        
        input_user = input("\nВыберите действие: ").strip().lower()
        match input_user:
            case "1":
                get_all_task()
            case "2":
                set_task()
            case "3":
                deleting_task()
            case "0":
                print("Завершение работы программы !\n")
                break
            case _:
                print("Не верный ввод\n")
                continue


def get_all_task():
    if not task_list:
        print("\nСписок задач пуст")
        return False
    else:
        print("\nСписок задач:")
        for i in range(len(task_list)):
            print(f"+++++++++++++(№{i+1} {task_list[i]})")


def set_task():
    print("\nВведите ваши задачи через ENTER, \nдля выхода в меню введите (0)")
    while True:
        input_task = input(f"\tЗадача №{len(task_list) + 1}. ").strip().capitalize()
        if input_task == "0":
            break
        if input_task == "":
            input_task = input(f"\tЗадача №{len(task_list) + 1}. ").strip().capitalize()
        else:
            task_list.append(input_task)


def deleting_task():
    if get_all_task() != False:
        input_index = input(f"\nКакую задачу удалить? № ").strip()
        while True:
            if not input_index.isdigit():
                input_index = input(f"\nКакую задачу удалить ? № ").strip()
            else:
                input_index = int(input_index)
                task_list.pop(input_index - 1)
                break
                    

if __name__ == "__main__":
    input_menu()
