users = ["Ana", "Luis", "Maria"]

print(users)
print(users[0])
print(users[1])
print(users[2])

users[1] = "Fernando"

print(users)

users.append("Sofia")

print(users)
print(f"Total users: {len(users)}")

roles = ["admin", "editor", "viewer"]

print("admin" in roles)
print("manager" in roles)

if "admin" in roles:
    print("Admin role exists")
else:
    print("Admin role is missing")

roles.remove("viewer")

print(roles)

products = ["Keyboard", "Mouse", "Monitor"]

first_product = products[0]
last_product = products[-1]

print(f"First product: {first_product}")
print(f"Last product: {last_product}")

