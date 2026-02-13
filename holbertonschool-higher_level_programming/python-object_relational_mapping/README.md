# Python - Object Relational Mapping

This project is part of the Holberton School Higher Level Programming curriculum.

It focuses on connecting Python programs to a MySQL database using:
- MySQLdb (SQL queries)
- SQLAlchemy (ORM)

The goal is to understand how to interact with databases from Python, both by writing raw SQL queries and by using an Object Relational Mapper (ORM).

---

## 🛠 Technologies Used

- Python 3
- MySQL 5.7
- MySQLdb module
- SQLAlchemy
- Ubuntu 20.04 LTS

---

## 📂 Project Structure

Each script connects to a MySQL database running on `localhost` at port `3306`.

Scripts accept MySQL credentials and database name as command-line arguments.

Example:
```bash
./0-select_states.py root root hbtn_0e_0_usa
