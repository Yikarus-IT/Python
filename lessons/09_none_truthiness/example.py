email = None

if email is None:
    print("No email found")
else:
    print(email)

name = ""

if name:
    print("Name exists")
else:
    print("Name is missing")

users = []

if users:
    print("Users found")
else:
    print("No users found")

product = {
    "name": "Keyboard",
    "discount": None,
}

if product["discount"] is None:
    print("Product has no discount")
else:
    print(f"Discount: {product['discount']}")


def find_user(users, name):
    for user in users:
        if user["name"] == name:
            return user

    return None


users = [
    {"name": "Ana", "role": "admin"},
    {"name": "Luis", "role": "editor"},
]

found_user = find_user(users, "Maria")

if found_user is not None:
    print(found_user["role"])
else:
    print("User not found")

