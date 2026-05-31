# Lesson 7: Loops

Loops let Python repeat work.

The most common loop in Python is a `for` loop.

```python
users = ["Ana", "Luis", "Maria"]

for user in users:
    print(user)
```

This means:

```text
For each user in users, run this indented code.
```

## Why Loops Matter

Admin panels usually work with many records:

```python
products = ["Keyboard", "Mouse", "Monitor"]
```

Without a loop, you would write:

```python
print(products[0])
print(products[1])
print(products[2])
```

With a loop:

```python
for product in products:
    print(product)
```

That works even if the list has 3 items or 3,000 items.

## Looping Over Dictionaries In A List

This is very common in real apps.

```python
users = [
    {"name": "Ana", "role": "admin"},
    {"name": "Luis", "role": "editor"},
]

for user in users:
    print(user["name"])
```

## Using if Inside A Loop

You can combine loops with conditionals.

```python
products = [
    {"name": "Keyboard", "stock": 10},
    {"name": "Mouse", "stock": 0},
]

for product in products:
    if product["stock"] > 0:
        print(f"{product['name']} is available")
    else:
        print(f"{product['name']} is out of stock")
```

## range

`range()` creates a sequence of numbers.

```python
for number in range(5):
    print(number)
```

This prints:

```text
0
1
2
3
4
```

Like list indexes, `range(5)` starts at `0` and stops before `5`.

