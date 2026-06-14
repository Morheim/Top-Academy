#       Практика по теме "декораторы"
#https://top-academy.site/j1jgohtrukjhb5dzmnngh8ncz0cjzqb4/?clckid=35241d20

#       Уровень 1: Базовый
#
#   Задача: создайте декоратор, который выводит сообщение о том,
# сколько раз была вызвана декорируемая функция.
# Реализуйте декоратор и примените его к простой функции.

#Декоратор
def func_count(func):
	count = 0
	def wrapper(*args, **kwargs):
		nonlocal count
		count += 1
		print(f"{func.__name__} была вызвана {count} раз ")
		return func(*args, **kwargs)
	return wrapper

#Вызов декоратора
@func_count
def greed(name:str) -> str:
	return name
# Вызов функции
# print(greed("Oleg"))
# print(greed("Alex"))
# print(greed("Alena"))
# print(greed("Nikita"))

#Вызов
# greed была вызвана 1 раз
# Oleg
# greed была вызвана 2 раз
# Alex
# greed была вызвана 3 раз
# Alena
# greed была вызвана 4 раз
# Nikita


#       Уровень 2: Средний
#
#   Задача: создайте декоратор log_execution,
# который записывает имя функции и аргументы,
# с которыми она была вызвана, в текстовый файл log.txt.


def log_execution(func):
	def wrapper(arg ,*args, **kwargs):
		with open("log.txt", "a", encoding = "utf-8") as log_file:
			log_file.write(f"Имя функции: {func.__name__}, аргумент {arg}\n")
		return func(arg ,*args, ** kwargs)
	return wrapper

@log_execution
def function(arg:str)->str:
	return arg

#Вызов
# print(function("arg1"))
# print(function("arg2"))
# print(function("arg3"))
# print(function("arg4"))
# print(function("arg5"))
# print(function("arg6"))


#       Уровень 3: Продвинутый
#
#   Задача: создайте декоратор time_execution,
# который измеряет время выполнения функции.
# Декоратор должен выводить название функции,
# время её выполнения и результат вызова.


import time
def time_execution(func):
	def wrapper(arg, *args, **kwargs):
		start_time = time.perf_counter()
		result = func(arg, *args, **kwargs)
		end_time = time.perf_counter()
		execution_time = end_time - start_time
		print(f"""Название функции {func.__name__}, 
		Время выполнения функции {execution_time:.10f} секунды,
		Результат вызова {arg}""")
		return result
	return wrapper

@time_execution
def greed1(name:str)->str:
	print(f"Hello {name}")

#Вызов
# greed1("Oleg")
# greed1("Alex")
# greed1("Alena")
# greed1("Nikita")


#       Итоговый проект
#https://top-academy.site/kfhcyglwfqaiy0vntfvxb4oef9oqhsel/?clckid=ad5d84e7

#«Калькулятор финансов»


class FinanceCalculator():
	def __init__(self):
		self.___Balance = 0
		self.TransactionList = list()

	@classmethod
	def log_transactions(func):
		def wrapper(*args, **kwargs):
			print(f"Имя функции {func.__name__}")
			return func(*args, **kwargs)
		return wrapper

	@log_transactions
	def add_transaction(self, type, amount, category):
		pass

	def get_transactions(self):
		pass

	def get_balance(self):
		pass

	def save_data(self):
		pass

	def load_data(self):
		pass

	def run(self):
		pass
def main_menu():
	while True:
		print("Кнопки меню:")
		print("\t1. Добавление транзакции (доход или расход).")
		print("\t2. Показать баланс и транзакции")
		print("\t0. Сохранить и выйти")
		print("\n\n")
		try:
			UserInput = int(input("Номер операции: ").strip())
			match UserInput:
				case 0:
					print("exit")
					break
				case 1:
					pass
				case 2:
					pass
				case 3:
					pass
				case 4:
					pass
		except:
			print("Не верный ввод попробуйте снова")
			continue


if __name__ == "__main__":
	main_menu()











