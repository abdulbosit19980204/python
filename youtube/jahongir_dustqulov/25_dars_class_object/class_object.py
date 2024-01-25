class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def get_info(self):
        print("Model:", self.model, "Color:", self.color)


# spark is object from Car class
spark = Car("Spark", "white")
Nexia = Car("Nexia", "white")
# print(spark)  # <__main__.Car object at 0x000002873D6BA8D0>
print(spark.get_info())
print(Nexia.get_info())
