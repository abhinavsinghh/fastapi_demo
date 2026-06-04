from fastapi import FastAPI
from models import Product
from database import session


app = FastAPI()


@app.get("/")
def greet():
    return "Hello, World!"


products = [
    Product(id=1, name='Phone', descr='Budget Phone', price = 99, quantity = 100),
    Product(id=2, name='Laptop', descr='Gaming Laptop', price = 990, quantity = 1100),
    Product(id=3, name='Phone', descr='Premium Phone', price = 999, quantity = 1500)
]

@app.get("/products")
def get_All_products():
    db = session()
    db.query()
    return products


@app.get("/products/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product

    return "Product not found" 


@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return product


@app.put("/products")
def update_product(id: int, product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return 'Product added succesfully'
    
    return 'No product found' 

@app.delete("/products")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
        
    return "No product found"
