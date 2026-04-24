name = input("Введите ваше мия: ").strip().capitalize()
Surname = input("Введите вашу Фамилию: ").strip().capitalize()
Text = input("Введите текст основного сообщения.")

print(f"""
Уважаемый {name} {Surname},
{Text}
С уважением, {name} {Surname}
""")
