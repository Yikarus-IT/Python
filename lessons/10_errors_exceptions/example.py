raw_quantity = "5"

try:
    quantity = int(raw_quantity)
    print(f"Quantity: {quantity}")
except ValueError:
    print("Quantity must be a number")

raw_price = "abc"

try:
    price = float(raw_price)
    print(f"Price: {price}")
except ValueError:
    print("Price must be a valid number")

user = {
    "name": "Ana",
    "role": "admin",
}

try:
    print(user["email"])
except KeyError:
    print("User has no email field")

products = ["Keyboard", "Mouse"]

try:
    print(products[5])
except IndexError:
    print("Product index does not exist")


def parse_user_count(raw_count):
    try:
        return int(raw_count)
    except ValueError:
        return None


user_count = parse_user_count("not a number")

if user_count is None:
    print("Could not parse user count")
else:
    print(f"User count: {user_count}")

