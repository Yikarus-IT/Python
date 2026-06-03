# Exercise 1:
# Create a function called greet_user.
#
# It should receive one parameter:
# - name
#
# It should print:
# "Hello, <name>"
#
# Call the function at least twice with different names.
def greet_user(name):
    print(f"Hello, {name}")

greet_user("Jan")
greet_user("Audrey")

# Exercise 2:
# Create a function called calculate_total.
#
# It should receive:
# - price
# - quantity
#
# It should return price multiplied by quantity.
#
# Call the function and print the result.
def calculate_total(price, quantity):
    return price * quantity

print(calculate_total(20,23))
# Exercise 3:
# Create a function called get_stock_message.
#
# It should receive:
# - stock
#
# If stock is greater than 0, return "Available".
# Otherwise, return "Out of stock".
#
# Call the function with different stock values and print the results.
def get_stock_message(stock):
    if stock > 0:
        return "Available"
    else:
        return "Out of stock"

print(get_stock_message(5))
print(get_stock_message(-1))
# Exercise 4:
# Create a function called clean_username.
#
# It should receive:
# - username
#
# It should remove extra spaces and make the username lowercase.
#
# Call the function and print the result.
def clean_username(username):
    return username.strip().lower()

username = "   LuCAASS    "
print(clean_username(username))

# Exercise 5:
# Create a function called count_active_users.
#
# It should receive:
# - users
#
# users should be a list of dictionaries.
# Each dictionary should have:
# - name
# - active
#
# The function should count how many users are active.
# It should return the final count.
#
# Call the function and print the result.
def count_active_users(users):
    count = 0
    for user in users:
        if user["active"] == True:
            count += 1
    return count

users = [{"name" : "Jan", "active" : True}, {"name" : "Audrey", "active" : True}, {"name" : "Mike", "active" : False}]
print(count_active_users(users))

