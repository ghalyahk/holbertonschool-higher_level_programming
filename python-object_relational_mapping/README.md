# 0-select_states.py

## 📌 Description

This script connects to a MySQL database and lists **all states** from the table `states` in the database `hbtn_0e_0_usa`.

The results are displayed exactly as stored in the database and sorted in **ascending order by `id`**.

This project is part of the **Holberton School – Higher Level Programming** curriculum and focuses on using **Python with MySQL databases**.

---

## 🛠 Requirements

* Python 3
* MySQL server running on `localhost` at port `3306`
* Python module `MySQLdb`
* Operating system: Ubuntu 20.04 LTS

---

## 📂 File Structure

```
holbertonschool-higher_level_programming/
└── python-object_relational_mapping/
    ├── 0-select_states.py
    └── README.md
```

---

## ▶️ Usage

The script takes **3 arguments**:

1. MySQL username
2. MySQL password
3. Database name

### Example:

```bash
./0-select_states.py root root hbtn_0e_0_usa
```

### Output:

```
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

---

## 🧠 Script Behavior

* Connects to MySQL using `MySQLdb`
* Executes a `SELECT` query on the `states` table
* Sorts results by `states.id` in ascending order
* Prints each row exactly as returned by MySQL
* Code does **not run when imported** (protected by `if __name__ == "__main__"`)

---

## 🧪 Testing

No test cases are required for this task.

---

## 📚 Repository Info

* **GitHub Repository:** `holbertonschool-higher_level_programming`
* **Directory:** `python-object_relational_mapping`
* **File:** `0-select_states.py`

---

## ✍️ Author

* Student at **Holberton School**

---

✅ Task completed according to project requirements.
