from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
products = []
orders = []

class Product(BaseModel):
    name: str
    price: float
    quantity: int

class Address(BaseModel):
    city: str
    country: str
    zip_code: str

class OrderItem(BaseModel):
    product_id: int
    bought_quantity: int

class Order(BaseModel):
    timestamp: str
    items: list[OrderItem]
    total_amount: float
    address: Address

@app.get("/products")
async def get_products():
    return products

@app.post("/orders")
async def create_order(order: Order):
    orders.append(order)
    return order

@app.get("/orders")
async def get_orders(limit: int = 10, offset: int = 0):
    return orders[offset : offset + limit]

@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    for order in orders:
        if order.id == order_id:
            return order
    return {"message": "Order not found"}

@app.put("/products/{product_id}")
async def update_product(product_id: int, quantity: int):
    for product in products:
        if product.id == product_id:
            product.quantity = quantity
            return product
    return {"message": "Product not found"}

def initialize_dummy_data():
    dummy_products = [
        Product(name="TV", price=500, quantity=10),
        Product(name="Laptop", price=1000, quantity=5),
        Product(name="Mobile", price=300, quantity=20),
    ]
    products.extend(dummy_products)

initialize_dummy_data()
