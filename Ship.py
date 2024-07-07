class Ship:
    def __init__(self, name, year, country):
        self.name = name
        self.year = year
        self.country = country

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Year: {self.year}")
        print(f"Country: {self.country}")
        print()

class Frigate(Ship):
    def __init__(self, name, year, country, _type):
        super().__init__(name, year, country)
        self._type = _type

    def display_info(self):
        super().display_info()
        print(f"Тип: {self._type}")
        print()

class Destroyer(Ship):
    def __init__(self, name, year, country, gun_type):
        super().__init__(name, year, country)
        self.gun_type = gun_type

    def display_info(self):
        super().display_info()
        print(f"Тип: {self.gun_type}")
        print()

class Cruiser(Ship):
    def __init__(self, name, year, country, project, water_type):
        super().__init__(name, year, country)
        self.project = project
        self.water_type = water_type

    def display_info(self):
        super().display_info()
        print(f"Проект: {self.project}")
        print(f"Водоизмещение: {self.water_type}")
        print()

# Пример использования
frigate = Frigate("Адмирал Горшков", 2000, "Россия", "Ферегат")
frigate.display_info()

destroyer = Destroyer("Адмирал Чабаненко", 1992, "Россия","Эсминец")
destroyer.display_info()

cruiser = Cruiser("Петр Великий", 1995, "СССР", "1144  ОРЛАН", 25860)
cruiser.display_info()