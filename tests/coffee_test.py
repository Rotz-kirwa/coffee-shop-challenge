import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_getter_and_setter():
    c = Customer("Alice")
    assert c.name == "Alice"

def test_coffee_name_immutable_and_validation():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_customer_name_length_validation():
    with pytest.raises(ValueError):
        Customer("a" * 16)

def test_coffee_name_immutable_and_validation():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

    with pytest.raises(AttributeError):
        coffee.name = "Latte"

    with pytest.raises(TypeError):
        Coffee(123)

    with pytest.raises(ValueError):
        Coffee("ab")  # too short

def test_customer_orders_and_coffees_relationship():
    c = Customer("Alice")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    assert c.orders() == []
    assert c.coffees() == []

    order1 = c.create_order(coffee1, 5.0)
    order2 = c.create_order(coffee2, 4.0)

    assert order1 in c.orders()
    assert order2 in c.orders()

    assert coffee1 in c.coffees()
    assert coffee2 in c.coffees()

def test_most_aficionado():
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    coffee = Coffee("Mocha")

    assert Customer.most_aficionado(coffee) is None

    c1.create_order(coffee, 5.0)
    c1.create_order(coffee, 5.0)
    c2.create_order(coffee, 5.0)

    assert Customer.most_aficionado(coffee) == c1
