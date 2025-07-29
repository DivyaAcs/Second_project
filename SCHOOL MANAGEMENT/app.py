from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('Student.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route - Welcoming page
@app.route('/')
def index():
    return render_template('index.html')

# Dashboard route - Common layout with sidebar
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Students details page
@app.route('/students')
def students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM Students').fetchall()
    conn.close()
    return render_template('student.html', students=students)

# Courses details page
@app.route('/courses')
def courses():
    conn = get_db_connection()
    courses = conn.execute('SELECT * FROM Courses').fetchall()
    conn.close()
    return render_template('courses.html', courses=courses)

# Marks details page
@app.route('/marks')
def marks():
    conn = get_db_connection()
    marks = conn.execute('SELECT * FROM Marks').fetchall()
    conn.close()
    return render_template('marks.html', marks=marks)

# Attendance details page
@app.route('/attendance')
def attendance():
    conn = get_db_connection()
    attendance = conn.execute('SELECT * FROM Attendance').fetchall()
    conn.close()
    return render_template('attendance.html', attendance=attendance)

@app.route('/transport')
def transport():
    conn = get_db_connection()
    transport = conn.execute('SELECT * FROM Transport').fetchall()
    conn.close()
    route1 =[row for row in transport if row['Route']==1]
    route2 =[row for row in transport if row['Route']==2]
    return render_template('transport.html',route1=route1,route2=route2)
    




if __name__ == '__main__':
    app.run(debug=True)
