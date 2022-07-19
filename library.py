import csv
from turtle import title
from unicodedata import name
from cs50 import SQL
open ('library.db','w').close()
database = SQL("sqlite:///library.db")
database.execute(""" CREATE TABLE IF NOT EXISTS student(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    student_gender TEXT
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS book(
    book_id INTEGER NOT NULL PRIMARY KEY,
    book_title TEXT,
    book_author TEXT,
    book_publisher TEXT,
    book_copies INTEGER,
    book_cost INTEGER
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS users(
    staff_id INTEGER NOT NULL PRIMARY KEY,
    staff_name TEXT,
    staff_contact TEXT,
    staff_mail TEXT,
    staff_password TEXT,
    staff_address TEXT
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS book_records(
    book_record_id INTEGER,
    book_title TEXT,
    student_id INTEGER,
    student_name TEXT,
    staff_name TEXT,
    student_gender TEXT,
    release_date TEXT,
    due_date TEXT,
    book_return_date TEXT
    );""")
# database.execute(""" CREATE TABLE IF NOT EXISTS borrower_records(
#     borrowers_id INTEGER NOT NULL PRIMARY KEY,
#     book_title TEXT,
#     staff_name TEXT,
#     student_number_of_copies INTEGER,
#     release_date TEXT,
#     due_date TEXT
#     );""")
database.execute(""" CREATE TABLE IF NOT EXISTS relating(
    
    book_id INTEGER,
    student_id INTEGER,
    book_record_id INTEGER,
    staff_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    
    FOREIGN KEY (book_id) REFERENCES book(book_id),
    FOREIGN KEY (staff_id) REFERENCES users(staff_id)

    );""")


with open ('library_management_system.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        #titles = row['title']
        names = row['name']
        staff_name = row['staff_name']
        staff_gender = row['staff_gender']
        student_gender = row['student_gender']
        release_date = row['release_date']
        due_date = row['due_date']
        book_return_date = row['book_return_date']
        staff_name = row['staff_name']
        contact_number = row['contact_number']
        staff_mail= row['staff_mail']
        staff_password = row['staff_password']
        book_title = row['book_title']
        staff_name = row['staff_name']
        student_number_of_copioes = row['student_number_of_copies']
        release_date= row['release_date']
        due_date = row['due_date']
        book_title = row['book_title']
        staff_name = row['staff_name']
        staff_address = row['staff_address']
        #student_number_of_copies=row['student_number_copies']
        release_date = row['release_date']
        due_date = row['due_date']
        book_publisher = row['book_pubisher']
        book_author = row['book_author']
        book_copies = row['book_copies']
        book_cost = row['book_cost']
        
        database.execute("INSERT INTO student(student_name,student_gender) VALUES(?,?)",names,staff_gender)
        database.execute("INSERT INTO book(book_title,book_author,book_publisher,book_copies,book_cost) VALUES(?,?,?,?,?)",book_title,book_author,book_publisher,book_copies,book_cost)
        database.execute("INSERT INTO users(staff_name,staff_contact,staff_mail,staff_password,staff_address) VALUES(?,?,?,?,?)",staff_name,contact_number,staff_mail,staff_password,staff_address)
        database.execute("INSERT INTO book_records(book_title,student_name,staff_name,student_gender,release_date,due_date,book_return_date) VALUES(?,?,?,?,?,?,?)",book_title,names,staff_name,student_gender,release_date,due_date,book_return_date)
        #database.execute("INSERT INTO borrower_records(book_title,staff_name,student_number_of_copies,release_date,due_date) VALUES(?,?,?,?,?)",book_title,staff_name,student_number_of_copioes,release_date,due_date)
        database.execute("INSERT INTO relating(book_id,student_id,book_record_id,staff_id) VALUES((SELECT book_id FROM book WHERE book_author = ?),(SELECT student_id FROM student WHERE student_name = ?),(SELECT book_record_id FROM book_records WHERE book_record_id = ?),(SELECT staff_id FROM users WHERE staff_name =?))",book_author,names,book_title,staff_name)
        
        
        
        