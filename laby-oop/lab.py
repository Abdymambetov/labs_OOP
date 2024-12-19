from abc import ABC, abstractmethod



class Animal(ABC):
    def __init__(self, name, age, weight):
        self._name = name  
        self._age = age    
        self._weight = weight  

    @abstractmethod
    def make_sound(self):
        """Абстрактный метод, который должен быть переопределен в каждом подклассе."""
        pass

    @abstractmethod
    def calculate_food(self):
        """Метод расчета необходимого количества корма."""
        pass

    def get_info(self):
        """Возвращает информацию о животном."""
        return {
            "Name": self._name,
            "Age": self._age,
            "Weight": self._weight,
        }


# Подклассы для разных типов животных
class Lion(Animal):
    def make_sound(self):
        return "Roar!"

    def calculate_food(self):
        return self._weight * 0.05  # 5% от веса

    def hunt(self):
        return f"{self._name} is hunting."


class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"

    def calculate_food(self):
        return self._weight * 0.1  # 10% от веса


class Parrot(Animal):
    def make_sound(self):
        return "Squawk!"

    def calculate_food(self):
        return self._weight * 0.02  # 2% от веса

    def fly(self):
        return f"{self._name} is flying."


class Penguin(Animal):
    def make_sound(self):
        return "Honk!"

    def calculate_food(self):
        return self._weight * 0.03  # 3% от веса



class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        """Добавляет животное в зоопарк."""
        self.animals.append(animal)
        print(f"{animal._name} has been added to the zoo.")

    def remove_animal(self, name):
        """Удаляет животное по имени."""
        self.animals = [animal for animal in self.animals if animal._name != name]
        print(f"{name} has been removed from the zoo.")

    def list_animals(self):
        """Выводит информацию о всех животных."""
        print("\nAnimals in the zoo:")
        for animal in self.animals:
            print(animal.get_info())

    def feed_all(self):
        """Кормит всех животных и выводит общий расход корма."""
        total_food = 0
        print("\nFeeding all animals:")
        for animal in self.animals:
            food_needed = animal.calculate_food()
            total_food += food_needed
            print(f"{animal._name} needs {food_needed:.2f} kg of food.")
        print(f"Total food needed: {total_food:.2f} kg")

    def make_all_sounds(self):
        """Заставляет всех животных издать звуки."""
        print("\nAnimal sounds:")
        for animal in self.animals:
            print(f"{animal._name} says: {animal.make_sound()}")

    def generate_report(self):
        """Генерирует отчет о животных и корме."""
        report = {"Animals": [], "Total Food Needed": 0}
        for animal in self.animals:
            animal_info = animal.get_info()
            food_needed = animal.calculate_food()
            report["Animals"].append({**animal_info, "Food Needed": f"{food_needed:.2f} kg"})
            report["Total Food Needed"] += food_needed

        print("\nZoo Report:")
        for animal in report["Animals"]:
            print(animal)
        print(f"Total Food Needed: {report['Total Food Needed']:.2f} kg")


# Пример использования
if __name__ == "__main__":
    zoo = Zoo()

    # Добавление животных
    zoo.add_animal(Lion(name="Simba", age=5, weight=190))
    zoo.add_animal(Elephant(name="Dumbo", age=10, weight=1200))
    zoo.add_animal(Parrot(name="Polly", age=2, weight=1.5))
    zoo.add_animal(Penguin(name="Pingu", age=4, weight=30))

    # Вывод информации о всех животных
    zoo.list_animals()

    # Кормление всех животных
    zoo.feed_all()

    # Воспроизведение звуков всех животных
    zoo.make_all_sounds()

    # Генерация отчета
    zoo.generate_report()
