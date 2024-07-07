





class Device:
    def __init__(self, name, firma):
        self.name = name
        self.firma = firma

    def introduce(self):
        print(f"Model: {self.name} Firma:{self.firma} ")

class CoffeeMashine(Device):
    def __init__(self, name, firma, drinks):
        super().__init__(name, firma)
        self.drinks = drinks

    def introduce(self):
        super().introduce()
        print(f"CoffeeMashine умеет готовить {self.drinks} ")

class Blender(Device):
    def __init__(self, name, firma, speed):
        super().__init__(name, firma)
        self.speed = speed

    def introduce(self):
        super().introduce()
        print(f"Blender скорость {self.speed}")

class MeatGrinder(Device):
    def __init__(self, name, firma, time, power):
        super().__init__(name, firma)
        self.time = time
        self.power = power

    def introduce(self):
        super().introduce()
        print(f"MeatGrinder время неарерывной работы {self.time}, мощность  {self.power} ")

coffeeMashine = CoffeeMashine("H4555", "Gorenie", "Капучино, Латте, Мокко")
blender = Blender("Creen65t", "Mr. Craft", "1000 оборотов в минуту")
meatGrinder = MeatGrinder("NLO 2.0", "Garlin", "20 minuts", "2500Вт")

coffeeMashine.introduce()
blender.introduce()
meatGrinder.introduce()