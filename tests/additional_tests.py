import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_most_aficionado_ties_and_empty():
    coffee1 = Coffee("Mocha")
    coffee2 = Coffee("Latte")
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    c3 = Customer("Charlie")

    # No orders yet, so no aficionado
    assert Customer.most_aficionado(coffee1) is None

    # Both Alice and Bob have one order each, so it's a tie
    c1.create_order(coffee1, 5.0)
    c2.create_order(coffee1, 5.0)
    assert Customer.most_aficionado(coffee1) in [c1, c2]

    # Charlie has two orders, so he should be the aficionado now
    c3.create_order(coffee1, 5.0)
    c3.create_order(coffee1, 5.0)
    assert Customer.most_aficionado(coffee1) == c3

    # Latte has no orders, so no aficionado
    assert Customer.most_aficionado(coffee2) is None

def test_coffee_name_immutable_and_validation():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

    # Trying to change the name should fail because it's read-only
    with pytest.raises(AttributeError):
        coffee.name = "Latte"

    # Name must be a string, so this should fail
    with pytest.raises(TypeError):
        Coffee(123)

    # Name must be at least 3 characters long
    with pytest.raises(ValueError):
        Coffee("ab")  # too short

def test_customer_name_length_validation():
    # Name longer than 15 characters should raise an error
    with pytest.raises(ValueError):
        Customer("a" * 16)

def test_order_price_boundaries():
    c = Customer("Alice")
    coffee = Coffee("Latte")

    # Prices at the limits should be accepted
    Order(c, coffee, 1.0)
    Order(c, coffee, 10.0)

    # Prices outside the limits should raise errors
    with pytest.raises(ValueError):
        Order(c, coffee, 0.99)

    with pytest.raises(ValueError):
        Order(c, coffee, 10.01)
