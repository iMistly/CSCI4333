import sqlite3 as sql

# It's easier just to try to insert everything rather than check if it already exists. SQLite3 will return an error if you try to insert a duplicate PRIMARY KEY
def try_sql_exec(statement):
    try:
        cur.execute(statement)
    except sql.OperationalError as e:
        print(f'{e}... moving on')
    except sql.IntegrityError as e:
        print(f'\r{e}... Entry already exists',end="")
    except sql.Error as e:
        print(f'\r{e}... Error',end="")
   

# Variables
connection = sql.connect('no_town.db')
connection_original = sql.connect('original_db.db')
cur = connection.cursor()
cur_original = connection_original.cursor()

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
        year INT,
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

# Convert orginal_data from original_db.db to new database

data = cur_original.execute('SELECT * FROM original_data').fetchall()

for row in data:
    address = f'{row[0]} {row[1]} {row[2]}'
    ssn = row[4]
    name = row[3]
    album_id = row[5]
    title = row[6]
    year = row[7]
    format = row[8]
    instrument_id = row[9]
    instrument_name = row[10]
    instrument_key = row[11]

    # Insert into Musician
    try_sql_exec(f'INSERT INTO Musician (ssn, name, address) VALUES ({ssn}, "{name}", "{address}");')

    # Insert into Instrument
    try_sql_exec(f'INSERT INTO Instrument (instrument_id, name, key) VALUES ({instrument_id}, "{instrument_name}", "{instrument_key}");')
    
    # Insert into Album
    try_sql_exec(f'INSERT INTO Album (album_id, title, year, format) VALUES ({album_id}, "{title}", {year}, "{format}");')
    
    # Insert into Features
    try_sql_exec(f'INSERT INTO Features (album_id, ssn) VALUES ({album_id}, {ssn});')
    
    # Insert into Played
    try_sql_exec(f'INSERT INTO Played (album_id, instrument_id) VALUES ({album_id}, {instrument_id});')

# Commit changes to database file
connection.commit()