Project Structure
customer.py – Defines the Customer class. It manages customer info and their orders.

coffee.py – Defines the Coffee class for different coffee types.

order.py – Defines the Order class connecting customers and coffees, including price validation.

tests/ – Contains unit tests I wrote using pytest to make sure everything works as expected.
Copy code
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
This project currently doesn’t have any external dependencies, but if you add any later, you can install them with:
python
from customer import Customer
from coffee import Coffee
c = Customer("Alice")
coffee = Coffee("Latte")
order = c.create_order(coffee, 5.0)
print(f"{c.name} ordered a {coffee.name} for ${order.price}")
Testing
I wrote tests to check that the code behaves properly and all rules are followed. To run all tests, use:
pytest
The tests cover attribute validation, the relationships between customers, coffees, and orders, and business logic like price limits.

