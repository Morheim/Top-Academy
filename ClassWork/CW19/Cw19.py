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


import os


def log_transactions(func):
	def wrapper(self, *args, **kwargs):
		res = func(self, *args, **kwargs)
		print(f"Лог: {func.__name__} вызвана с аргументами {args} и результатом {res}")
		return res

	return wrapper

class FinanceManager:
	def __init__(self):
		self.balance = 0.0
		self.transactions = []
		self.filename = "transactions.txt"

	def load_data(self):
		if not os.path.exists(self.filename):
			return print("Файл данных не найден. Начинаем с пустого баланса.")

		with open(self.filename, 'r', encoding='utf-8') as f:
			lines = f.read().splitlines()

		if lines:
			self.balance = float(lines[0].split(':')[1])
			self.transactions = [{'type': t, 'amount': float(a), 'category': c}
								 for t, a, c in (line.split(',') for line in lines[1:] if line)]
		print("Данные успешно загружены из файла.")

	@log_transactions
	def add_transaction(self, t_type, amount, category):
		if t_type not in ('доход', 'расход'):
			return print("Ошибка: Неверный тип операции.")
		if amount <= 0:
			return print("Ошибка: Сумма должна быть положительным числом.")
		if t_type == 'расход' and amount > self.balance:
			return print("Ошибка: Недостаточно средств на балансе.")

		self.balance += amount if t_type == 'доход' else -amount
		self.transactions.append({'type': t_type, 'amount': amount, 'category': category})
		print(f"Транзакция добавлена: {self.transactions[-1]}")
		return True

	def get_transactions(self):
		return self.transactions

	def get_balance(self):
		return self.balance

	def save_data(self):
		with open(self.filename, 'w', encoding='utf-8') as f:
			f.write(f"balance:{self.balance}\n")
			f.writelines(f"{t['type']},{t['amount']},{t['category']}\n" for t in self.transactions)

	def run(self):
		while True:
			print("\nМеню:\n1. Добавить доход/расход\n2. Показать баланс и транзакции\n3. Сохранить и выйти")
			choice = input("Выберите действие: ").strip()

			match choice:
				case '1':
					try:
						self.add_transaction(
							input("Введите тип (доход/расход): ").strip().lower(),
							float(input("Введите сумму: ")),
							input("Введите категорию: ").strip()
						)
					except ValueError:
						print("Ошибка: Сумма должна быть числом.")

				case '2':
					print(f"Текущий баланс: {self.balance}\nСписок транзакций:")
					if self.transactions:
						for t in self.transactions:
							print(t)
					else:
						print("Транзакции отсутствуют.")

				case '3':
					self.save_data()
					print("Данные успешно сохранены в файл.\nПрограмма завершена.")
					break

				case _:
					print("Ошибка: Неверный ввод команды.")


if __name__ == "__main__":
	app = FinanceManager()
	app.load_data()
	app.run()











