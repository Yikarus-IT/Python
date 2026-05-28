# Lesson 6: Dictionaries

A dictionary stores values using names called keys.

```python
user = {
    "name": "Ana",
    "role": "admin",
    "active": True,
}
```

Lists are good for multiple items.

Dictionaries are good for describing one item with multiple fields.

## Why Dictionaries Matter

Admin panel data often looks like this:

```python
product = {
    "name": "Keyboard",
    "price": 49.99,
    "stock": 12,
}
```

This shape is very close to:

- JSON from APIs
- database rows
- form data
- React state objects

## Reading Values

Use the key inside square brackets:

```python
user = {
    "name": "Ana",
    "role": "admin",
}

print(user["name"])
print(user["role"])
```

## Changing Values

```python
user = {
    "name": "Ana",
    "role": "viewer",
}

user["role"] = "admin"

print(user)
```

## Adding Values

```python
user = {
    "name": "Ana",
}

user["active"] = True

print(user)
```

## Checking If A Key Exists

Use `in` to check whether a dictionary has a key.

```python
user = {
    "name": "Ana",
}

print("name" in user)
print("email" in user)
```

## Lists Of Dictionaries

This is one of the most common shapes in real applications.

```python
users = [
    {"name": "Ana", "role": "admin"},
    {"name": "Luis", "role": "editor"},
]
```

That means:

- `users` is a list.
- Each item inside the list is a dictionary.

