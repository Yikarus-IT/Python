# Exercise 1:
# Create a variable called age.
#
# If age is 18 or greater, print "Adult".
# Otherwise, print "Minor".
age = 3
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Exercise 2:
# Create a variable called user_role.
#
# If user_role is "admin", print "Full access".
# Else if user_role is "editor", print "Can edit content".
# Otherwise, print "Read-only access".
user_role = "Admin"

if user_role == "Admin":
    print("Full acces")
elif user_role == "Editor":
    print("Can edit content")
else:
    print("Read-only access")

# Exercise 3:
# Create a variable called stock.
#
# If stock is greater than 0, print "Product is available".
# Otherwise, print "Product is out of stock".
stock = 32

if stock > 0:
    print("Product is available")
else:
    print("Product is out of stock")

# Exercise 4:
# Create a variable called raw_email.
# Give it extra spaces and mixed uppercase/lowercase letters.
#
# Clean it using strip() and lower().
#
# If the clean email ends with "@example.com", print "Company email".
# Otherwise, print "External email".
raw_email = "  emAil_adresSS@example.com    "
clean_email = raw_email.strip().lower()

if clean_email.endswith("example.com"):
    print("Company email")
else:
    print("External email")

# Exercise 5:
# Create:
# - total_records
# - records_per_page
#
# Calculate:
# - full_pages
# - remaining_records
# - total_pages
#
# If there are remaining records, add one extra page to total_pages.
#
# Print total_pages.
total_records = 35
records_per_page = 6

full_pages = total_records // records_per_page
remaining_records = total_records % records_per_page
total_pages = full_pages

if remaining_records > 0:
    total_pages = total_pages + 1

print(f"Total pages: {total_pages}")
