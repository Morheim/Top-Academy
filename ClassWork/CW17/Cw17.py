class Suhop:
	def __init__(self, Name):
		self.Name = Name
	def run(self):
		print(f"{self.Name} Бегает")


class Vodoplav:
	def __init__(self, Name):
		self.Name = Name

	def Swim(self):
		print(f"{self.Name} Плавает")


class Zemnovodnoe(Suhop, Vodoplav):
	def __init__(self, Name):
		self.Name = Name

# Lion = Suhop("Lion")
# Kosatka = Vodoplav("Kosatka")
# MorskayaCherepashka = Zemnovodnoe("Morskaya Cherepashka")
# Lion.run()
# Kosatka.Swim()
# MorskayaCherepashka.run()
# MorskayaCherepashka.Swim()



class LibraryItem:
	def __init__(self, Title):
		self.Title = Title

	def GetInfo(self):
		return self.Title



class Book(LibraryItem):
	def __init__(self, Title):
		super().__init__(Title)

	def GetInfo(self):
		return f"Книга {super().GetInfo()}"



class Journal(LibraryItem):
	def __init__(self, Title):
		super().__init__(Title)

	def GetInfo(self):
		return f"Журнал {super().GetInfo()}"



class Audiobook(LibraryItem):
	def __init__(self, Title, Duration):
		super().__init__(Title)
		self.Duration = Duration

	def GetInfo(self):
		return f"Аудиокнига: {super().GetInfo()} \nдлительность {self.Duration}"




book = Book("Warkraft")
print(book.GetInfo())

journal = Journal("Top Gear")
print(journal.GetInfo())

audiobook = Audiobook("Мастер и маргарита", "1:45")
print(audiobook.GetInfo())

#Задания
#https://top-academy.site/6f3fxfno9gthrmaegpbua3r7y8gbizwe/?clckid=79fd6722
#
# Уровень 1: Базовый
#
# Задача: создайте класс Employee, который:
#
# Имеет атрибуты name и position (имя и должность сотрудника).
# Имеет метод display_info, который выводит информацию о сотруднике в формате:
# «Сотрудник: {name}, Должность: {position}».

class Employee:
	def __init__(self, Name, Position):
		self.Name = Name
		self.Position = Position

	def GetParams(self):
		return {self.Name, self.Position}

	def DisplayInfo(self):
		return f"Сотрудник: {self.Name}, Должность: {self.Position}"

#
# Уровень 2: Средний
#
# Задача: создайте класс Team, который:
#
# Содержит атрибут team_members (список сотрудников).
#   Имеет метод add_member, который добавляет сотрудника в команду.
#   Имеет метод show_team, который выводит список всех сотрудников с их должностями.


class Team(Employee):
	def __init__(self, team_members):
		self.team_members = team_members

	def AddMember(self, emp):
		self.team_members.add(emp)

	def ShowTeam(cls):
		for emp in cls.team_members:
			print(f"{emp.DisplayInfo()}")

	def UpdatePosition(self, Name, NewPosition):
		if Name in self.team_members:
			self.team_members[Name] = NewPosition
		else:
			print(f"Сотрудник {Name} не найден")



Members = {Employee("Валера", "Программист"),
           Employee("Гена", "Продажник")}

team = Team(Members)
team.AddMember(Employee("Валерия", "Стажёр"))
team.ShowTeam()
print()
team.UpdatePosition("Валера", "Старший програмист")
team.ShowTeam()
















































