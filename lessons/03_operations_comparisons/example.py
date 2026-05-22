products = 17
categories = 4

total_records = products + categories
records_per_page = 5

full_pages = total_records // records_per_page
remaining_records = total_records % records_per_page

print(f"Total records: {total_records}")
print(f"Full pages: {full_pages}")
print(f"Remaining records: {remaining_records}")

user_count = 21
minimum_users = 10

has_many_users = user_count >= minimum_users
is_exactly_ten = user_count == 10

print(f"Has many users: {has_many_users}")
print(f"Is exactly ten: {is_exactly_ten}")

raw_email = "  ADMIN@Example.COM  "
clean_email = raw_email.strip().lower()

print(f"Raw email: {raw_email}")
print(f"Clean email: {clean_email}")
print(f"Is company email: {clean_email.endswith('@example.com')}")

title = "python admin panel"

print(title.upper())
print(title.replace("python", "FastAPI"))

