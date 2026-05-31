#https://storage.yandexcloud.net/top-academy-services-omni/materials/ei2ht-PYzaLWAt6D6EB67HuxEQmRrlr8.pdf?response-content-disposition=inline%3B%20filename%3D%22Python_PZ_Modul__10_Klassy_i_ob_ekty_1583241626.pdf%22&clckid=8c187bbd

"""Задание 1
Реализуйте класс «Человек». Необходимо хранить в
полях класса: ФИО, дату рождения, контактный телефон,
город, страну, домашний адрес. Реализуйте методы класса
для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса."""

class Human:
	def __init__(self, FIO = "", date = "", phone_number = "", city = "", country = "", home = ""):
		self.FIO = FIO
		self.date = date
		self.phone_number = phone_number
		self.city = city
		self.country = country
		self.home = home

	def set_name(self):
		self.FIO = input("Add name: ")

	def get_name(self):
		print(self.FIO)

	def set_date(self):
		self.date = input("Add date: ")

	def get_date(self):
		print(self.date)

	def set_phone_number(self):
		self.phone_number = input("Add phone_number: ")

	def get_phone_number(self):
		print(self.phone_number)

	def set_city(self):
		self.city = input("Add city: ")

	def get_city(self):
		print(self.city)

	def set_country(self):
		self.country = input("Add country: ")

	def get_country(self):
		print(self.country)

	def set_home(self):
		self.home = input("Add home: ")

	def get_home(self):
		print(self.home)


	def get_all_info(self):
		print(self.FIO)
		print(self.date)
		print(self.phone_number)
		print(self.city)
		print(self.country)
		print(self.home)

"""Задание 2
Создайте класс «Город». Необходимо хранить в полях класса:
 название города, название региона, название
страны, количество жителей в городе, почтовый индекс
города, телефонный код города. Реализуйте методыкласса
для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса."""

class City:
	def __init__(self,
	             name_city = "",
	             name_region = "",
	             name_сountry = "",
	             number_of_inhabitants_in_the_city = int(0),
	             postal_code = int(0),
	             telephone_area_code = int(0),):

		self.name_city = name_city
		self.name_region = name_region
		self.name_country = name_сountry
		self.number_of_inhabitants_in_the_city = number_of_inhabitants_in_the_city
		self.postal_code = postal_code
		self.telephone_area_code = telephone_area_code

	def get_all_info(self):
		print(f"Название города - {self.name_city}")
		print(f"Название региона - {self.name_region}")
		print(f"Название страны - {self.name_country}")
		print(f"Количество жителей - {self.number_of_inhabitants_in_the_city}")
		print(f"Почтовый индекс - {self.postal_code}")
		print(f"Телефонный код города - +{self.telephone_area_code}")
	def set_name_city(self):
		self.name_city = input("Введите название города: ")
	def get_name_city(self):
		print(f"Название города - {self.name_city}")


	def set_name_region(self):
		self.name_region = input("Введите название региона: ")
	def get_name_region(self):
		print(f"Название региона - {self.name_region}")


	def set_name_country(self):
		self.name_country = input("Введите название страны: ")
	def get_name_city(self):
		print(f"Название страны - {self.name_country}")


	def set_number_of_inhabitants_in_the_city(self):
		try:
			self.number_of_inhabitants_in_the_city = int(input("Введите количество жителей: "))
		except TypeError:
			print("Введено не верное значение попробуйте снова: ", end = "")
			self.number_of_inhabitants_in_the_city = int(input())
	def get_number_of_inhabitants_in_the_city(self):
		print(f"Количество жителей - {self.number_of_inhabitants_in_the_city}")


	def set_postal_code(self):
		try:
			self.postal_code = int(input("Введите почтовый индекс: "))
		except TypeError:
			print("Введено не верное значение попробуйте снова: ", end="")
			self.postal_code = int(input())
	def get_postal_code(self):
		print(f"Почтовый индекс - {self.postal_code}")


	def set_telephone_area_code(self):
		try:
			self.telephone_area_code = int(input("Введите телефонный код города: "))
		except TypeError:
			print("Введено не верное значение попробуйте снова: ", end="")
			self.telephone_area_code = int(input())
	def get_(self):
		print(f"Телефонный код города - +{self.telephone_area_code}")



#
# my_city = City()
# my_city.set_name_city()
# my_city.set_name_region()
# my_city.set_name_country()
# my_city.set_number_of_inhabitants_in_the_city()
# my_city.set_postal_code()
# my_city.set_telephone_area_code()
#
#
# my_city.get_name_city()
# print()
# my_city.get_all_info()


"""Задание 3
Создайте класс «Страна». Необходимо хранить в
полях класса: 
название страны, название континента
название континента,
количество жителей в стране,
телефонный код страны,
название столицы,
 название городов страны.
  Реализуйте
1
методы класса для ввода данных, вывода данных, реализуйте доступ к
 отдельным полям через методы класса."""

class Country:
	def __init__(self,
	             name_country = "",
	             name_of_the_continent = "",
	             number_of_inhabitants = int(0),
	             telephone_country_code = int(0),
	             name_of_the_capital = "",
	             names_of_cities_in_the_country = list()):

		self.name_country = name_country
		self.name_of_the_continent = name_of_the_continent
		self.number_of_inhabitants = number_of_inhabitants
		self.telephone_country_code = telephone_country_code
		self.name_of_the_capital = name_of_the_capital
		self.names_of_cities_in_the_country = names_of_cities_in_the_country

	def set_name_country(self):
		self.name_country = input("Введите название страны")
	def get_name_country(self):
		return self.name_country


	def set_name_of_the_continent(self):
		self.name_of_the_continent = input("Введите название континента")
	def get_name_of_the_continent(self):
		return self.name_of_the_continent


	def set_number_of_inhabitants(self):
		self.number_of_inhabitants = input("Введите ")
	def get_number_of_inhabitants(self):
		return self.number_of_inhabitants


	def set_(self):
		self. = input("Введите ")

	def get_(self):
		return self.






















