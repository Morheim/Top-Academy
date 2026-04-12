#https://top-academy.site/od4cup7goucuuxgu80rceyicrczz324i/?clckid=8e87cd37

def cw1():
    # Создаем пустой список для хранения транзакций
    transactions = []

    # Запрашиваем у пользователя количество транзакций
    number_of_transactions = int(input("Введите количество транзакций, которое вы хотите добавить: "))

    # Ввод данных о каждой транзакции
    for _ in range(number_of_transactions):
        amount = input("Введите сумму транзакции: ")
        description = input("Введите описание транзакции: ")
        # Формируем строку транзакции и добавляем в список
        transaction = f"Сумма: {amount}, Описание: {description}"
        transactions.append(transaction)

    # Выводим список всех транзакций
    print("\nСписок всех ваших транзакций:")
    for transaction in transactions:
        print(transaction)

        
def cw2():
    # Создаем пустой список для хранения информации о расходах на питание
    meal_expenses = []

    # Запрашиваем у пользователя количество дней для учета
    days_count = int(input("На сколько дней вы хотите ввести расходы на питание? "))

    # Ввод данных о расходах на каждый день
    for i in range(1, days_count + 1):
        cost = input(f"Введите стоимость приёма пищи за день {i}: ")
        meal = input("Введите описание приёма пищи: ")
        expense = f"День {i}: Стоимость - {cost}, Приём пищи - {meal}"
        meal_expenses.append(expense)

    # Вывод информации о расходах
    print("\nВаш список расходов на питание:")
    for expense in meal_expenses:
        print(expense)

#https://top-academy.site/lmcbgryccihnnjm0jxmap5uz2kfy08pn/?clckid=7c4bca7d
films = []
films.append("дюна")
films.append("1+1")
films.append("World Of Warcraft")


def PCW1():
    print(films)

    print("Список фильмов")
    for film in films:
        print(film)

    for i in range(len(films)):
        print(f"фильм №{i+1}: [{films[i]}]")
    

def PCW2():
    while True:
        print("1. Добавить фильм в список")
        print("2. удалить элеменит из списка")
        print("0. Выход")
        choice = input("Введите пункт меню: ").strip()[0]
        match choice:
            case "0":
                print("0. Выход")
            case "1":
                film = input("Введите название фильма: ").strip()
                if film not in films:
                    films.append(film)
                else:
                    print("Фильм с таким названием уже есть в списке")
                print(f"Список фильмов: {films}")
                
            case "2":
                film = input("Введите название фильма: ").strip()
                if film in films:
                    films.remove(film)
                else:
                    print("Не найден фильм с таким названием")
                print(f"Список фильмов: {films}")
            case _:
                print("Не коректный ввод попробуйте ещё")

rates = []
avg = 0

def PCW3():
    while True:
        print("1. Добавить оценку в список")
        print("0. Результаты и выход")
        
        choice = input("Введите пункт меню: ").strip()[0]
        
        match choice:
            case "0":
                print("0. Окончание работы программы")
                if len(rates) > 0:
                    avg = sum(rates)/len(rates)
                print(f"Все оценки: {rates}")
                print(f"Средняя оценка: {avg}")
                print("Оценки выше средней: ", end = "")
                for rate in rates:
                    if rate > avg:
                        print(f"{rate}", end = ", ")
                break
            
            case "1":
                rate = float(input("Введите оценку").strip())
                while rate < 0 or rate > 5:
                    rate = float(input("Введите оценку").strip())
                rates.append(rate)
            case _:
                print("Некоректный ввод")


                    
                
















