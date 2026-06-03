# Exercise 1:
# Create a variable called email and set it to None.
#
# If email is None, print "No email found".
# Otherwise, print the email.
email = None
if email is None:
    print("No email found")
else:
    print(email)

# Exercise 2:
# Create a variable called username.
# Set it to an empty string.
#
# Use truthiness to check whether username has a value.
#
# If it has a value, print "Username exists".
# Otherwise, print "Username is missing".
username = ""

if username:
    print("Username exists")
else:
    print("Username is missing")

# Exercise 3:
# Create a list called products.
# Start with an empty list.
#
# Use truthiness to check whether the list has items.
#
# If it has items, print "Products found".
# Otherwise, print "No products found".
products = []

if products:
    print("Products found")
else:
    print("No products found")

# Exercise 4:
# Create a dictionary called user.
#
# It should have:
# - name
# - phone
#
# Set phone to None.
#
# If phone is None, print "No phone number".
# Otherwise, print the phone number.
user = {
    "name": "John",
    "phone": None
}

if user['phone']:
    print(user['phone'])
else:
    print("No phone number")

# Exercise 5:
# Create a function called find_product.
#
# It should receive:
# - products
# - product_name
#
# products should be a list of dictionaries.
# Each product dictionary should have:
# - name
# - stock
#
# If a product with that name exists, return that product dictionary.
# If no product matches, return None.
#
# Call the function.
# If the result is not None, print the product stock.
# Otherwise, print "Product not found".
def find_product(products, product_name):
    for product in products:
        if product['name'] == product_name:
            return product
    return None

products = [
    {'name': 'Laptop', 'stock': 10},
    {'name': 'Mouse', 'stock': 20},
    {'name': 'Keyboard', 'stock': 15}
]
result = find_product(products, "Laptop")

if result:
    print(result['stock'])
else:
    print("Product not found")

