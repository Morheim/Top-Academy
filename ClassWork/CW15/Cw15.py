class Car:
	wheels = 4
	def __init__(self, brand, color):
		self.brand = brand
		self.color = color
	def drive(self):
		print(f"{self.brand} {self.color} едет")
	def info(cls):
		print(f"Все машины имеют {cls.wheels} колеса")

	@staticmethod
	def get_info():
		print("Машины - транспортное средство. ")


# car = Car("Toyota","white")
# car.drive()
# car.info()
# car.get_info()


class Library:
	total = 0
	def __init__(self, title, status = "Доступна"):
		self.title = title
		self.status = status
		Library.total += 1


	def dost_stat(self):
		return self.status

	@classmethod
	def get_total(cls):
		return f"Сейчас в библеотеке доступно {cls.total} книг"

	def izmen_status(self, new_status):
		self.status = new_status

# book1 = Library("Зелёная миля")
# book2 = Library("Тёмная башня")
# book3 = Library("Кэри")
#
# print(Library.get_total())
# book1.izmen_status("Взяли")
# print(book1.dost_stat())


class SystemManagement:
	Zakaz = {}
	@staticmethod
	def AddOrder(Number, Zakaz):
		if Number > 10:
			print()




