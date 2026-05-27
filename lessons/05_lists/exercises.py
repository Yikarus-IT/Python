# Exercise 1:
# Create a list called products.
# Add at least three product names as strings.
#
# Print the full list.
products = ["Keyboard", "Mouse", "Monitor"]

print(products)

# Exercise 2:
# Using your products list, print the first product.
#
# Remember: Python list indexes start at 0.
print(products[0])

# Exercise 3:
# Add one more product to the products list using append().
#
# Print the updated list.
products.append("Webcam")
print(products)

# Exercise 4:
# Create a list called roles with at least three role names.
#
# Check whether "admin" exists in the list.
# Store the result in a variable called has_admin.
#
# Print has_admin.
roles = ["Admin", "Editor", "Developer"]
has_admin = "Admin" in roles
print(has_admin)

# Exercise 5:
# Create a list called menu_items.
# Add a few admin panel menu names, like Dashboard, Users, or Settings.
#
# Print how many items are in the list using len().
menu_items = ["Dashboard", "Users", "Settings"]
print(len(menu_items))

menu_items.append("Drivers")
print(len(menu_items))



# Exercise 6:
# Create a list called statuses.
# Add values like "pending", "active", and "disabled".
#
# Change one of the values using its index.
#
# Print the updated list.
statuses = ["Pending", "Active", "Disabled"]
statuses[0] = "Inactive"
print(statuses)

# Exercise 7:
# Create a list called permissions.
# Add a few permission names.
#
# If "delete_users" exists in permissions, print "Can delete users".
# Otherwise, print "Cannot delete users".
permissions = ["edit_users", "delete_users", "view_dashboard"]

if "delete_users" in permissions:
    print("Can delete users")
else:
    print("Cannot delete users")

# Exercise 8:
# Create a list called roles.
# Add some admin panel roles.
#
# Remove "editor" from the list.
#
# Print the updated list.
roles = ["Admin", "Editor", "Developer", "Tester"]
roles.remove("Editor")
print(roles)