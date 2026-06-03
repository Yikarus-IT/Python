# Lesson 9: None and Truthiness

Python has a special value called `None`.

`None` means "no value" or "nothing here".

```python
email = None
```

This is different from an empty string:

```python
email = ""
```

And different from zero:

```python
count = 0
```

## Why None Matters

In real apps, data is not always present.

```python
user = {
    "name": "Ana",
    "email": None,
}
```

That might mean the user exists, but does not have an email yet.

## Checking For None

Use `is None`:

```python
email = None

if email is None:
    print("No email found")
```

Use `is not None`:

```python
email = "ana@example.com"

if email is not None:
    print("Email exists")
```

## Truthiness

In Python, some values behave like `False` in an `if`.

These are falsy:

```python
False
None
0
""
[]
{}
```

These are truthy:

```python
True
1
"hello"
[1, 2, 3]
{"name": "Ana"}
```

## Examples

```python
name = ""

if name:
    print("Name exists")
else:
    print("Name is missing")
```

```python
users = []

if users:
    print("Users found")
else:
    print("No users found")
```

## Function Returns

Functions can return `None`.

```python
def find_user(users, name):
    for user in users:
        if user["name"] == name:
            return user

    return None
```

Then:

```python
user = find_user(users, "Ana")

if user is not None:
    print(user["name"])
else:
    print("User not found")
```

