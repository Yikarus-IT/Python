# Lesson 2: Strings, Numbers, and Basic Operations

In Lesson 1, we stored values in variables.

Now we learn how to work with those values.

## Strings

A string is text.

```python
name = "Pod"
```

You can join strings together:

```python
first_name = "Ada"
last_name = "Lovelace"
full_name = first_name + " " + last_name
```

You can also use an f-string, which is usually cleaner:

```python
message = f"Hello, {first_name}"
```

## Numbers

Python has integers and floats.

```python
users = 10       # int
price = 19.99    # float
```

Common operations:

```python
total = 10 + 5
difference = 10 - 5
double = 10 * 2
half = 10 / 2
```

## Type Conversion

Sometimes you need to convert a value from one type to another.

```python
age_text = "31"
age_number = int(age_text)
```

This matters because `"31"` is text, but `31` is a number.

## Comments

Python ignores comments.

```python
# This is a comment.
```

Comments are useful when explaining why something exists.

