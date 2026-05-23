#https://top-academy.site/2gqlsxwvrfkr3scojsvcrjzlcywlbx3h/?clckid=84989e55

#https://top-academy.site/nm9bjibbmckt9o66hhswnexynnpxrj4e/?clckid=aad5dc1e

"""Уровень 1: Базовый

Задача: напишите программу,
 которая находит минимальное значение в списке чисел,
  введённом пользователем."""

arr = [-90,70,0,321,35,3125,32151,-124]

def min_one(lst):
	minimum =  lst[0]
	for el in lst:
		if el < minimum:
			minimum = el
	return minimum

def min_two(lst):
	s_lst = sorted(lst)
	return s_lst[0]

print(min_one(arr))
print(min_two(arr))
print(arr)


"""Уровень 3: Продвинутый

Задача: напишите программу,
 которая удаляет все повторяющиеся элементы из списка
  и упорядочивает оставшиеся элементы по возрастанию."""

def task3_1(lst):
	set_lst = set(lst)
	new_list = list(set_lst)
	new_list.sort()
	return new_list

def task3_2(lst):
	r_lst = list()
	for el in lst:
		if el not in r_lst:
			r_lst.append(el)
	r_lst.sort()
	return r_lst

print(task3_1(arr))
print(task3_2(arr))
print(arr)


#https://top-academy.site/q9ds4johcpahuzxbkkbseduux4epxwt0/?clckid=0875a706

#https://top-academy.site/3nwfuriqojoo2kamgap5smcac7cfmeh9/?clckid=ae48426c


stec = list()

def stec(stec):

	while True:
		print("1. добавляет число в стек")
		print("2. Удалить число из стека")
		print("3. Содержимое стека")
		print("")

		user_liput_task = input("Введите номер команды: ").strip().lower()

		match user_liput_task:
			case "0":
				print("завершение программы")

			case "1":
				push_stec(stec)
				continue

			case "2":
				pop_stec(stec)
				continue

			case "3":
				print(show_stec(stec))
				continue

			case _:
				print("Не верный ввод, попробуйте снова")
				continue

def push_stec(lst):
	item = int(input("Введите число: "))
	lst.append(item)

def pop_stec(lst):
	if not lst:
		print("Cтэк пуст ")
		return
	el = lst.pop()
	print(f"удалено {el}")

def show_stec(lst):
	return lst if lst else "Cтек пуст"



from collections import deque
dequ = deque

def queue(dequ):
	while True:
		user_liput_task = input("Введите номер команды: ").strip().lower()

		print("1. добавляет число в очередь")
		print("2. Удалить число из очередь")
		print("3. Содержимое стека")
		print("")

		match user_liput_task:
			case "0":
				print("Завершение программы")
				break

			case "1":
				push_deque()
				continue

			case "2":
				pop_deque()
				continue

			case "3":
				show_deque()
				continue

			case _:
				print("Не верный ввод, попробуйте снова")
				continue

low_task = []
high_task = []

def push_deque():
	task = input("Add task: ")
	priority = input("input priority (В\Н)").strip().lower()
	match priority:
		case "в":
			high_task.append(task)

		case "н":
			low_task.append(task)

		case _:
			print("Error priority")

def pop_deque():
	if not low_task and high_task:
		print("Стек пуст")
		return
	el = high_task.pop() if high_task else low_task.pop()
	print(f"Был удалён {el}")

def show_deque():
	if not low_task and high_task:
		print("Стек пуст")
	print(low_task, high_task)




