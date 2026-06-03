# Lesson 10: Errors and Exceptions

Errors are part of programming.

Python gives detailed error messages that tell you what went wrong and where it happened.

## Syntax Errors

A syntax error means Python could not understand the code.

Example:

```python
if True
    print("Hello")
```

This is missing a colon after `if True`.

Correct:

```python
if True:
    print("Hello")
```

## Runtime Errors

A runtime error happens while the program is running.

Example:

```python
number = int("hello")
```

Python understands the code, but it cannot convert `"hello"` into a number.

## Common Errors

### NameError

You used a variable name that does not exist.

```python
print(username)
```

### TypeError

You used a value in the wrong way.

```python
age = 30
message = "Age: " + age
```

### KeyError

You tried to read a dictionary key that does not exist.

```python
user = {"name": "Ana"}

print(user["email"])
```

### IndexError

You tried to read a list index that does not exist.

```python
products = ["Keyboard"]

print(products[5])
```

### ValueError

The value has the right type, but the wrong content.

```python
number = int("abc")
```

## try and except

Use `try` and `except` when you expect something might fail and want to handle it.

```python
raw_age = "abc"

try:
    age = int(raw_age)
    print(age)
except ValueError:
    print("Age must be a number")
```

## Avoid Catching Everything Too Early

This is possible:

```python
try:
    risky_code()
except Exception:
    print("Something went wrong")
```

But it can hide useful details.

Prefer catching the specific error you expect:

```python
except ValueError:
```

## Why This Matters

Admin panels handle user input.

Users can type invalid values:

```python
quantity = "five"
```

APIs can return missing fields:

```python
user["email"]
```

Learning errors helps you debug instead of panic.

