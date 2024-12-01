import sqlite3 as sql
import pandas as pd

# It's easier just to try to insert everything rather than check if it already exists. SQLite3 will return an error if you try to insert a duplicate PRIMARY KEY
def try_sql_exec(statement):
    try:
        cur.execute(statement)
    except sql.OperationalError as e:
        print(f'{e}... moving on')
    except sql.IntegrityError as e:
        print(f'\r{e}... Entry already exists',end="")
   

# Variables
connection = sql.connect('original_db.db')
cur = connection.cursor()
in_file = 'no_town.csv'
clean_file = 'no_town_clean.csv'

# Try to make tables. SQLite will return an error if they already exist.
statement = '''
    CREATE TABLE Musician (
        ssn INT,
        name TEXT,
        address TEXT,
        PRIMARY KEY (ssn)
    );
'''

try_sql_exec(statement)

statement = '''
    CREATE TABLE Instrument (
        instrument_id INT,
        name TEXT,
        key TEXT,
        PRIMARY KEY (instrument_id)
    );
'''

try_sql_exec(statement)

statement = '''
    CREATE TABLE Album (
        album_id INT,
        title TEXT,
        date INT,
        format TEXT,
        PRIMARY KEY (album_id)
    );
'''

try_sql_exec(statement)

statement = '''
    CREATE TABLE Features (
        album_id INT,
        ssn INT,
        primary key (album_id, ssn),
        foreign key (album_id) references Album(album_id),
        foreign key (ssn) references Musician(ssn)
    );
'''

try_sql_exec(statement)

statement = '''
    CREATE TABLE Played (
        album_id INT,
        instrument_id INT,
        primary key (album_id, instrument_id),
        foreign key (album_id) references Album(album_id),
        foreign key (instrument_id) references Musician(instrument_id)
    );
'''

try_sql_exec(statement)
print()

# Get rid of all ' char and space char
with open(in_file, 'r') as i:
    with open(clean_file, 'w') as o:
        for line in i.readlines():
            o.write(line.replace("'","").replace(" ",""))
            
df = pd.read_csv(clean_file)

# Convert cleaned csv into the database
for data in df.values:
    try_sql_exec(f'INSERT INTO Musician (ssn, name, address) VALUES ("{data[4]}","{data[3]}","{f"{data[0]} {data[1]} {data[2]}"}")')
    try_sql_exec(f'INSERT INTO Instrument (instrument_id, name, key) VALUES ("{data[9]}","{data[10]}","{data[11]}")')
    try_sql_exec(f'INSERT INTO Album (album_id, title, date, format) VALUES ("{data[5]}","{data[6]}","{data[7]}","{data[8]}")')
    try_sql_exec(f'INSERT INTO Features (album_id, ssn) VALUES ("{data[5]}","{data[4]}")')
    try_sql_exec(f'INSERT INTO Played (album_id, instrument_id) VALUES ("{data[5]}","{data[9]}")')
print()
# Commit changes to database file
connection.commit()