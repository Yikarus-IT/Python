# Exercise 1:
# Create a dictionary called user.
#
# It should have:
# - name
# - role
# - active
#
# Print the full dictionary.
user = {
    "name": "Yari",
    "role": "Admin",
    "active": True
}

# Exercise 2:
# Using your user dictionary, print only the user's name.
print(user["name"])

# Exercise 3:
# Change the user's role to a different role.
#
# Print the updated dictionary.
user["role"] = "Editor"

print(user["role"])

# Exercise 4:
# Add an email field to the user dictionary.
#
# Print the updated dictionary.
user["email"] = "yari@email.com"

print(user["email"])

# Exercise 5:
# Check whether the user dictionary has an email key.
#
# Store the result in a variable called has_email.
#
# Print has_email.
has_email = "email" in user

print(has_email)

# Exercise 6:
# Create a dictionary called product.
#
# It should have:
# - name
# - price
# - stock
#
# If stock is greater than 0, print "Available".
# Otherwise, print "Out of stock".
product = {
    "name": "iPad",
    "price": 450.00,
    "stock": 15
}

if product["stock"] > 0:
    print("Available")
else:
    print("Out of stock")

# Exercise 7:
# Create a list called users.
#
# The list should contain at least three dictionaries.
# Each dictionary should describe one user with:
# - name
# - role
#
# Print the first user's name.
# Print the last user's role.
users = [
    {
        "name": "Alan",
        "role": "Admin"
    },
    {
        "name": "Kari",
        "role": "Developer"
    },
    {
        "name": "Sharon",
        "role": "Editor"
    }
]

print(users[0]["name"])
print(users[-1]["role"])
