# Lesson 3: Operations, Comparisons, and String Methods

In Lesson 2, we used strings and numbers.

Now we go a little deeper into what Python lets us do with them.

## Math Operators

Python can do common math operations:

```python
total = 10 + 5
difference = 10 - 5
product = 10 * 5
division = 10 / 5
```

There are also a few operators that show up often:

```python
remainder = 10 % 3
power = 2 ** 3
rounded_down = 10 // 3
```

## Comparison Operators

Comparisons return booleans: `True` or `False`.

```python
age = 21

print(age > 18)
print(age == 21)
print(age != 30)
```

Common comparison operators:

```python
==  equal to
!=  not equal to
>   greater than
<   less than
>=  greater than or equal to
<=  less than or equal to
```

## String Methods

Strings come with useful built-in actions called methods.

```python
name = "  admin panel  "

print(name.upper())
print(name.lower())
print(name.strip())
```

Common string methods:

```python
text.upper()
text.lower()
text.strip()
text.replace("old", "new")
text.startswith("A")
text.endswith(".com")
```

## Why This Matters

Admin panels constantly compare and clean data:

```python
email = " USER@EXAMPLE.COM "
clean_email = email.strip().lower()

is_admin = role == "admin"
has_enough_users = users >= 10
```

This lesson gets us ready for decisions:

```python
if is_admin:
    print("Welcome")
```

