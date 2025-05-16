from customer import Customer
from coffee import Coffee

class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if not (0.5 < price < 15.0):
            raise ValueError("price must be greater than 0.5 and less than 15.0")

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

