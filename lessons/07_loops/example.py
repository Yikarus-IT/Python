menu_items = ["Dashboard", "Users", "Products", "Settings"]

for item in menu_items:
    print(item)

products = [
    {"name": "Keyboard", "stock": 12},
    {"name": "Mouse", "stock": 0},
    {"name": "Monitor", "stock": 4},
]

for product in products:
    if product["stock"] > 0:
        print(f"{product['name']} is available")
    else:
        print(f"{product['name']} is out of stock")

users = [
    {"name": "Ana", "role": "admin", "active": True},
    {"name": "Luis", "role": "editor", "active": False},
    {"name": "Maria", "role": "viewer", "active": True},
]

active_users = 0

for user in users:
    if user["active"]:
        active_users = active_users + 1

print(f"Active users: {active_users}")

for page_number in range(1, 6):
    print(f"Page {page_number}")

