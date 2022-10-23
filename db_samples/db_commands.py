"""Sample DB commands"""

import mysql.connector

# Set constants
DB_NAME = "storage"
TABLE_NAME = "Persons"
FIELDS_DESC = "(PersonID int, FirstName varchar(255), City varchar(255))"
# Persons
PERSON_ARTHUR = '(1, "Arthur", "Delaver")'
PERSON_JAMES = '(2, "James", "Amsterdam")'

# SQL Commands
CREATE_DB_IF_NOT_EXISTS = "CREATE DATABASE IF NOT EXISTS {db}"
SHOW_DATABASES = "SHOW DATABASES"
CREATE_TABLE = "CREATE TABLE {db}.{name} {fields}"
INSERT_INTO = "INSERT INTO {db}.{table} {fields} VALUES {values}"
SELECT = "SELECT {fields} FROM {db}.{table}"
DROP_DB = "DROP DATABASE {db}"

# Connect to MYSQL server
mydb = mysql.connector.connect(
    host="localhost", port="3306", user="root", password="1234"
)

# Get cursor
mycursor = mydb.cursor()

# Create database if not exists
mycursor.execute(CREATE_DB_IF_NOT_EXISTS.format(db=DB_NAME))

# Get all databases
mycursor.execute(SHOW_DATABASES)

# Print the result
x = mycursor.fetchall()
print("======================DATABASES===========================")
print(x)

# Create some table
mycursor.execute(
    CREATE_TABLE.format(db=DB_NAME, name=TABLE_NAME, fields=FIELDS_DESC)
)

# Insert data into table
mycursor.execute(
    INSERT_INTO.format(
        db=DB_NAME, table=TABLE_NAME, fields="", values=PERSON_ARTHUR
    )
)
mycursor.execute(
    INSERT_INTO.format(
        db=DB_NAME, table=TABLE_NAME, fields="", values=PERSON_JAMES
    )
)

# Select data
print("======================SELECT * FROM ===========================")
mycursor.execute(SELECT.format(fields="*", db=DB_NAME, table=TABLE_NAME))
# Print the result
for x in mycursor:
    print(x)

# Select data
print("======================SELECT FirstName FROM ===========================")
mycursor.execute(
    SELECT.format(fields="FirstName", db=DB_NAME, table=TABLE_NAME)
)
# Print the result
for x in mycursor:
    print(x)

# Drop database
mycursor.execute(DROP_DB.format(db=DB_NAME))

# Get all databases
mycursor.execute(SHOW_DATABASES)

# Print the result
print("======================DATABASES===========================")
print(mycursor.fetchone())
print(mycursor.fetchone())
print(mycursor.fetchone())
print(mycursor.fetchone())
print(mycursor.fetchone())
print(mycursor.fetchone())
