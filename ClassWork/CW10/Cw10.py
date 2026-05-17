# https://top-academy.site/er8pidyex9r9hkpppjxvaxiblxtudymt/?clckid=1b61237f


# https://top-academy.site/obysvv3o4dclrklqs6qdls3nnr2mj7qz/?clckid=e1280a75

"""Уровень 1: Базовый

Задача: напишите программу, 
которая использует итератор для последовательного 
перебора строк текста,
разделённого символами перевода строки (\n). 
Программа должна по очереди выводить каждую строку.
Если строки закончились,
выведите сообщение: «Текст завершён»."""


def CW1_1():
	def read_file(name: str) -> list[str]:
		with open("text.txt", "r", encoding="utf-8") as file:
			data = file.read()
			lines = data.split("\n")
			return lines

	def main() -> None:
		lines = read_file("w1.txt")
		iterator = iter(lines)
		while True:
			try:
				print(next(iterator))
			except:
				print("Текст завершон")
				break

	main()


"""Уровень 2: Средний

Задача: напишите программу,
которая с помощью итератора перебирает 
числа в диапазоне с заданным шагом.
Пользователь должен указать начало, 
конец и шаг. Программа должна выводить 
числа по одному. Если числа закончились, 
выведите сообщение: «Диапазон завершён»."""


def CW2_1():
	def even_numbers_with_lc(start, end, step):
		return [number for number in range(start, end + 1, step)]

	start = int(input("Введите начало диапазона: "))
	end = int(input("Введите конец диапазона: "))
	step = int(input("Введите шаг диапазона: "))

	print(f"Числа от {start} до {end} с диапазоном {step}: ", end="")
	print(even_numbers_with_lc(start, end, step))
	numbers = even_numbers_with_lc(start, end, step)
	iterals = iter(numbers)

	print("Числа по порядку")
	while True:
		try:
			print(f"Число: {next(iterals)}")
		except StopIteration:
			print("«Диапазон завершён»")
			break


# CW2_1()
"""Уровень 3: Продвинутый

Задача: напишите программу, 
которая принимает от пользователя список чисел 
(вводится одной строкой, числа разделены пробелами).

Программа должна:

Использовать итератор для последовательного 
вывода каждого числа.
Определить сумму всех чисел, используя цикл с итератором.
После завершения вывода всех 
чисел сообщить: «Все числа выведены. Сумма: {сумма}»."""


def CW3_1():
	def read_file(name: str) -> list[str]:
		with open("text.txt", "r", encoding="utf-8") as file:
			data = file.read()
			nums = data.split(" ")
			return nums

	def main() -> None:
		lines = read_file("w2.txt")
		iterator = iter(lines)

		summa = 0
		print("Числа по порядку")
		while True:
			try:
				num = int(next(iterator))
				summa += num
				print(num)
			except StopIteration:
				print(f"Все числа выведены, их сумма = ({summa})")
				break

	main()


# CW3_1()

# https://top-academy.site/bctshmsdmttdxvlu5nhjvebjew5m8uwn/?clckid=1666a36a

def CW1_2():
	def rep_msg(msg, times):
		counter = 1
		while counter <= times:
			yield msg
			counter += 1

	for i in rep_msg("Text", 5):
		print(i)


def CW2_2():
	def filters_square(nums, tresshold):
		return [n ** 2 for n in nums if n > tresshold]

	numbers = [1, 4, 19, 20, 5, 3, 2, -7, 9]
	filtered = filters_square(numbers, 10)
	print(filtered)

# CW2_2()
