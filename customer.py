class Customer:
    def __init__(self, name):
        self.name = name  # invokes setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == "":
            raise ValueError("Name cannot be empty")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order._all_orders if order.customer == self]

    def coffees(self):
        return [order.coffee for order in self.orders()]

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        counts = {}
        for order in Order._all_orders:
            if order.coffee == coffee:
                counts[order.customer] = counts.get(order.customer, 0) + 1
        if not counts:
            return None
        return max(counts, key=counts.get)
