import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# New South Indian Employees with Departments and Projects
new_employees = [
    ("Surya Narayan", "surya.narayan@kadit.com", "Software Development", "2023-06-12", "AI Chatbot"),
    ("Deepika Rajan", "deepika.rajan@kadit.com", "HR", "2021-10-05", "Employee Engagement"),
    ("Karthik Ramesh", "karthik.ramesh@kadit.com", "Marketing", "2022-02-18", "SEO Optimization"),
    ("Anjali Menon", "anjali.menon@kadit.com", "Finance", "2020-07-25", "Budget Planning"),
    ("Govind Shankar", "govind.shankar@kadit.com", "Software Development", "2023-11-01", "RAG-based Search Engine"),
]

# Insert Departments if not exists
for _, _, department, _, _ in new_employees:
    cursor.execute("INSERT OR IGNORE INTO departments (name) VALUES (?)", (department,))

# Insert Employees and Assign to Projects
for name, email, department, hire_date, project in new_employees:
    # Get Department ID
    cursor.execute("SELECT id FROM departments WHERE name = ?", (department,))
    department_id = cursor.fetchone()[0]

    # Insert Employee
    cursor.execute("""
        INSERT INTO employees (name, email, department_id, hire_date)
        VALUES (?, ?, ?, ?)
    """, (name, email, department_id, hire_date))

    # Get Employee ID
    cursor.execute("SELECT id FROM employees WHERE email = ?", (email,))
    employee_id = cursor.fetchone()[0]

    # Ensure Project Exists
    cursor.execute("INSERT OR IGNORE INTO projects (name, start_date) VALUES (?, ?)", (project, hire_date))

    # Get Project ID
    cursor.execute("SELECT id FROM projects WHERE name = ?", (project,))
    project_id = cursor.fetchone()[0]

    # Assign Employee to Project
    cursor.execute("""
        INSERT INTO employee_project (employee_id, project_id, role)
        VALUES (?, ?, ?)
    """, (employee_id, project_id, "Team Member"))

# Commit changes
conn.commit()
print("New South Indian employees added and assigned to projects successfully.")

# Close connection
conn.close()
