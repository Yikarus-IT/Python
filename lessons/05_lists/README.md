# Lesson 5: Lists

A list stores multiple values in one variable.

```python
users = ["Ana", "Luis", "Maria"]
```

Lists are one of the most common data structures in Python.

## Why Lists Matter

Admin panels constantly work with collections:

```python
products = ["Keyboard", "Mouse", "Monitor"]
roles = ["admin", "editor", "viewer"]
menu_items = ["Dashboard", "Users", "Settings"]
```

## Reading Values

List positions are called indexes.

Python indexes start at `0`.

```python
users = ["Ana", "Luis", "Maria"]

print(users[0])
print(users[1])
print(users[2])
```

## Changing Values

```python
users = ["Ana", "Luis", "Maria"]

users[1] = "Fernando"

print(users)
```

## Adding Values

Use `.append()` to add one item to the end.

```python
users = ["Ana", "Luis"]

users.append("Maria")

print(users)
```

## Removing Values

Use `.remove()` to remove a matching value.

```python
roles = ["admin", "editor", "viewer"]

roles.remove("viewer")

print(roles)
```

## Counting Items

Use `len()` to count how many items are in a list.

```python
products = ["Keyboard", "Mouse", "Monitor"]

print(len(products))
```

## Checking If A Value Exists

Use `in` to check whether a value exists in a list.

```python
roles = ["admin", "editor", "viewer"]

print("admin" in roles)
print("manager" in roles)
```

