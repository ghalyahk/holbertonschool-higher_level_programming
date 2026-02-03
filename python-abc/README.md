# Python ABC – Animal Example

## Description

This project demonstrates the use of **Abstract Base Classes (ABCs)** in Python using the `abc` module. An abstract class `Animal` defines a blueprint that requires subclasses to implement the `sound()` method.

Two concrete subclasses are provided:

* `Dog` → returns `"Bark"`
* `Cat` → returns `"Meow"`

Attempting to instantiate the abstract class `Animal` directly will raise a `TypeError`, as expected.

---

## Files

* **task_00_abc.py**: Contains the abstract class `Animal` and its subclasses `Dog` and `Cat`.
* **main_00_abc.py**: Test file used to verify the implementation.

---

## Requirements

* Python 3.x

No external libraries are required.

---

## Usage

Run the provided main file:

```bash
./main_00_abc.py
```

### Expected Output

```text
Bark
Meow
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Animal with abstract method sound
```

---

## Key Concepts

* Abstract Base Classes (ABC)
* `@abstractmethod` decorator
* Enforcing method implementation in subclasses

---

## Author

Holberton School – Higher Level Programming
