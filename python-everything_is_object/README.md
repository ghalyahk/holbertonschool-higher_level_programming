# Python – Everything is Object

## 📌 Project Description

This project explores one of Python’s core concepts: **Everything is an object**.

The goal is to understand how Python handles objects in memory, including:

* Object identity
* Object type
* Object mutability
* Object references
* Variable assignment behavior

---

## 📂 Directory

```
python-everything_is_object/
│── 0-answer.txt
│── 1-answer.txt
│── 2-answer.txt
│── 3-answer.txt
│── ...
```

Each task requires answering conceptual questions about Python object behavior.

---

## 📝 Task 3 – Right count

### Question

Do `a` and `b` point to the same object?

```python
a = 89
b = 89
```

### Answer

```
Yes
```

### Explanation

In Python, small integers (typically between -5 and 256) are cached and reused.

When assigning:

```python
a = 89
b = 89
```

Both variables reference the same integer object in memory.

This can be verified using:

```python
a is b
```

Which returns:

```
True
```

---

## 🧠 Key Concepts Covered

* `is` vs `==`
* Immutable objects
* Object identity (`id()`)
* Python memory optimization

---

## 🛠 Technologies Used

* Python 3

---

## 👩‍💻 Author

Holberton School Student

---

## 📎 Notes

This project is theoretical and focuses on understanding Python internals rather than writing executable programs.
