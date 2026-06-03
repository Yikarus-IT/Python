# Exercise 1:
# Create a variable called raw_age.
# Store a number inside it as text, like "30".
#
# Use try/except to convert raw_age into an integer.
#
# If it works, print the age.
# If it fails, print "Age must be a number".
raw_age = "30"

try:
    age = int(raw_age)
    print(age)
except ValueError:
    print("Age must be a number")

# Exercise 2:
# Create a variable called raw_price.
# Store invalid text inside it, like "abc".
#
# Use try/except to convert raw_price into a float.
#
# If it works, print the price.
# If it fails, print "Price must be a valid number".
raw_price = "price.here"

try:
    price = float(raw_price)
    print(price)
except ValueError:
    print("Price must be a valid number")

# Exercise 3:
# Create a dictionary called user.
#
# Include:
# - name
# - role
#
# Do not include email.
#
# Use try/except to print user["email"].
#
# If the email key does not exist, print "User has no email field".
user = {"name": "Joshua", "role": "Admin"}

try:
    print(user["email"])
except KeyError:
    print("User has no email field")

# Exercise 4:
# Create a list called products.
# Add two product names.
#
# Use try/except to print an index that does not exist.
#
# If the index does not exist, print "Product index does not exist".
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": 25}
]

try:
    print(products[3])
except IndexError:
    print("Product index does not exist")

# Exercise 5:
# Create a function called parse_quantity.
#
# It should receive:
# - raw_quantity
#
# It should try to convert raw_quantity into an integer.
#
# If conversion works, return the integer.
# If conversion fails, return None.
#
# Call the function.
# If the result is None, print "Invalid quantity".
# Otherwise, print the quantity.
def parse_quantity(raw_quantity):
    try:
        return int(raw_quantity)
    except ValueError:
        return None

result = parse_quantity("10")
print(result)

result = parse_quantity("abc")
print(result)
