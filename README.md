# CSCI4333 - Yifeng Gao
## Database Design & Implement

This class uses Python and SQLite3 to learn how to create databases more effectively. We also learned less-computerized techniques such as creating ER-Diagrams and Relational Schema by hand.

I created this repository to archive my final project progress though it is a little late into the semester...

# Guidlines:
## CSCI4333 Database Project
Notown Records has decided to store information about musicians who perform on its albums (as well as other company data) in a database. The company has wisely chosen to hire you as a database designer. Here is the background information provided by the company:
1. Each musician that records at Notown has a name, address (number, street name, and street type), and an SSN.
2. Each instrument purchased at Notown has an id, a name (suppose only three names: guitar, synthesizer, flute), and a musical key (suppose only six types: C, B, E, C-flat, B-flat, E-flat).
3. Each album recorded on the Notown label has a title, an album identifier, a copyright date, and a format (CD or MC).
4. Each musician may participate in several albums and a given album may be designed by several musicians.
5. Each instrument can be used in any number of albums, and an album may use several instruments. 

The data is stored in a huge CSV file provided to you (no town.csv). And now, they want to take advantage of advanced database design to better manage the data. To help the company, these are the tasks you need to address: 

**Task 1**: (5 pt) Build a database (named as original db.db) via Python and SQLite. And import the data in the CSV file into the database. Your code should be written in `task1.py`. 

**Task 2**: (5 pt) Draw an ER-model based on the description and build the database via Python and SQLite that is generated from the ER model. En- forcing all the key/participation constraints. Your code should be written in `task2.py`. 

**Task 3**: (5 pt) Extract the corresponding information from the database `.py` and put it into the corresponding table in the database. 1 

**Task 4**: (5 pt) The company asks you to implement a Python program for the following function: `summary.py`: Return the summary report of the company. The report includes:
1. A total number of musicians and a list of musicians (name and ssn).
2. A total number of albums and a list of albums recorded at Notown (name
and album id).
3. A total number of instruments and a list of instruments at Notown (name,
key, and id).
4. A table consists of the names of musicians and the total number of albums
written by them.