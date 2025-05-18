from customer import Customer
from coffee import Coffee
from debug import setup_logger

logger = setup_logger()

class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0 inclusive")
        logger.debug(f"Creating Order: customer={customer.name}, coffee={coffee.name}, price={price}")

        self.customer = customer
        self.coffee = coffee
        self._price = price

        Order._all_orders.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        raise AttributeError("price attribute is read-only")
