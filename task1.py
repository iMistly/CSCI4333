import sqlite3 as sql
import csv

connection = sql.connect('original_db.db')
cur = connection.cursor()

statement = '''
    CREATE TABLE original_data (
        num INT,
        street TEXT,
        street_type TEXT,
        person_name TEXT,
        ssn INT,
        album_id INT,
        album_name TEXT,
        year INT,
        album_type TEXT,
        instrument_id INT,
        instrument_type TEXT,
        key TEXT
    );
'''

cur.execute(statement)

with open('no_town.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    
    for row in reader:
        cur.execute('INSERT INTO original_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [row.strip(" '") for row in row])
        
connection.commit()