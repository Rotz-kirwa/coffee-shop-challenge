from debug import setup_logger

logger = setup_logger()

class Customer:
    def __init__(self, name):
        logger.debug(f"Initializing Customer with name: {name}")
        self.name = name  # invokes setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        logger.debug(f"Setting Customer name to: {value}")
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == "":
            raise ValueError("Name cannot be empty")
        if len(value) > 15:
            raise ValueError("Name cannot be longer than 15 characters")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order._all_orders if order.customer == self]

    def coffees(self):
        # Return unique list of Coffee instances
        coffees = set()
        for order in self.orders():
            coffees.add(order.coffee)
        return list(coffees)

    def create_order(self, coffee, price):
        logger.debug(f"Customer {self.name} creating order for coffee {coffee.name} at price {price}")
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        logger.debug(f"Finding most aficionado for coffee: {coffee.name}")
        from order import Order
        spending = {}
        for order in Order._all_orders:
            if order.coffee == coffee:
                spending[order.customer] = spending.get(order.customer, 0) + order.price
        if not spending:
            return None
        return max(spending, key=spending.get)
