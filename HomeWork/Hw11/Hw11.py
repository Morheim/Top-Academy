#   Задание 1
#       Реализуйте класс «Автомобиль».
#           Необходимо хранить
# в полях класса:
# название модели,
# год выпуска,
# производителя,
# объем двигателя,
# цвет машины, цену.
#           Реализуйте методы класса для
# ввода данных,
# вывода данных,
# реализуйте доступ к отдельным полям через методы класса.

class Car:
    def __init__(self,
                 ModelName = "ModelName",
                 YearOfManufacture = int(0),
                 Manufacturer = "Manufacturer",
                 EngineSize = float(0),
                 Color = "Color",
                 PriceOfTheCar = float(0)):

        self.ModelName = ModelName
        self.YearOfManufacture = YearOfManufacture
        self.Manufacturer = Manufacturer
        self.EngineSize = EngineSize
        self.Color = Color
        self.PriceOfTheCar = PriceOfTheCar


    def __str__(self):
        return f"""Информация об этом авто 
        название модели - {self.ModelName} 
        год выпуска - {self.YearOfManufacture} 
        производителя - {self.Manufacturer} 
        объем двигателя - {self.EngineSize} л.с. 
        цвет машины - {self.Color}
        цена - {self.PriceOfTheCar}
"""


    def SetModelName(self):
        self.ModelName = input("Введите название модели: ")

    def GetModelName(self):
        return self.ModelName


    def SetYearOfManufacture(self):
        current_year = 2026
        while True:
            try:
                user_input = input("Введите год выпуска автомобиля: ")
                year = int(user_input)

                if 1886 <= year <= current_year:
                    self.year_of_manufacture = year
                    break
                else:
                    print(f"Ошибка: Год выпуска должен быть в диапазоне от 1886 до {current_year}. Попробуйте снова.\n")

            except ValueError:
                print("Ошибка: Введены некорректные данные. Пожалуйста, введите целое число (например, 2020).\n")

    def GetYearOfManufacture(self):
        return self.YearOfManufacture


    def SetManufacturer(self):
        while True:
            user_input = input("Введите производителя: ").strip()

            if user_input:
                self.manufacturer = user_input
                break
            else:
                print("Ошибка: Название производителя не может быть пустым. Попробуйте снова.\n")



    def GetManufacturer(self):
        return self.Manufacturer


    def SetEngineSize(self):
        while True:
            try:
                user_input = input("Введите объем двигателя (например, 1.6 или 2.0): ")
                engine_size = float(user_input)

                if engine_size <= 0:
                    print("Ошибка: Объем двигателя должен быть больше нуля. Попробуйте снова.\n")
                    continue

                self.engine_size = engine_size
                break

            except ValueError:
                print("Ошибка: Введены некорректные данные. Пожалуйста, введите число (например, 1.6).\n")

    def GetEngineSize(self):
        return self.EngineSize


    def SetColor(self):
        while True:
            print("1.Белый")
            print("2.Черный")
            print("3.Серый")
            print("4.Красный")
            print("5.Оранжевый")
            print("6.Желтый")
            print("7.Зеленый")
            print("8.Синий")
            print("9.Фиолетовый")
            print("10.Коричневый")
            print("11.Розовый")

            colors = input("Выберете цвет машины: ")
            if colors.isdigit():
                match colors:
                    case "1":
                        colors = "Белый"
                    case "2":
                        colors = "Черный"
                    case "3":
                        colors = "Серый"
                    case "4":
                        colors = "Красный"
                    case "5":
                        colors = "Оранжевый"
                    case "6":
                        colors = "Желтый"
                    case "7":
                        colors = "Зеленый"
                    case "8":
                        colors = "Синий"
                    case "9":
                        colors = "Фиолетовый"
                    case "10":
                        colors = "Коричневый"
                    case "11":
                        colors = "Розовый"
                    case _:
                        print("Не верный ввод")
                        continue

                self.Color = colors
                break
            else:
                continue

    def GetColor(self):
        return self.Color


    def SetPriceOfTheCar(self):
        while True:
            try:
                user_input = input("Введите стоимость машины: ")
                price = float(user_input)

                if price < 0:
                    print("Ошибка: Стоимость не может быть отрицательной. Попробуйте снова.\n")
                    continue

                self.PriceOfTheCar = price
                break

            except ValueError:
                print("Ошибка: Введены некорректные данные (буквы или символы). Введите число.\n")

    def GetPriceOfTheCar(self):
        return self.PriceOfTheCar

# cars = Car()
# cars.SetModelName()
# cars.SetYearOfManufacture()
# cars.SetManufacturer()
# cars.SetEngineSize()
# cars.SetColor()
# cars.SetPriceOfTheCar()
#
# print(cars)


#___________________________________________________________________________________________________________________
#           Задание 2
#       Реализуйте класс «Книга».
#   Необходимо хранить в полях класса:
#   название книги,
#   год выпуска,
#   издателя,
#   жанр,
#   автора,
#   цену.
#
#       Реализуйте методы класса
#   для ввода данных,
#   вывода данных,
#   реализуйте доступ к отдельным
#   полям через методы класса.

class Book:
    def __init__(self, BookTitle = None, YearOfManufacture = None, Publisher = None, Genre = None, Author = None, Price = None):
        self.BookTitle = BookTitle
        self.YearOfManufacture = YearOfManufacture
        self.Publisher = Publisher
        self.Genre = Genre
        self.Author = Author
        self.Price = Price

    def __str__(self):
        return f"""Информация о книге
        Название книги - {self.BookTitle}
        Год выпуска - {self.YearOfManufacture}
        Издатель - {self.Publisher}
        Жанр - {self.Genre}
        Автор - {self.Author}
        Цена - {self.Price}
"""
    def SetBookTitle(self):
        while True:
            UserInput = input("Введите название книги ").strip()
            if UserInput != "":
                self.BookTitle = UserInput
                break
            else:
                print("Название книги не может быть пустым попробуйте снова")

    def GetBookTitle(self):
        return self.BookTitle


    def SetYearOfManufacture(self):
        while True:
            UserInput = input("Введите год выпуска книги ").strip()
            if UserInput != "":
                self.BookTitle = int(UserInput)
                break
            else:
                print("Год выпуска книги не может быть пустым")

    def GetYearOfManufacture(self):
        return self.YearOfManufacture



    def SetPublisher(self):
        while True:
            UserInput = input("Введите издателя книги ").strip()
            if UserInput != "" and not UserInput.isdigit():
                self.Publisher = UserInput
                break
            else:
                print("Издатель книги не может быть пустым попробуйте снова")

    def GetPublisher(self):
        return self.Publisher



    def SetGenre(self):
        while True:
            UserInput = input("Введите жанр книги ").strip()
            if UserInput != "" and not UserInput.isdigit():
                self.Genre = UserInput
                break
            else:
                print("Жанр не может быть пустым")

    def GetGenre(self):
        return self.Genre



    def SetAuthor(self):
        while True:
            UserInput = input("Введите автора книги ").strip()
            if UserInput != "" and not UserInput.isdigit():
                self.Author = UserInput
                break
            else:
                print("имя или псевдоним автора не может быть пустым попробуйте снова")

    def GetAuthor(self):
        return self.Author



    def SetPrice(self):
        while True:
            UserInput = input("Введите стоимость книги ").strip()
            if UserInput:
                UserInput = float(UserInput)
                if UserInput > 0.0:
                    self.Price = float(UserInput)
                    break
                else:
                    print("Стоимость должна быть больше 0")
            else:
                print("стоимость не может быть пустой или не из чисел")

    def GetPrice(self):
        return self.Price


# book = Book("Warcraft", "1 октября 2001", "АСТ", "Роман", "Кристи Голден")
# book.SetPrice()
# print(book)


#_________________________________________________________________________________________

#           Задание 3
#       Реализуйте класс «Стадион».
#
#   Необходимо хранить в полях класса:
# название стадиона,
# дату открытия,
# страну,
# город,
# вместимость.
#
#   Реализуйте методы класса для
# ввода данных,
# вывода данных,
#
# реализуйте доступ к отдельным полям через методы класса.


class Stadium:
    def __init__(self, StadiumName:str = None, OpeningDate:str = None, Country:str = None, City:str = None, Capacity:int = None):
        self.StadiumName = StadiumName
        self.OpeningDate = OpeningDate
        self.Country = Country
        self.City = City
        self.Capacity = Capacity

    def __str__(self):
        return f"""Информация об этом стадионе
        Название - {self.StadiumName}
        Дата открытия - {self.OpeningDate}
        Страну - {self.Country}
        Город - {self.City}
        Вместимость - {self.Capacity}
"""

    def SetStadiumName(self):
        while True:
            UserInput = input("Введите название стадиона ").strip().capitalize()
            if UserInput != "":
                self.StadiumName = UserInput
                break
            else:
                print("Поле не может быть пустым")

    def GetStadiumName(self):
        return self.self.StadiumName

    def SetOpeningDate(self):
        while True:
            UserInput = input("Введите дату открытия стадиона ").strip()
            if UserInput != "":
                self.OpeningDate = UserInput
                break
            else:
                print("Поле не может быть пустым")


    def GetOpeningDate(self):
        return self.self.OpeningDate

    def SetCountry(self):
        while True:
            UserInput = input("Введите страну где расположен стадион ").strip().capitalize()
            if UserInput != "":
                self.Country = UserInput
                break
            else:
                print("Поле не может быть пустым")

    def GetCountry(self):
        return self.self.Country


    def SetCity(self):
        while True:
            UserInput = input("Введите город в котором расположен этот стадион ").strip().capitalize()
            if UserInput != "":
                self.City = UserInput
                break
            else:
                print("Поле не может быть пустым")


    def GetCity(self):
        return self.self.City


    def SetCapacity(self):
        while True:
            UserInput = input("Введите сколько вмещает в себя стадион ").strip()
            if UserInput != "":
                if UserInput.isdigit():
                    UserInput = int(UserInput)
                    if UserInput > 0:
                        self.Capacity = UserInput
                        break
                    else:
                        print("Поле должно быть бельше 0")
                else:
                    print("Поле должно быть числом")
            else:
                print("Поле не может быть пустым")

    def GetCapacity(self):
        return self.self.Capacity


stadium = Stadium()
stadium.SetStadiumName()
stadium.SetOpeningDate()
stadium.SetCountry()
stadium.SetCity()
stadium.SetCapacity()
print(stadium)
