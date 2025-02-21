# import sqlite3  

# #this files helps to create a simple database tables for practise so that we can execute the sql queries

# def connect_db(db_path="student.db"):
#      try:
#         conn = sqlite3.connect(db_path)
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM student")  
#         conn.close()
#         return True
#      except Exception as e:
        
#         return False
     

# def insert_values_in_table():
#     if not connect_db():
#         print("Failed to connect to database.")
#         return "Failed to connect to database."
    
#     connection = sqlite3.connect('student.db')  
#     cursor = connection.cursor()
#     cursor.execute('''  
#         CREATE TABLE if not exists student (  
#             name TEXT,  
#             class TEXT,  
#             section TEXT,  
#             marks INTEGER  
#         ); 
#     ''')

#     cursor.execute("INSERT INTO student VALUES ('Alice', 'Data Science', 'A', 90)")  
#     cursor.execute("INSERT INTO student VALUES ('Bob', 'Data Science', 'B', 85)")  
#     cursor.execute("INSERT INTO student VALUES ('Charlie', 'DevOps', 'A', 80)")  
#     cursor.execute("INSERT INTO student VALUES ('David', 'DevOps', 'B', 75)")  
#     print("Data inserted ")

#     connection.commit()  
#     connection.close()

# # insert_values_in_table() #uncomment for sample database to practise.

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("kadit_company.db")
cursor = conn.cursor()

# Create Departments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);
""")

# Create Employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    department_id INTEGER,
    hire_date DATE NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE SET NULL
);
""")

# Create Projects table
cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    start_date DATE NOT NULL,
    end_date DATE
);
""")

# Create Employee_Project (Many-to-Many Relationship)
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee_project (
    employee_id INTEGER,
    project_id INTEGER,
    role TEXT NOT NULL,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);
""")

# Create Salaries table (Tracking Salary History)
cursor.execute("""
CREATE TABLE IF NOT EXISTS salaries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    salary_amount REAL NOT NULL,
    effective_date DATE NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
);
""")

# Create Attendance table (Tracking Employee Attendance)
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    check_in_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    check_out_time TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
);
""")

# Commit changes and close connection
conn.commit()
conn.close()

print("Kadit company database with complex relationships has been created successfully!")
