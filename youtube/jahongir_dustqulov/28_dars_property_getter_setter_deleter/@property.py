class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.petrol = 1

    def get_info(self):
        print(f"Name: {self.name}\nColor: {self.color}")

    def set_color(self, color):
        self.color = color

    def set_petrol(self, petrol):
        self.petrol = petrol

    @property
    def rasxod(self):
        return 100 / self.petrol


nexia = Car("Nexia", "grey")
nexia.get_info()
nexia.set_petrol(4)
print(nexia.rasxod)

