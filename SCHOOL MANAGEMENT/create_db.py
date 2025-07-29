import sqlite3
conn=sqlite3.connect("Student.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Marks (
    student_id INTEGER,
    subject TEXT,
    marks INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Attendance (
    student_id INTEGER PRIMARY KEY,
    total_days INTEGER,
    present_days INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Fees (
    student_id INTEGER,
    actual_amount INTEGER,           
    amount_due INTEGER
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Courses(
               Course_name TEXT,
               Course_duration INTEGER,
               Course_fees INTEGER
               )
               """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS Transport(
               Route INTEGER,
               Places_Name TEXT,
               Timings TEXT
                )               
""")
students = [
    (1, 'Divya', 'divya@gmail.com'),
    (2, 'Rahul', 'rahul@gmail.com'),
    (3, 'Padma Shree', 'Padmashree34@gmail.com'),  
    (4, 'Rossy', 'rossy123@gmail.com'),        
    (5, 'Hemanth', 'hemanthgowda@gmail.com'),
    (6, 'Ambika', 'ambika@gmail.com'),
    (7, 'Kushi', 'kushi@gmail.com'),
    (8, 'Pallavi', 'pallavi@gmail.com'),
    (9, 'Priyanka', 'priyanka@gmail.com'),
    (10, 'Sagar', 'sagowda@gmail.com'),
]

for student in students:
    try:
        cursor.execute("INSERT INTO Students VALUES (?, ?, ?)", student)
    except sqlite3.IntegrityError:
        print(f"Student with id {student[0]} already exists.")


cursor.executemany("INSERT INTO Marks VALUES (?, ?, ?)", [
    (1, 'Math', 85),
    (2, 'Science', 92),
    (3, 'Math', 78),
    (4, 'Science', 88),
    (5, 'Science', 88),
    (6, 'Science', 88),
    (7, 'Science', 88),
    (8, 'Science', 88),
    (9, 'Science', 88),
    (10, 'Science', 88)
])

cursor.executemany("INSERT INTO Attendance VALUES (?, ?, ?)", [
    (1, 100, 95),
    (2, 100, 89),
    (3, 100,  72),
    (4, 100,  83),  
    (5, 100,  77),
    (6, 100,  56),
    (7, 100,  92),
    (8, 100,  86),
    (9, 100,  56),
    (10, 100,  21)
])


cursor.executemany("INSERT INTO Fees VALUES (?, ?,?)", [
    (1, 2250000,2000),
    (2, 2250000,1500),
    (3, 2250000,15000),
    (4, 2250000,12000),
    (5, 2250000,15000),
    (6, 2250000,13400),
    (7, 2250000,11500),
    (8, 2250000,14500),
    (9, 2250000,23000),
    (10,2250000,50000)
])
cursor.executemany("INSERT INTO Courses VALUES(?,?,?)", [
    ("Computer Science", 4, 230000),
    ("Aeronatics", 4, 230000),
    ("PHD Mathamatics ",2, 220000),
    ("Electrical Engineering", 4, 230000),
    ("Data Science", 4, 210000),
    ("Basic Science", 4, 240000)
])
cursor.executemany("INSERT INTO Transport VALUES(?,?,?)",[
    (1,"Rajankunte",'06:45 am'),
    (1,"Peenya",'07:01 am'),
    (1,"Dasarahalli",'07:15 am'),
    (1,"Ulall Nagar",'07:30 am'),
    (1,"Deepak Nagar",'07:45 am'),
    (2,"Kengeri",'07:50 am'),
    (2,"Gandhi Nagar",'08:01 am'),
    (2,"Madavara",'08:15 am'),
    (2,"Cake factory",'08:30 am'),
    (2,"Rajkumar Road",'08:45 am'),
    (2,"Nelamangala",'08:50 am')
])


conn.commit()
conn.close()

print("✅ Student.db created with sample data.")
