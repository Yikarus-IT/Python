# Lesson 8: Functions

A function is a reusable block of code.

```python
def greet():
    print("Hello")
```

To run the function, call it:

```python
greet()
```

## Why Functions Matter

Without functions, code gets repeated.

```python
print("Welcome, Ana")
print("Welcome, Luis")
print("Welcome, Maria")
```

With a function:

```python
def welcome_user(name):
    print(f"Welcome, {name}")

welcome_user("Ana")
welcome_user("Luis")
welcome_user("Maria")
```

## Parameters

Parameters are values a function receives.

```python
def welcome_user(name):
    print(f"Welcome, {name}")
```

Here, `name` is a parameter.

## Return Values

Some functions give a value back using `return`.

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(10, 3)

print(total)
```

`print()` shows something in the terminal.

`return` gives a value back to the code that called the function.

## Functions With Conditionals

```python
def get_stock_message(stock):
    if stock > 0:
        return "Available"

    return "Out of stock"
```

## Functions With Lists

```python
def count_active_users(users):
    active_users = 0

    for user in users:
        if user["active"]:
            active_users = active_users + 1

    return active_users
```

Functions let us package useful behavior into small named pieces.

