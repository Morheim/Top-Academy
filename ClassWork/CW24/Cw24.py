#бстрактные классы
#https://top-academy.site/dd2v6cymtda28f201f6yd6rmybaephcg/?clckid=5e7f1a54


from abc import ABC, abstractmethod


class DataManager(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass


class FileDataManager(DataManager):
    def save(self, data):
        with open('data.txt', 'w') as file:
            file.write(data)

    def load(self):
        with open('data.txt', 'r') as file:
            return file.read()

class DatabaseDataManager(DataManager):
    def __init__(self):
        self.data = None

    def save(self, data):
        self.data = data

    def load(self):
        return self.data

file_manager = FileDataManager()
file_manager.save("Пример данных в файле")
print(file_manager.load())  # Пример данных в файле

db_manager = DatabaseDataManager()
db_manager.save("Пример данных в базе данных")
print(db_manager.load())  # Пример данных в базе данных

print("\n\n\nзадание 1\n\n\n")

class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Transport):
    def start_engine(self):
        print("Двигатель машины запущен")

    def stop_engine(self):
        print("Двигатель машины выключен")

class Bicycle(Transport):
    def start_engine(self):
        print("Двигателя нет, крутите педали")

    def stop_engine(self):
        print("Двигателя нет, педали перестали крутить")


#асинхронной программирование

