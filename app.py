# #app.py
# import streamlit as st
# import sqlite3
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai
# import warnings
# import psycopg2
# import mysql.connector

# warnings.filterwarnings("ignore")
# load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_PRO_API_KEY"))

# class Db_configure():
#     pass

    
# def connect_db(db_path=""):
#      try:
#         conn = sqlite3.connect(db_path)
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM student") 
#         conn.close()
#         return True
#      except Exception as e:
#         return False
     
# def check_postgres_connection(host, dbname, user, password, port):
#     try:
#         conn = psycopg2.connect(
#             host=host, database=dbname, user=user, password=password, port=port
#         )
#         conn.cursor().execute("SELECT 1")
#         conn.close()
#         return "Connection successful!"
#     except Exception as e:
#         return f"Error: {e}"
    
# def check_mysql_connection(host, dbname, user, password, port):
#     try:
#         conn = mysql.connector.connect(
#             host=host, database=dbname, user=user, password=password, port=port
#         )
#         conn.cursor().execute("SELECT 1")
#         conn.close()
#         return "Connection successful!"
#     except Exception as e:
#         return f"Error: {e}"

# def get_db_schema(db_data={}):

#     if not db_data:
#         return "No data provided"
    
#     if db_data["db_type"]=="SQLite":
#         try:
#             conn = sqlite3.connect(db_data["db_name"])
#             cursor = conn.cursor()
#             schema_data=get_schema_details(cursor,db_data["db_type"])
#             cursor.close()
#             return schema_data
#         except Exception as e:
#             return f"Error reading schema: {str(e)}"
        
#     elif db_data["db_type"]=="PostgreSQL":
#         print("POstgres..")
#         try:
#             conn = psycopg2.connect(
#                 host=db_data["db_host"], database=db_data["db_name"], user=db_data["db_user"], password=db_data["db_password"], port=db_data["db_port"]
#             )
#             print("Connected..")
#             cursor= conn.cursor()
#             schema_data=get_schema_details(cursor,db_data["db_type"])
#             print("Schema extracted..")
#             cursor.close()
#             return schema_data
#         except Exception as e:
#             return f"Error reading schema: {str(e)}"
#     else:
#         try:
#             conn = mysql.connector.connect(
#             host=db_data["db_host"], database=db_data["db_name"], user=db_data["db_user"], password=db_data["db_password"], port=db_data["db_port"]
#             )
#             cursor= conn.cursor()
#             schema_data=get_schema_details(cursor,db_data["db_type"])
#             cursor.close()
#             return schema_data
#         except Exception as e:
#             return f"Error reading schema: {str(e)}"
        

# def get_schema_details(cursor, db_type):
    
#     try:
#         if db_type == "SQLite":
#             cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#         elif db_type == "PostgreSQL":
#             cursor.execute("""
#             SELECT table_name, column_name, data_type
#             FROM information_schema.columns
#             WHERE table_schema = 'public'
#             ORDER BY table_name, ordinal_position;
#             """)
#             schema_data = cursor.fetchall()
#             schema = []
#             table_columns = {}

#             for table_name, column_name, data_type in schema_data:
#                 if table_name not in table_columns:
#                     table_columns[table_name] = []
#                 table_columns[table_name].append(f"    - {column_name} ({data_type})")

#             for table_name, columns in table_columns.items():
#                 schema.append(f"\n  Table: {table_name}\n" + "\n".join(columns))

#             return "\n".join(schema)
        
#         elif db_type == "MySQL":
#             cursor.execute("SHOW TABLES;")
#         tables = cursor.fetchall()
        
#         schema = []
#         for table in tables:
#             table_name = table[0]
#             cursor.execute(f"PRAGMA table_info({table_name});")
#             columns = cursor.fetchall()
            
#             columns_info = [f"    - {col[1]} ({col[2]})" for col in columns]
#             table_schema = f"\n  Table: {table_name}\n" + "\n".join(columns_info)
#             schema.append(table_schema)

#             return "\n".join(schema)


#     except Exception as e:
#         return f"Error fetching schema details: {e}"

# def get_gemini_response(question, prompt):
#     model = genai.GenerativeModel("gemini-pro")
#     print("Model Loaded")

#     response = model.generate_content(prompt + "\n\nUser Question: " + question)
#     print("Response Generated\n")
#     return response.text

# def read_sql_query(query, data):
    
#     print("SQL query: ",query)
#     try:
#         conn = sqlite3.connect(data["db_name"])
#         print("connected to database")
#         cur = conn.cursor()
#         cur.execute(query)
#         rows = cur.fetchall()
#         print("query executed")
#         conn.close()
#         print("Rows",rows)
#         return rows
    
#     except Exception as e:
#         st.error(f"Error executing query: {str(e)}")
#         print("Error occured.../")
#         return []

# def read_postgres_sql(query, data):
#     try:
#         conn = psycopg2.connect(
#             host=data["db_host"], database=data["db_name"], user=data["db_user"], password=data["db_password"], port=data["db_port"]
#         )
#         cursor = conn.cursor()
#         cursor.execute(query)
#         rows = cursor.fetchall()
#         print("query executed")
#         cursor.close()
#         conn.close()
#         print("Rows",rows)
#         return rows
    
#     except Exception as e:
#         return f"Error: {e}"

# def get_complete_prompt(db_path="student.db"):
#     schema = get_db_schema(db_path)

#     return f"""
#         You are an expert SQL assistant. You will help users write SQL queries that are efficient, secure and follow best practices.

#         Database Schema:
#         {schema}

#         Rules to follow:
#         1. Only write standardized SQL that works across major databases
#         2. Convert English questions into SQL queries based on the above schema
#         3. Add proper indexing suggestions when relevant
#         4. Use clear aliases and formatting
#         5. Consider performance implications
#         6. Avoid SQL injection risks
#         7. Include error handling where needed
#         8. SQL code should not have any syntax errors
#         9. Do not begin or end with any ``` or any other special characters
#         10. Only use tables and columns that exist in the schema above

#         Important note : Don't mention sql in your response , provide me a only sql query

#         Please provide only the SQL query without any explanations unless specifically asked for details.
#         """

import os
from typing import Dict, Any, Optional
import pandas as pd
import sqlite3
import psycopg2
import mysql.connector
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from contextlib import contextmanager

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_PRO_API_KEY"))

class DatabaseManager:
    def __init__(self):
        self.connections = {}
    
    @contextmanager
    def get_connection(self, db_data: Dict[str, Any]):
        """Context manager for database connections"""
        db_type = db_data['db_type']
        conn_key = f"{db_type}_{db_data.get('db_name')}_{db_data.get('db_host')}"
        
        try:
            if conn_key not in self.connections:
                self.connections[conn_key] = self._create_connection(db_data)
            
            yield self.connections[conn_key]
        except Exception as e:
            raise e
        finally:
            pass  
    
    def _create_connection(self, db_data: Dict[str, Any]):
        """Create a new database connection"""
        try:
            if db_data['db_type'] == "SQLite":
                return sqlite3.connect(db_data['db_name'])
            elif db_data['db_type'] == "PostgreSQL":
                return psycopg2.connect(
                    host=db_data['db_host'],
                    database=db_data['db_name'],
                    user=db_data['db_user'],
                    password=db_data['db_password'],
                    port=db_data['db_port']
                )
            elif db_data['db_type'] == "MySQL":
                return mysql.connector.connect(
                    host=db_data['db_host'],
                    database=db_data['db_name'],
                    user=db_data['db_user'],
                    password=db_data['db_password'],
                    port=db_data['db_port']
                )
        except Exception as e:
            raise ConnectionError(f"Failed to connect to database: {str(e)}")

    def get_connection_form(self, db_type: str) -> Dict[str, Any]:
        """Get connection form fields based on database type"""
        if db_type == "SQLite":
            return {
                'db_name': st.sidebar.text_input("Database Name", value="student.db"),
                'db_host': None,
                'db_port': None,
                'db_user': None,
                'db_password': None
            }
        else:
            return {
                'db_host': st.sidebar.text_input("Host", "localhost"),
                'db_port': st.sidebar.text_input("Port", "5432" if db_type == "PostgreSQL" else "3306"),
                'db_name': st.sidebar.text_input("Database Name", value='restapi_db'),
                'db_user': st.sidebar.text_input("User", value="postgres"),
                'db_password': st.sidebar.text_input("Password", type="password", value="1234")
            }

    def test_connection(self, db_data: Dict[str, Any]) -> Dict[str, Any]:
        """Test database connection"""
        try:
            with self.get_connection(db_data) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                return {'success': True, 'message': "Connection successful!"}
        except Exception as e:
            return {'success': False, 'message': f"Connection failed: {str(e)}"}

    def get_schema(self, db_data: Dict[str, Any]) -> Dict[str, Any]:
        """Get database schema"""
        try:
            with self.get_connection(db_data) as conn:
                cursor = conn.cursor()
                schema = self._get_schema_details(cursor, db_data['db_type'])
                return {'success': True, 'schema': schema}
        except Exception as e:
            return {'success': False, 'message': f"Failed to get schema: {str(e)}"}

    def _get_schema_details(self, cursor, db_type: str) -> str:
        """Get detailed schema information"""
        schema = []
        
        try:
            if db_type == "SQLite":
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                
                for table in tables:
                    table_name = table[0]
                    cursor.execute(f"PRAGMA table_info({table_name});")
                    columns = cursor.fetchall()
                    schema.append(self._format_table_schema(table_name, columns, 'sqlite'))
                    
            elif db_type == "PostgreSQL":
                cursor.execute("""
                    SELECT table_name, column_name, data_type
                    FROM information_schema.columns
                    WHERE table_schema = 'public'
                    ORDER BY table_name, ordinal_position;
                """)
                schema_data = cursor.fetchall()
                schema.extend(self._format_postgres_schema(schema_data))
                
            elif db_type == "MySQL":
                cursor.execute("SHOW TABLES;")
                tables = cursor.fetchall()
                
                for table in tables:
                    table_name = table[0]
                    cursor.execute(f"SHOW COLUMNS FROM {table_name};")
                    columns = cursor.fetchall()
                    schema.append(self._format_table_schema(table_name, columns, 'mysql'))
            
            return "\n".join(schema)
        except Exception as e:
            raise Exception(f"Error fetching schema details: {str(e)}")

    def _format_table_schema(self, table_name: str, columns: list, db_type: str) -> str:
        """Format table schema based on database type"""
        if db_type == 'sqlite':
            columns_info = [f"    - {col[1]} ({col[2]})" for col in columns]
        elif db_type == 'mysql':
            columns_info = [f"    - {col[0]} ({col[1]})" for col in columns]
        else:
            columns_info = [f"    - {col[1]} ({col[2]})" for col in columns]
            
        return f"\n  Table: {table_name}\n" + "\n".join(columns_info)

    def _format_postgres_schema(self, schema_data: list) -> list:
        """Format PostgreSQL schema data"""
        table_columns = {}
        for table_name, column_name, data_type in schema_data:
            if table_name not in table_columns:
                table_columns[table_name] = []
            table_columns[table_name].append(f"    - {column_name} ({data_type})")
        
        return [f"\n  Table: {table_name}\n" + "\n".join(columns) 
                for table_name, columns in table_columns.items()]

    def execute_query(self, query: str, db_data: Dict[str, Any]) -> Optional[pd.DataFrame]:
        """Execute SQL query and return results as DataFrame"""
        try:
            with self.get_connection(db_data) as conn:
                cursor = conn.cursor() 
                query_validation=self.validate_sql(cursor,query,db_data["db_type"])
                if not query_validation["success"]:
                    # cursor.close()
                    # conn.commit()  # Commit changes if needed
                    # conn.close()
                    return query_validation["Msg"]
                
                cursor.execute(query)
                if cursor.description:
                    columns = [desc[0] for desc in cursor.description]
                    rows = cursor.fetchall()

                    # cursor.close()
                    # conn.commit()  
                    # conn.close()
                
                    if rows:
                        return pd.DataFrame(rows, columns=columns)
                    else:
                        return "No result data"
                else:
                    # cursor.close()
                    # conn.commit()  
                    # conn.close()
                    if "insert" in query.lower():
                        return " Data inserted sucessfully.."
                    elif "create" in query.lower():
                        return "Table created Sucessfully.."
                    elif "update" in query.lower():
                        return "Data updated Sucessfully.."
                    
                return None
        except Exception as e:
            if str(e)=="You can only execute one statement at a time":
                return "Multiple queries "
            raise Exception(f"Query execution failed: {str(e)}")
        finally:
            pass
            # cursor.close() 
            # conn.close()
    
    def validate_sql(self, cursor, query,db_type):
        """Validates if an SQL query is syntactically correct without execution."""
        try:
            if db_type == "PostgreSQL" or db_type == "MySQL":
                cursor.execute(f"EXPLAIN {query}")
            elif db_type == "SQLite":
                cursor.execute(f"EXPLAIN QUERY PLAN {query}")

            return {"success": True, "Msg": "SQL query is valid."}
        
        except Exception as e:
            return {"success": False, "Msg": f"Invalid SQL: {str(e)}"}

class QueryGenerator:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-pro")

    def generate_query(self, question: str, schema: str) -> str:
        """Generate SQL query from natural language question"""
        prompt = self._get_prompt_template(schema)
        # return "DELETE FROM teacher;"
        return "SELECT   name FROM   Student;"
        # response = self.model.generate_content(prompt + "\n\nUser Question: " + question)
        # return response.text

    def _get_prompt_template(self, schema: str) -> str:
        """Get the prompt template for query generation"""
        return f"""
        You are an expert SQL assistant. You will help users write SQL queries that are efficient, secure and follow best practices.

        Database Schema:
        {schema}

        Rules to follow:
        1. Only write standardized SQL that works across major databases
        2. Convert English questions into SQL queries based on the above schema
        3. Add proper indexing suggestions when relevant
        4. Use clear aliases and formatting
        5. Consider performance implications
        6. Avoid SQL injection risks
        7. Include error handling where needed
        8. SQL code should not have any syntax errors
        9. Do not begin or end with any ``` or any other special characters
        10. Only use tables and columns that exist in the schema above

        Important note: Don't mention sql in your response, provide only the SQL query

        Please provide only the SQL query without any explanations unless specifically asked for details.
        """