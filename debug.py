import logging

def setup_logger():
    logger = logging.getLogger('coffee_shop')
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

def main():
    from customer import Customer
    from coffee import Coffee
    from order import Order
    
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    print(f"Created customers: {alice.name}, {bob.name}")

    # Create coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    americano = Coffee("Americano")
    print(f"Created coffees: {latte.name}, {espresso.name}, {americano.name}")

    # Create orders
    order1 = alice.create_order(latte, 5.0)
    order2 = alice.create_order(espresso, 4.0)
    order3 = bob.create_order(latte, 6.0)
    order4 = alice.create_order(latte, 7.0)
    print(f"Order 1: {order1.customer.name} ordered {order1.coffee.name} for ${order1.price}")
    print(f"Order 2: {order2.customer.name} ordered {order2.coffee.name} for ${order2.price}")
    print(f"Order 3: {order3.customer.name} ordered {order3.coffee.name} for ${order3.price}")
    print(f"Order 4: {order4.customer.name} ordered {order4.coffee.name} for ${order4.price}")

    # Test relationship methods
    print(f"\nAlice's orders: {len(alice.orders())}")
    print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
    print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")
    print(f"Latte's order count: {latte.num_orders()}")

    # Test aggregate methods
    print(f"\nLatte's average price: ${latte.average_price():.2f}")
    print(f"Espresso's order count: {espresso.num_orders()}")
    print(f"Americano's order count: {americano.num_orders()}")

    # Test bonus: most_aficionado
    aficionado = Customer.most_aficionado(latte)
    print(f"\nMost aficionado for Latte: {aficionado.name if aficionado else 'None'}")

    # Test empty case for bonus
    aficionado = Customer.most_aficionado(americano)
    print(f"Most aficionado for Americano: {aficionado.name if aficionado else 'None'}")

if __name__ == "__main__":
    main()