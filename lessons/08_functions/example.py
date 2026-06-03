def welcome_user(name):
    print(f"Welcome, {name}")


welcome_user("Ana")
welcome_user("Luis")


def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(19.99, 3)

print(f"Total: {total}")


def get_stock_message(stock):
    if stock > 0:
        return "Available"

    return "Out of stock"


print(get_stock_message(12))
print(get_stock_message(0))


def count_active_users(users):
    active_users = 0

    for user in users:
        if user["active"]:
            active_users = active_users + 1

    return active_users


users = [
    {"name": "Ana", "active": True},
    {"name": "Luis", "active": False},
    {"name": "Maria", "active": True},
]

active_count = count_active_users(users)

print(f"Active users: {active_count}")


def clean_email(email):
    return email.strip().lower()


raw_email = " ADMIN@Example.COM "
email = clean_email(raw_email)

print(email)

