import sqlite3  

#this files helps to create a simple database tables for practise so that we can execute the sql queries

def connect_db(db_path="student.db"):
     try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")  
        conn.close()
        return True
     except Exception as e:
        
        return False
     

def insert_values_in_table():
    if not connect_db():
        print("Failed to connect to database.")
        return "Failed to connect to database."
    
    connection = sqlite3.connect('student.db')  
    cursor = connection.cursor()
    cursor.execute('''  
        CREATE TABLE if not exists student (  
            name TEXT,  
            class TEXT,  
            section TEXT,  
            marks INTEGER  
        ); 
    ''')

    cursor.execute("INSERT INTO student VALUES ('Alice', 'Data Science', 'A', 90)")  
    cursor.execute("INSERT INTO student VALUES ('Bob', 'Data Science', 'B', 85)")  
    cursor.execute("INSERT INTO student VALUES ('Charlie', 'DevOps', 'A', 80)")  
    cursor.execute("INSERT INTO student VALUES ('David', 'DevOps', 'B', 75)")  
    print("Data inserted ")

    connection.commit()  
    connection.close()

# insert_values_in_table() #uncomment for sample database to practise.


