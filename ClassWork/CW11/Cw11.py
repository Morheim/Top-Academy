"""
r - это чтение файла (если нет - ошибка)
w - Запись в файл с удалением предидущей информацией (если нет - создаёт новый)
a - запись в конец файла
"""

# file = open("file.txt", "r", encoding="utf-8")
# a = file.read()
# print(a)
# file.close()

# Обработка ошибок
# try:
# 	with open("file.txt", "r", encoding="utf-8") as file:
# 		content = file.read()
# 		print(content)
# except FileNotFoundError:
# 	print("Файл не найден. ")
# except IOError:
# 	print("Ошибка ввода-вывода. ")


# contacts = {"Иван": "123-456", "Мария": "789-012"}
#
# #сохранение контактов в файл
# with open("contacts.txt", "w", encoding="utf-8") as file:
# 	for name, phone in contacts.items():
# 		file.write(f"{name}: {phone}\n")


# #Чтение контактов из файла
# try:
# 	with open("contacts.txt", "r", encoding="utf-8") as file:
# 		for line in file:
# 			print(line.strip())
# except FileNotFoundError:
# 	print("Файл с контактами не найден. ")



# with open("image.jpg", "rd") as file:
# 	data = file.read()
# 	print(f"Прочитано {len(data)} байт.")

