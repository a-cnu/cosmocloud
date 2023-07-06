# cosmocloud

This is a backend application built with FastAPI in Python. It provides a set of APIs for an ecommerce application similar to Flipkart/Amazon. The APIs allow listing products, creating orders, fetching orders, updating product quantities, and more.


- Python 3.10
- FastAPI
- Pydantic

## Getting Started

To run the application, follow these steps:

1. Install the required dependencies using pip: pip install fastapi pydantic

2. Save the code provided in a Python file, e.g., `main.py`.

3. Open a terminal or command prompt and navigate to the directory where you saved `main.py`.

4. Run the application using the following command:  uvicorn main:app --reload

5. Once the server starts, you can access the APIs at `http://localhost:8000`.


The following APIs are available:

- `GET /products`: Get a list of all available products.
- `POST /orders`: Create a new order.
- `GET /orders`: Get a list of all orders (supports pagination).
- `GET /orders/{order_id}`: Get a specific order by its ID.
- `PUT /products/{product_id}`: Update the available quantity for a product.

Please refer to the code for the request and response models used in each API.



In this implementation, the data is stored in memory using global variables. This means the data will be lost once the server is restarted. If you want to persist the data, you can explore using a database like MongoDB with Pymongo or Motor.






