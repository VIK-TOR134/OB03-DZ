#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`,
# `eat()`) для всех животных.
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические
# атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод
# `make_sound()` для каждого животного.
#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы
# для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например,
# `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} is chirping.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} is roaring.")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} is hissing.")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Added {staff_member.name} to the staff.")

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

# Пример использования
bird = Bird("Parrot", 2, "25cm")
mammal = Mammal("Lion", 5, "Golden")
reptile = Reptile("Snake", 3, "Smooth")

zoo_keeper = ZooKeeper("John")
veterinarian = Veterinarian("Dr. Smith")

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_staff(zoo_keeper)
zoo.add_staff(veterinarian)

zoo_keeper.feed_animal(bird)
veterinarian.heal_animal(mammal)  # Исправлено здесь

# Демонстрация полиморфизма
animals = [bird, mammal, reptile]
animal_sound(animals)
