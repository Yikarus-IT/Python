# Exercise 1:
# Create two string variables:
# - first_name
# - last_name
#
# Then create a third variable called full_name using an f-string.
#
# Print full_name.
first_name = "Luis Fernando"
last_name = "Rodriguez Navarro"
full_name = f"{first_name} {last_name}"
backward_name = last_name + " " + first_name

print(full_name)
print(backward_name)

# Exercise 2:
# Imagine an admin panel dashboard.
#
# Create three integer variables:
# - products
# - categories
# - users
#
# Then create a variable called total_items that adds them together.
#
# Print each individual value.
# Print total_items.
products = 125
categories = 10
users = 12

total_items = products + categories + users

print(f"Products: {products}")
print(f"Categories: {categories}")
print(f"Users: {users}")
print(f"Total Items: {total_items}")

# Exercise 3:
# Calculate the cost of a monthly service.
#
# Create:
# - monthly_cost
# - number_of_months
#
# Then create total_cost by multiplying them.
#
# Print total_cost.
monthly_cost = 1500
number_of_months = 12

total_cost = monthly_cost * number_of_months

print(f"Monthly cost: {monthly_cost}")
print(f"Number of months: {number_of_months}")
print(f"Total cost: ${total_cost}")

# Exercise 4:
# Create a string variable called starting_users.
# Store a number inside it as text, like "20".
#
# Convert starting_users into an integer and store it in starting_users_number.
#
# Create future_users by adding 10 to starting_users_number.
#
# Print future_users.

starting_users = "20"
starting_users_number = int(starting_users)

future_users = starting_users_number + 10

print(f"Starting users: {starting_users_number}")
print(f"Future users: {future_users}")