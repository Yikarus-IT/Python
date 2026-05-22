# Lesson 4: Conditionals

Conditionals let a program make decisions.

In Lesson 3, we learned comparisons:

```python
age >= 18
email.endswith("@example.com")
users < max_users
```

Those comparisons return `True` or `False`.

Now we use those booleans to decide what code should run.

## if

```python
age = 21

if age >= 18:
    print("Adult")
```

The indented code only runs if the condition is `True`.

## else

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

`else` runs when the `if` condition is `False`.

## elif

`elif` means "else if".

```python
role = "editor"

if role == "admin":
    print("Full access")
elif role == "editor":
    print("Can edit content")
else:
    print("Read-only access")
```

Python checks conditions from top to bottom.

## Indentation Matters

Python uses indentation to know what belongs inside the `if`.

```python
if is_active:
    print("This is inside the if")

print("This always runs")
```

## Why This Matters

Admin panels are full of decisions:

```python
if user_role == "admin":
    print("Show user management")

if stock <= 0:
    print("Out of stock")

if email.endswith("@company.com"):
    print("Company user")
```

