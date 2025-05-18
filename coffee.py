from debug import setup_logger

logger = setup_logger()

class Coffee:
    def __init__(self, name):
        logger.debug(f"Initializing Coffee with name: {name}")
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = name

    @property
    def name(self):
        return self._name

    # Make name immutable by not providing a setter

    def orders(self):
        from order import Order
        return [order for order in Order._all_orders if order.coffee == self]

    def customers(self):
        customers_set = set()
        for order in self.orders():
            customers_set.add(order.customer)
        return list(customers_set)

    def num_orders(self):
        logger.debug(f"Getting number of orders for Coffee: {self._name}")
        return len(self.orders())

    def average_price(self):
        logger.debug(f"Calculating average price for Coffee: {self._name}")
        orders = self.orders()
        if not orders:
            return 0
        total = sum(order.price for order in orders)
        return total / len(orders)
