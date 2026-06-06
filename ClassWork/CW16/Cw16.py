# # пример наследования
# class Animal:
# 	def __init__(self, Name):
# 		self.Name = Name
#
# 	def speak(self):
# 		return "Я животное"
#
# class Dog(Animal):
# 	def speak(self):
# 		return "Гав-гав!"
#
# class Cat(Animal):
# 	def speak(self):
# 		return "Мяу-мяу!"
#
#
# slon = Animal("Манфред")
# print(slon.Name)
# print(slon.speak())
#
# dog = Dog("Шарик")
# print(dog.Name)
# print(dog.speak())
#
# cat = Cat("Мурзик")
# print(cat.Name)
# print(cat.speak())
#
#
# #пример инкапсуляции
# class BankAccount:
# 	def __init__(self, Owner, Balance):
# 		self.Owner = Owner
# 		self._AccountNumber = "12345"
# 		self.__Balance = Balance
#
# 	def GetBalance(self):
# 		return self.__Balance
#
# 	def Deposit(self, Amount):
# 		if Amount > 0:
# 			self.__Balance += Amount
# 		return self.__Balance
#
#
# #Пример использования
# Account = BankAccount("Алиса", 1000)
# print(Account.Owner)
# print(Account.GetBalance())
# Account.Deposit(500)
# print(Account.GetBalance())
#
#
# #Пример полеморфизма
# from abc import ABC, abstractmethod
# class Shape(ABC):
# 	@abstractmethod
# 	def GetArea(self):
# 		pass
#
# class Circle(Shape):
# 	def __init__(self, radius):
# 		self.radius = radius
#
# 	def GetArea(self):
# 		return 3.14 * self.radius ** 2
#
#
# class Rectangle(Shape):
# 	def __init__(self, width, height):
# 		self.width = width
# 		self.height = height
#
# 	def GetArea(self):
# 		return self.width * self.height
#
#
# #Пример использования
# circle = Circle(5)
# rectangle = Rectangle(4,6)
#
# print(circle.GetArea())
# print(rectangle.GetArea())
#
#
#
#
#
#
#
#

class Employee:
	def __init__(self, FirstName = None, LastName = None, Salary = None):
		self.__FirstName = FirstName
		self.__LastName = LastName
		self.__Salary = Salary

	def GetInfo(self):
		return f"""Имя - {self.__FirstName}
Фамилия - {self.__LastName}
З.П. - {self.__Salary} 
"""

	def GetSalary(self):
		return self.__Salary

	def AddSalary(self, Amount):
		if Amount > 0:
			self.__Salary += Amount
		return self.__Salary


class Manager(Employee):
	def __init__(self, FirstName, LastName, Salary, Bonus = 0):
		super().__init__(FirstName, LastName, Salary)
		if Bonus >= 0:
			self.Bonus = Bonus
		else:
			self.Bonus = 0

	def AddBonus(self, Bonus):
		if Bonus > 0:
			return int(self.__Salary + self.Bonus)


class Intern(Employee):
	def __init__(self, FirstName = None, LastName = None, Salary = None, DiscRate = 0):
		super().__init__(FirstName, LastName, Salary)
		if DiscRate >= 0:
			self.DiscRate = DiscRate
		else:
			self.DiscRate = 0

	def GetSalary(self):
		return int(super().GetSalary() * self.DiscRate)

employees = [
Employee("Ivan", "Ivanov", 40000),
Manager("Egor", "Egorov", 50000, 20000),
Intern("Kolya", "Kolyaev", 40000, 0.5)
]
for emp in employees:
	print(f"{emp.GetInfo()} Zarplata {emp.GetSalary()}")

















