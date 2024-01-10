class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order(Menu):
    def __init__(self, number, ports, name, price):
        self.number = number
        self.ports = ports
        super().__init__(name, price)


class Client(Order):
    def __init__(self, table):
        self.table = table,
        self.order = []

    def set_order(self):
        self.order.append({'number': self.number, 'name': self.name, 'price': self.price, 'ports': self.ports})

    def get_order(self):
        return f"Order number: {self.number}, name: {self.name}, price: {self.price}, pors: {self.ports}, table: {self.table}"

