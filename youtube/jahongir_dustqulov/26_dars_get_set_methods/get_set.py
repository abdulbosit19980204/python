class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def get_model(self):
        return self.model.upper()

    def set_color(self, color):
        print(f"Color  changed from {self.color} to {color}")
        self.color = color

    def get_full_info(self):
        return f"Model:{self.model} Color: {self.color}"


spark = Car("Spark", "white")
Nexia = Car("Nexia", "White")
print(spark.get_full_info())  # Model:Spark Color: white
print(Nexia.get_model())  # NEXIA
spark.set_color("grey")
print(spark.get_full_info())  # Model:Spark Color: grey
