# Python Test-Driven Development

## Project Overview

This project contains Python exercises focused on **Test-Driven Development (TDD)**.  
Each exercise includes a Python function and corresponding tests using `doctest`.

---

## Exercise 0: Integers Addition

**File:** `0-add_integer.py`  
**Function:** `add_integer(a, b=98)`

### Description

- Adds two numbers after validating their types.
- Both `a` and `b` must be **integers** or **floats**, otherwise a `TypeError` is raised.
- Floats are **cast to integers** before addition.
- Returns an **integer**.

### Example Usage

```python
>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(100.3, -2)
98
>>> add_integer(4, "School")
Traceback (most recent call last):
TypeError: b must be an integer
