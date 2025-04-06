from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import uvicorn
import time
import datetime
import os
from burgers import Burger
from person import Student, Staff

# Create static directory if it doesn't exist
os.makedirs("static", exist_ok=True)

app = FastAPI(title="De Anza Food Court API", 
              description="API for the De Anza Food Court ordering system")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create burger items directly in the API
menu_items = {
    "de_anza_burger": Burger("De Anza Burger", 1, 5.25),
    "bacon_cheese": Burger("Bacon Cheese", 2, 5.75), 
    "mushroom_swiss": Burger("Mushroom Swiss", 3, 5.95),
    "western_burger": Burger("Western Burger", 4, 5.95),
    "don_cali_burger": Burger("Don Cali Burger", 5, 5.95)
}

# Initialize order dictionary
order_dict = {key: 0 for key in menu_items}

# Track order totals
price_no_tax = 0
price_after_tax = 0
total_tax = 0

class BurgerModel(BaseModel):
    name: str
    id: int
    price: float

class OrderItemModel(BaseModel):
    burger_name: str
    quantity: int

class CustomerType(BaseModel):
    is_student: bool

class OrderResponse(BaseModel):
    items: Dict[str, dict]
    price_no_tax: float = 0
    tax_amount: float = 0
    price_after_tax: float = 0
    
@app.get("/", response_class=HTMLResponse, tags=["General"])
async def read_root():
    """
    Serve the main HTML page
    """
    with open("static/index.html", "r") as file:
        return file.read()

@app.get("/menu", tags=["Menu"])
async def get_menu():
    """
    Get the full menu with all available burger options
    """
    menu_response = {}
    for key, burger in menu_items.items():
        menu_response[key] = {
            "name": burger.name,
            "id": burger.number,
            "price": burger.price
        }
    return menu_response

@app.get("/order", response_model=OrderResponse, tags=["Order"])
async def get_order():
    """
    Get the current order details with order items and pricing
    """
    order_items = {}
    for item_name, quantity in order_dict.items():
        if quantity > 0:
            burger = menu_items[item_name]
            order_items[item_name] = {
                "name": burger.name,
                "price": burger.price,
                "quantity": quantity,
                "item_total": burger.price * quantity
            }
    
    # Return full order details similar to Order.py print_bill
    return {
        "items": order_items,
        "price_no_tax": round(price_no_tax, 2),
        "tax_amount": round(total_tax, 2),
        "price_after_tax": round(price_after_tax, 2)
    }

@app.post("/order/add", tags=["Order"])
async def add_item(item: OrderItemModel):
    """
    Add a burger to the current order
    """
    if item.burger_name not in menu_items:
        raise HTTPException(status_code=404, detail="Burger not found")
    
    if item.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be positive")
    
    order_dict[item.burger_name] += item.quantity
    return {"message": f"{item.quantity} {item.burger_name}(s) added to the order"}

@app.delete("/order/{burger_name}", tags=["Order"])
async def delete_item(burger_name: str):
    """
    Delete a burger from the current order
    """
    if burger_name not in order_dict:
        raise HTTPException(status_code=404, detail="Item not found in order")
    
    if order_dict[burger_name] <= 0:
        raise HTTPException(status_code=400, detail="No items to delete")
    
    del order_dict[burger_name]
    return {"message": f"{burger_name} has been deleted from the order"}

@app.post("/order/calculate", tags=["Order"])
async def calculate_order(customer: CustomerType):
    """
    Calculate the total price of the order with tax based on customer type
    """
    global price_no_tax, total_tax, price_after_tax
    
    if customer.is_student:
        price_no_tax = sum(
            order_dict[item] * float(menu_items[item].price) 
            for item in order_dict 
            if order_dict[item] > 0
        )
        total_tax = price_no_tax * Student().get_tax_rate()
    else:
        price_no_tax = sum(
            order_dict[item] * float(menu_items[item].price) 
            for item in order_dict
            if order_dict[item] > 0
        )
        total_tax = price_no_tax * Staff().get_tax_rate()
    
    price_after_tax = price_no_tax + total_tax
    
    return {
        "price_no_tax": round(price_no_tax, 2),
        "tax_amount": round(total_tax, 2),
        "price_after_tax": round(price_after_tax, 2)
    }

@app.post("/order/bill", tags=["Order"])
async def generate_bill():
    """
    Generate a detailed bill for the current order
    """
    # Similar to print_bill in Order.py
    bill_items = []
    for item_name, quantity in order_dict.items():
        if quantity > 0:
            burger = menu_items[item_name]
            item_cost = burger.price * quantity
            bill_items.append({
                "name": item_name,
                "burger_name": burger.name,
                "price": burger.price,
                "quantity": quantity,
                "cost": item_cost
            })
    
    bill = {
        "restaurant": "De Anza Food Court",
        "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "items": bill_items,
        "total_before_tax": round(price_no_tax, 2),
        "tax_amount": round(total_tax, 2),
        "total_after_tax": round(price_after_tax, 2)
    }
    
    return bill

@app.post("/order/save", tags=["Order"])
async def save_order():
    """
    Save the current order to a file
    """
    if not any(order_dict.values()):
        raise HTTPException(status_code=400, detail="Cannot save an empty order")
    
    # Similar to save_to_file in Order.py
    time_stamp = time.time()
    order_time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H-%M-%S')
    filename = order_time_stamp + '.txt'

    with open(filename, 'w') as file:
        file.write("            Here is your order detail:\n")
        file.write("**********************************************************\n")
        for item_name, quantity in order_dict.items():
            if quantity > 0:
                item_price = menu_items[item_name].price
                item_cost = item_price * quantity
                file.write(
                    f"{item_name} - Price: ${item_price:.2f}, Quantity: {quantity}, Cost: ${item_cost:.2f}\n")
        file.write("**********************************************************\n")
        file.write(f"Total before tax: ${price_no_tax:.2f}\n")
        file.write(f"Tax Amount: ${total_tax:.2f}\n")
        file.write(f"Total price after tax: ${price_after_tax:.2f}\n")
    
    return {"message": f"Order saved to file: {filename}"}

@app.post("/order/reset", tags=["Order"])
async def reset_order():
    """
    Reset the current order
    """
    global order_dict, price_no_tax, total_tax, price_after_tax
    order_dict = {key: 0 for key in menu_items}
    price_no_tax = 0
    total_tax = 0
    price_after_tax = 0
    return {"message": "Order has been reset"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 