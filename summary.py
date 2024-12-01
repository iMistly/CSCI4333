import sqlite3 as sql
from tabulate import tabulate

# Variables
connection = sql.connect('original_db.db')
cur = connection.cursor()

def select_print(statement):
    res = cur.execute(statement)
    relational_schema = [x[0] for x in res.description]
    print(tabulate(res, headers=relational_schema, tablefmt="pretty"))

print("Number of Musicians:")
select_print('SELECT COUNT(*) FROM Musician')
print("\nList of Musicians:")
select_print('SELECT name, ssn FROM Musician')
print("\nTotal number of Albums:")
select_print('SELECT COUNT(*) FROM Album')
print("\nList of Albums:")
select_print('SELECT title, album_id FROM Album')
print("\nTotal number of Instruments:")
select_print('SELECT COUNT(*) FROM Instrument')
print("\nList of Instruments:")
select_print('SELECT name, key, instrument_id FROM Instrument')
print("\nNumber of Albums a Musician has been featured in:")
select_print('SELECT name, COUNT(*) FROM Musician NATURAL JOIN Features GROUP BY ssn')