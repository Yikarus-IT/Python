user_role = "admin"

if user_role == "admin":
    print("Full access")
elif user_role == "editor":
    print("Can edit content")
else:
    print("Read-only access")

stock = 0

if stock > 0:
    print("Product is available")
else:
    print("Product is out of stock")

raw_email = " MANAGER@Example.com "
email = raw_email.strip().lower()

if email.endswith("@example.com"):
    print("Company email")
else:
    print("External email")

current_users = 17
max_users = 20

if current_users < max_users:
    print("There is room for more users")
else:
    print("User limit reached")

total_records = 21
records_per_page = 5

full_pages = total_records // records_per_page
remaining_records = total_records % records_per_page
total_pages = full_pages

if remaining_records > 0:
    total_pages = total_pages + 1

print(f"Total pages: {total_pages}")

