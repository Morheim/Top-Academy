#Декораторы

def apply_function(func, value):
	return func(value)

def square(x):
	return x * x

result = apply_function(square, 5)
print(result)


def decirator(func):
	def wrapper(name):
		print("До вызова функции")
		func(name)
		print("После вызова функции")
	return wrapper

@decirator
def greet(name):
	print(f"Привет, {name}!")

greet("Иван")


def decorator1(func):
	def wrapper():
		print("Декоратаор 1")
		func()
	return wrapper


def decorator2(func):
	def wrapper():
		print("Декоратаор 2")
		func()
	return wrapper

@decorator1
@decorator2
def say_hello():
	print("Привет!")

say_hello()


def authorize(func):
	def wrapper(user):
		if user == "admin":
			return func()
		else:
			print("Доступ запрещен")
	return wrapper

@authorize
def secret():
	print("Секретная информация!")

secret("admin")
secret("guest")


def log_action(func):
	def wrapper(username, *args, **kwargs):
		with open("action.log", "a", encoding = "utf-8") as log_file:
			log_file.write(f"пользователь: {username}, действие {func.__name__}\n")
		return func(username, *args, ** kwargs)
	return wrapper

@log_action
def login(username):
	print(f"{username} вошёл в систему.")

@log_action
def update_profile(username, profile_data):
	print(f"{username} обновил профиль с данными: {profile_data}.")

login("Alice")
update_profile("Alice", {"age": 25, "city": "Москва"})

