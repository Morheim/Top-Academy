#Python. Урок №14. Magic-методы.
#https://top-academy.site/kmhyuhyh2q0pslrz0scgncgbqulflvgw/?clckid=8a738d7a


#Список магических методов
#https://pyplanet.ru/article/all-magic-methods.html?clckid=3bac8bda


#Практические задачи
#https://top-academy.site/pbhywzxd9yzygresqdfqbvrclfnt04u2/?clckid=0ea9cd62

# 	Уровень 1: Базовый
#
# Задача: создайте класс Rectangle для работы с прямоугольниками.
# В классе должны быть:

# 1. Атрибуты length и width, задаваемые при создании объекта.
# 2. Метод _str_, который возвращает строку вида
#       «Прямоугольник: длина={length}, ширина={width}».
# 3. Метод area, который вычисляет площадь прямоугольника.
# 4. Метод perimeter, который вычисляет периметр прямоугольника.

class Rectangle:
	def __init__(self, length = float(0), width = float(0)):
		self.length = length
		self.width = width

	def set_length(self):
		try:
			self.length = float(input("Введите length: "))
		except TypeError:
			self.length = float(input("введено не верное значение нужно целочисленное: "))

	def get_length(self):
		return self.length

	def set_width(self):
		try:
			self.width = float(input("Введите width: "))
		except TypeError:
			self.width = float(input("введено не верное значение нужно целочисленное: "))

	def get_width(self):
		return self.width

	def __str__(self):
		return f"Прямоугольник: \nдлина = {self.length} \nширина = {self.width}"

	def area(self):
		return self.length * self.width

	def perimeter(self):
		return 2 * (self.length + self.width)



# rectangle_obj = Rectangle()
# rectangle_obj.set_length()
# rectangle_obj.set_width()
# print(rectangle_obj.area())
# print(rectangle_obj.perimeter())

# Уровень 2: Средний
#
# Задача: создайте класс BankAccount для работы с банковскими счетами.
# В классе должны быть:

# *  Атрибут balance, задающий начальный баланс (по умолчанию равен 0).
# *  Метод _str_, который возвращает строку вида «Баланс: {balance}».
# *  Метод deposit, который добавляет деньги на счёт.
# *  Метод withdraw, который снимает деньги со счёта
#   (если хватает средств, иначе выводится сообщение об ошибке).

class BankAccount:
	def __init__(self, balance = float(0)):
		self.balance = balance

	def set_balance(self):
		try:
			balance = float(input("Введите balance: "))
		except TypeError:
			balance = float(input("не верный тип введите balance целочисленное число: "))

	def get_balance(self):
		return self.balance

	def __str__(self):
		return f"Баланс: {self.balance}"

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
		else:
			print("Недостаточно средств")


class Time:
	def __init__(self, hours, minuts, seconds):
		self.hours = hours
		self.minuts = minuts
		self.seconds = seconds

	def __str__(self):
		return f"{self.hours}:{self.minuts:02d}:{self.seconds:02d}"

	def __eq__(self, other):
		return self.hours == other.hours and \
			self.minuts == other.minuts and \
			self.seconds == other.seconds

	def add_time(self,seconds):
		self.seconds += seconds
		if self.seconds >= 60:
			new_min = self.seconds // 60
			self.minuts += new_min
			self.seconds -= new_min * 60

		if self.minuts >= 60:
			new_min = self.minuts // 60
			self.hours += new_min
			self.minuts -= new_min * 60

#доп практика
#https://storage.yandexcloud.net/top-academy-services-omni/materials/V0YdEDgwiBCu09MqxLHO68huTS76UHZo.pdf?response-content-disposition=inline%3B%20filename%3D%22Python_PZ_Modul__10_Peregruzka_operatorov_c_5_1584698959.pdf%22&clckid=e0ba34ff

# Задание 2
# Создайте класс Дробь (или используйте уже ранее
# созданный вами). Используя перегрузку операторов реализуйте для него арифметические операции для работы
# с дробями (операции +, -, *, /).

class Fraction:
	def __init__(self, a,b):
		if b == 0:
			raise ValueError("Знаминатель не может быть 0")
		self.chisl = a
		self.znam = b

	def __str__(self):
		return f"{self.chisl} / {self.znam}"

	def __add__(self, other):
		new_chisl = self.chisl * other.znam + other.chisl * self.znam
		new_znam = self.znam * other.znam
		return Fraction(new_chisl, new_znam)

	def __sub__(self, other):
		new_chisl = self.chisl * other.znam - other.chisl * self.znam
		new_znam = self.znam * other.znam
		return Fraction(new_chisl, new_znam)

	def __mul__(self, other):
		new_chisl = self.chisl * other.chisl
		new_znam = self.znam * other.znam
		return Fraction(new_chisl, new_znam)

	def __truediv__(self, other):
		new_chisl = self.chisl * other.znam
		new_znam = self.znam * other.chisl
		return Fraction(new_chisl, new_znam)

try:
	f1 = Fraction(2, 5)
	print(f1)
	f2 = Fraction(3, 4)
	print(f2)
	print(f1+f2)
	print(f1-f2)
	print(f1*f2)
	print(f1/f2)
except ValueError as e:
	print(f"{e}")
except Exception as e:
	print(f"Неизвестная ошибка: {e}")








