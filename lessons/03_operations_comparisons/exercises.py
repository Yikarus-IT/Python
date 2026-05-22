# Exercise 1:
# Create two number variables:
# - total_products
# - products_per_page
#
# Calculate:
# - full_pages using floor division
# - leftover_products using modulo
#
# Print both results.
total_products = 32
products_per_page = 7

full_pages = total_products // products_per_page
leftover_products = total_products % products_per_page

print(f"Full Pages: {full_pages}")
print(f"Leftover Products: {leftover_products}")

total_pages = full_pages + 1

print(f"Total pages: {total_pages}")

# Exercise 2:
# Create two number variables:
# - current_users
# - max_users
#
# Create a boolean variable called has_capacity.
# It should be True when current_users is less than max_users.
#
# Print has_capacity.
current_users  = 25
max_users = 10

has_capacity = current_users < max_users

print(f"Has capacity: {has_capacity}")

# Exercise 3:
# Create a string variable called raw_username.
# Give it extra spaces and mixed uppercase/lowercase letters.
#
# Create clean_username by using string methods to:
# - remove extra spaces
# - make the username lowercase
#
# Print clean_username.
raw_username = "  JSDFI JWIFE  ALDJKF     "
clean_username = raw_username.strip().lower()

print(f"Raw username: {raw_username}")
print(f"Clean username: {clean_username}")


# Exercise 4:
# Create a string variable called file_name.
# Store a fake file name like "report.csv" or "image.png".
#
# Create a boolean variable called is_csv.
# It should be True when file_name ends with ".csv".
#
# Print is_csv.
file_name = "report.csv"
is_csv = file_name.endswith("csv")

print(f"Is csv: {is_csv}")

# Exercise 5:
# Create a string variable called page_title.
# Replace one word in it using replace().
#
# Print the new title.
page_title = "Dashboard de Admin Panel"
new_page_title = page_title.replace("Admin Panel", "Admin Dashboard")

print(f"Original title: {page_title}")
print(f"New title: {new_page_title}")
