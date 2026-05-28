user = {
    "name": "Ana",
    "role": "admin",
    "active": True,
}

print(user)
print(user["name"])
print(user["role"])
print(user["active"])

user["role"] = "editor"
user["email"] = "ana@example.com"

print(user)

if "email" in user:
    print("User has an email")
else:
    print("User does not have an email")

product = {
    "name": "Keyboard",
    "price": 49.99,
    "stock": 12,
}

print(f"Product: {product['name']}")
print(f"Price: {product['price']}")

if product["stock"] > 0:
    print("Product is available")
else:
    print("Product is out of stock")

users = [
    {"name": "Ana", "role": "admin"},
    {"name": "Luis", "role": "editor"},
    {"name": "Maria", "role": "viewer"},
]

print(users)
print(users[0])
print(users[0]["name"])
print(users[-1]["role"])

