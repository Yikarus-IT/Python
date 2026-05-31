# Exercise 1:
# Create a list called menu_items.
# Add at least four admin panel menu names.
#
# Use a for loop to print each menu item.
menu_items = ['dashboard', 'users', 'products', 'orders']
for item in menu_items:
    print(item)

# Exercise 2:
# Create a list called products.
#
# The list should contain at least three dictionaries.
# Each product dictionary should have:
# - name
# - stock
#
# Use a for loop to print each product's name.
products = [
    {'name': 'apple', 'stock': 8},
    {'name': 'radish', 'stock': 6},
    {'name': 'banana', 'stock': 0}
]

for product in products:
    print(product['name'])

# Exercise 3:
# Using your products list, use a for loop with an if statement.
#
# If a product's stock is greater than 0, print:
# "<product name> is available"
#
# Otherwise, print:
# "<product name> is out of stock"
for product in products:
    if (product['stock'] > 0):
        print(f"{product['name']} is available")
    else:
        print(f"{product['name']} is out of stock")
# Exercise 4:
# Create a list called users.
#
# The list should contain at least three dictionaries.
# Each user dictionary should have:
# - name
# - active
#
# Count how many users are active.
#
# Print the final active user count.
users = [
    {'name': 'juan', 'active': True},
    {'name': 'maria', 'active': False},
    {'name': 'luis', 'active': True}
]
active_users = 0
for user in users:
    if (user['active'] == True):
        active_users +=1
print(f"Total active users: {active_users}")

# Exercise 5:
# Use range() to print page numbers from 1 through 5.
for number in range(1,6):
    print(number)
