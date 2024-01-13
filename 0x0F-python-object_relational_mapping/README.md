# Project README

## Before You Start
Please make sure your MySQL server is in version 8.0. You can find instructions on how to install MySQL 8.0 on Ubuntu 20.04.

## Background Context
In this project, you'll bridge the worlds of Databases and Python. The first part involves using the MySQLdb module to connect to a MySQL database and execute SQL queries. The second part utilizes the SQLAlchemy module, an Object-Relational Mapper (ORM), eliminating the need for direct SQL queries. With an ORM, your focus shifts from storage details to working with Python objects. This flexibility allows easy storage changes without rewriting your entire project.

### Without ORM Example:
```python
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
