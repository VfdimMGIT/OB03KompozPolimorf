import json  # Импортируем модуль json для работы с JSON-файлами

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age    # Возраст животного

    def make_sound(self):
        raise NotImplementedError("Subclasses should implement this method")  # Метод должен быть переопределен в подклассах

    def eat(self):
        print(f"{self.name} is eating.")  # Метод для имитации приема пищи

# Подкласс Bird (наследуется от Animal)
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)  # Вызов конструктора родительского класса
        self.wingspan = wingspan    # Уникальный атрибут для птиц: размах крыльев

    def make_sound(self):
        print(f"{self.name} says: Chirp!")  # Переопределение метода make_sound для птиц

# Подкласс Mammal (наследуется от Animal)
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)  # Вызов конструктора родительского класса
        self.fur_color = fur_color  # Уникальный атрибут для млекопитающих: цвет шерсти

    def make_sound(self):
        print(f"{self.name} says: Roar!")  # Переопределение метода make_sound для млекопитающих

# Подкласс Reptile (наследуется от Animal)
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)  # Вызов конструктора родительского класса
        self.scale_type = scale_type  # Уникальный атрибут для рептилий: тип чешуи

    def make_sound(self):
        print(f"{self.name} says: Hiss!")  # Переопределение метода make_sound для рептилий

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()  # Вызов метода make_sound для каждого животного

# Класс для сотрудника ZooKeeper
class ZooKeeper:
    def __init__(self, name):
        self.name = name  # Имя сотрудника

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")  # Метод для кормления животного

# Класс для сотрудника Veterinarian
class Veterinarian:
    def __init__(self, name):
        self.name = name  # Имя сотрудника

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")  # Метод для лечения животного

# Класс Zoo для управления зоопарком
class Zoo:
    def __init__(self):
        self.animals = []  # Список животных в зоопарке
        self.staff = []    # Список сотрудников в зоопарке

    def add_animal(self, animal):
        self.animals.append(animal)  # Добавление животного в зоопарк
        print(f"{animal.name} has been added to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)  # Добавление сотрудника в зоопарк
        print(f"{staff_member.name} has been added to the zoo staff.")

    def list_animals(self):
        print("Animals in the zoo:")  # Вывод списка животных
        for animal in self.animals:
            print(f"- {animal.name} ({animal.__class__.__name__})")

    def list_staff(self):
        print("Staff in the zoo:")  # Вывод списка сотрудников
        for staff in self.staff:
            print(f"- {staff.name} ({staff.__class__.__name__})")

    def save_to_file(self, filename):
        # Сериализация данных о животных и сотрудниках в JSON
        data = {
            "animals": [{"type": animal.__class__.__name__, "name": animal.name, "age": animal.age, **vars(animal)} for animal in self.animals],
            "staff": [{"type": staff.__class__.__name__, "name": staff.name, **vars(staff)} for staff in self.staff]
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)  # Запись данных в файл
        print(f"Zoo data saved to {filename}.")

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)  # Загрузка данных из файла

        self.animals = []  # Очистка текущего списка животных
        self.staff = []    # Очистка текущего списка сотрудников

        # Восстановление животных из данных
        for animal_data in data["animals"]:
            animal_type = animal_data.pop("type")  # Определение типа животного
            if animal_type == "Bird":
                self.animals.append(Bird(**animal_data))  # Создание объекта Bird
            elif animal_type == "Mammal":
                self.animals.append(Mammal(**animal_data))  # Создание объекта Mammal
            elif animal_type == "Reptile":
                self.animals.append(Reptile(**animal_data))  # Создание объекта Reptile

        # Восстановление сотрудников из данных
        for staff_data in data["staff"]:
            staff_type = staff_data.pop("type")  # Определение типа сотрудника
            if staff_type == "ZooKeeper":
                self.staff.append(ZooKeeper(**staff_data))  # Создание объекта ZooKeeper
            elif staff_type == "Veterinarian":
                self.staff.append(Veterinarian(**staff_data))  # Создание объекта Veterinarian

        print(f"Zoo data loaded from {filename}.")

# Основной блок программы
if __name__ == "__main__":
    # Создаем животных
    parrot = Bird("Polly", 5, 15)  # Птица
    lion = Mammal("Simba", 10, "Golden")  # Млекопитающее
    snake = Reptile("Kaa", 8, "Smooth")  # Рептилия

    # Создаем сотрудников
    keeper = ZooKeeper("John")  # Сотрудник ZooKeeper
    vet = Veterinarian("Dr. Smith")  # Сотрудник Veterinarian

    # Создаем зоопарк и добавляем животных и сотрудников
    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Сохраняем состояние зоопарка в файл
    zoo.save_to_file("zoo_data.json")

    # Создаем новый зоопарк и загружаем данные из файла
    new_zoo = Zoo()
    new_zoo.load_from_file("zoo_data.json")

    # Демонстрируем полиморфизм: вызываем make_sound для всех животных
    animal_sound(new_zoo.animals)

    # Демонстрируем методы сотрудников
    new_zoo.staff[0].feed_animal(new_zoo.animals[1])  # ZooKeeper кормит льва
    new_zoo.staff[1].heal_animal(new_zoo.animals[2])  # Veterinarian лечит змею

    # Выводим списки животных и сотрудников
    new_zoo.list_animals()
    new_zoo.list_staff()