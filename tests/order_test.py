import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_initialization_and_price_immutable():
    cust = Customer("Alice")
    coffee = Coffee("Latte")

    order = Order(cust, coffee, 5.0)
    assert order.price == 5.0
    assert order.customer == cust
    assert order.coffee == coffee

    with pytest.raises(AttributeError):
        order.price = 10.0

def test_order_customer_and_coffee_type_checks():
    coffee = Coffee("Mocha")

    with pytest.raises(TypeError):
        Order("not_a_customer", coffee, 5.0)

    with pytest.raises(TypeError):
        Order(Customer("Alice"), "not_a_coffee", 5.0)

    with pytest.raises(ValueError):
        Order(Customer("Alice"), coffee, 0.5)

    with pytest.raises(ValueError):
        Order(Customer("Alice"), coffee, 15.0)
