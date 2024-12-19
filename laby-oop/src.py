from abc import ABC, abstractmethod
import uuid
import pygame
import time

pygame.mixer.init()

class Animal(ABC):
    def __init__(self, name, age, weight):
        self._id = uuid.uuid4()
        self._name = name
        self._age = age
        self._weight = weight
        self._food_needs = 0  

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_weight(self):
        return self._weight

    def get_food_needs(self):
        return self._food_needs

    @abstractmethod
    def make_sound(self):
        pass

    def calculate_food(self): 
        self._food_needs = self._weight * 0.1 


class Lion(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.hunt_skill = "Excellent"

    def make_sound(self):
        try:
            pygame.mixer.music.load("ryk.mp3")
            pygame.mixer.music.play()
            time.sleep(3)  # Ждем, пока звук проиграется
        except pygame.error as e:
            print(f"Ошибка при загрузке или воспроизведении музыки: {e}")
        return "Roar!"

    def hunt(self):
        return "Lion is hunting!"

    def calculate_food(self):
        self._food_needs = self._weight * 0.15 


class Elephant(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trunk_size = "Large"

    def make_sound(self):
        try:
            pygame.mixer.music.load("trumpet.mp3")
            pygame.mixer.music.play()
            time.sleep(5)
        except pygame.error as e:
            print(f"Ошибка при загрузке или воспроизведении музыки: {e}")
        return "Trumpet!"

    def calculate_food(self):
        self._food_needs = self._weight * 0.2 


class Parrot(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.wingspan = 0.5

    def make_sound(self):
        try:
            pygame.mixer.music.load("squawk.mp3")
            pygame.mixer.music.play()
            time.sleep(2)
        except pygame.error as e:
            print(f"Ошибка при загрузке или воспроизведении музыки: {e}")
        return "Squawk!"

    def fly(self):
        return "Parrot is flying!"


# class Penguin(Animal):
#     def __init__(self, name, age, weight):
#         super().__init__(name, age, weight)
#         self.swimming_skill = "Expert"

#     def make_sound(self):
#         try:
#             pygame.mixer.music.load("honk.mp3")
#             pygame.mixer.music.play()
#             time.sleep(2)
#         except pygame.error as e:
#             print(f"Ошибка при загрузке или воспроизведении музыки: {e}")
#         return "Honk!"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def display_animals(self):
        for animal in self.animals:
            print(f"ID: {animal._id}, Name: {animal.get_name()}, Age: {animal.get_age()}, Weight: {animal.get_weight()}, Food Needs: {animal.get_food_needs()}")

    def feed_all(self):
        total_food = 0
        for animal in self.animals:
            animal.calculate_food() 
            total_food += animal.get_food_needs()
        print(f"Total food needed for all animals: {total_food}")


    def make_all_sounds(self):
        for animal in self.animals:
            print(f"{animal.get_name()}: {animal.make_sound()}")


    def generate_report(self):
        report = "Zoo Report:\n"
        report += f"Total animals: {len(self.animals)}\n"
        for animal in self.animals:
            report += f"ID: {animal._id}, Name: {animal.get_name()}, Species: {type(animal).__name__}, Age: {animal.get_age()}, Weight: {animal.get_weight()}, Food Needs: {animal.get_food_needs()}\n"
        report += f"Total food needed: {sum([animal.get_food_needs() for animal in self.animals])}\n"
        return report


# Пример использования
zoo = Zoo()
lion = Lion("Leo", 5, 200)
elephant = Elephant("Ellie", 10, 5000)
parrot = Parrot("Polly", 2, 0.2)


zoo.add_animal(lion)
zoo.add_animal(elephant)
zoo.add_animal(parrot)


zoo.display_animals()
zoo.make_all_sounds()
zoo.feed_all()
print(zoo.generate_report())
