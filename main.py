# # main.py  
# import streamlit as st
# import pandas as pd
# from app import read_sql_query, get_gemini_response, get_db_schema , connect_db  , check_postgres_connection , check_mysql_connection , read_postgres_sql

# st.set_page_config(
#     page_title="SQL Query Generator",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# if 'user_question' not in st.session_state:
#     st.session_state.user_question = ""
# if 'generated_query' not in st.session_state:
#     st.session_state.generated_query = None
# if 'query_results' not in st.session_state:
#     st.session_state.query_results = None

# if "db_path" not in st.session_state:
#     st.session_state.db_path = "student.db"
# if "db_connection" not in st.session_state:
#     st.session_state.db_connection = False

# if 'db_data' not in st.session_state:
#     st.session_state.db_data = {}
    
#     st.session_state.db_data["db_type"] = None
#     st.session_state.db_data["db_host"] = None

#     st.session_state.db_data["db_port"] = None
#     st.session_state.db_data["db_name"] = None
#     st.session_state.db_data["db_user"] = None
#     st.session_state.db_data["db_password"] = None

#     st.session_state.db_data["db_schema"] = None



# def generate_sql():
#     db_schema = st.session_state.db_data["db_schema"]
#     response = get_gemini_response(st.session_state.user_question, db_schema)
#     # response = "SELECT   * FROM student;"
#     response = response.strip().replace("sql", "").replace("`", "").replace("\n", " ")

#     st.session_state.generated_query = response
    
# def execute_query():
#     with st.spinner("Executing query..."):
#         if st.session_state.db_type=="SQLite":
#             print("read_sql_query")
#             data = read_sql_query(st.session_state.generated_query, st.session_state.db_data)
#             if data:
#                 st.session_state.query_results = pd.DataFrame(data)
#             else:
#                 st.session_state.query_results = None

#         elif st.session_state.db_type == "PostgreSQL":
#             print("read_postgres_sql")
#             data= read_postgres_sql(st.session_state.generated_query, st.session_state.db_data)
#             st.session_state.query_results = data
#         else:
#             st.session_state.query_results =" No results..."

# st.title("text 2 sql")
# st.markdown("convert user prompts into SQL queries and execute them")

# main_container = st.container()

# with main_container:
#     st.subheader("User generated question")

#     user_input = st.text_area(
#         "What would you like to know about your data?",
#         value="All data",
#         placeholder="e.g., Show me all students with grade above 90",
#         height=100,
#         key="user_question_input",
#     )

#     st.session_state.user_question = user_input
    
#     col1, col2 = st.columns([1, 4])

#     with col1:
#         if st.button("SQL query", use_container_width=True) and st.session_state.user_question:
#             generate_sql()
#         # else:
#         #     st.warning("enter a text to generate a SQL query.")
    
#     if st.session_state.generated_query:
#         st.subheader("generated sql query")
#         st.code(st.session_state.generated_query, language="sql")
        
#         if st.button("Execute", use_container_width=True):
#             execute_query()
    
#         if st.session_state.query_results is not None:
#             st.subheader("Query Results")

#             try:
#                 st.dataframe(
#                 st.session_state.query_results,
#                 use_container_width=True,
#                 hide_index=True
#                 )
#             except Exception as e:
#                 st.write(st.session_state.query_results)
            
#             # st.download_button(
#             #     "Download Results 📥",
#             #     data=st.session_state.query_results.to_csv(index=False),
#             #     file_name="query_results.csv",
#             #     mime="text/csv",
#             #     use_container_width=True
#             # )

# with st.sidebar:
#     st.header("Setup")
    
#     st.subheader("Database Connection")
#     db_type = st.sidebar.selectbox("Select Database Type", ["PostgreSQL","SQLite", "MySQL"])
#     st.session_state.db_type = db_type

#     if db_type == "SQLite":
#         db_name = st.sidebar.text_input("Database Name",value="student.db")

#         st.session_state.db_data["db_type"] = db_type
#         st.session_state.db_data["db_host"] = None  
#         st.session_state.db_data["db_port"] = None
#         st.session_state.db_data["db_name"] = db_name
#         st.session_state.db_data["db_user"] = None
#         st.session_state.db_data["db_password"] = None

#         if st.sidebar.button("Check Connection"):
#             db_status = connect_db(db_name)
#             st.session_state.db_connection = db_status
            
#             st.sidebar.write(db_status)

#     elif db_type == "PostgreSQL":
#         host = st.sidebar.text_input("Host", "localhost")
#         port = st.sidebar.text_input("Port", "5432")
#         dbname = st.sidebar.text_input("Database Name", value='restapi_db')
#         user = st.sidebar.text_input("User", value="postgres")
#         password = st.sidebar.text_input("Password", type="password",value="1234")

#         st.session_state.db_data["db_type"] = db_type
#         st.session_state.db_data["db_host"] = host  
#         st.session_state.db_data["db_port"] = port
#         st.session_state.db_data["db_name"] = dbname
#         st.session_state.db_data["db_user"] = user
#         st.session_state.db_data["db_password"] = password

#         if st.sidebar.button("Check Connection"):
#             print()
#             db_status = check_postgres_connection(host, dbname, user, password, port)
#             st.session_state.db_connection = db_status
#             st.sidebar.write(db_status)

#     elif db_type == "MySQL":
#         host = st.sidebar.text_input("Host", "localhost")
#         port = st.sidebar.text_input("Port", "3306")
#         dbname = st.sidebar.text_input("Database Name")
#         user = st.sidebar.text_input("User")
#         password = st.sidebar.text_input("Password", type="password")

#         st.session_state.db_data["db_type"] = db_type
#         st.session_state.db_data["db_host"] = host  
#         st.session_state.db_data["db_port"] = port
#         st.session_state.db_data["db_name"] = dbname
#         st.session_state.db_data["db_user"] = user
#         st.session_state.db_data["db_password"] = password
        

#         if st.sidebar.button("Check Connection"):
#             db_status = check_mysql_connection(host, dbname, user, password, port)
#             st.session_state.db_connection = db_status
            
#             st.sidebar.write(db_status)
    
#     st.subheader("Database Schema")
#     if st.checkbox("Show Schema") and st.session_state.db_connection:

#         schema_data = get_db_schema(st.session_state.db_data)
#         st.session_state.db_data["db_schema"] = schema_data
#         st.code(schema_data, language="sql") 
#     else:
#         st.write("No schema")

#     st.markdown("---")
#     st.markdown("### About")
#     st.markdown("Convert user text to sql query and execute it.")

import streamlit as st
import pandas as pd
from app import DatabaseManager, QueryGenerator
from streamlit_ace import st_ace


def init_session_state():
    default_values = {
        'user_question': "",
        'generated_query': None,
        'query_results': None,
        'db_connection': False,
        'db_data': {
            'db_type': None,
            'db_host': None,
            'db_port': None,
            'db_name': None,
            'db_user': None,
            'db_password': None,
            'db_schema': None
        }
    }
    
    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

db_manager = DatabaseManager()
query_generator = QueryGenerator()

def generate_sql():
    db_schema = st.session_state.db_data["db_schema"]
    if not db_schema:
        st.error("Please connect to a database and load schema first.")
        return
    
    response = query_generator.generate_query(
        st.session_state.user_question, 
        db_schema
    )
    st.session_state.generated_query = response.strip().replace("sql", "").replace("`", "").replace("\n", " ")

def execute_query():
    with st.spinner("Executing query..."):
        try:
            data = db_manager.execute_query(
                st.session_state.generated_query, 
                st.session_state.db_data
            )
            if isinstance(data, pd.DataFrame) or data:
                st.session_state.query_results = data
            else:
                st.session_state.query_results = None
        except Exception as e:
            st.error(f"Error executing query: {str(e)}")

def render_main_interface():
    st.title("Text to SQL Generator")
    st.markdown("Convert natural language to SQL queries and execute them")

    with st.container():
        st.subheader("User Question")
        user_input = st.text_area(
            "What would you like to know about your data?",
            value=st.session_state.user_question,
            placeholder="eg: Show me all students",
            height=100,
            key="user_question_input"
        )
        st.session_state.user_question = user_input

        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Generate SQL", use_container_width=True) and user_input:
                generate_sql()

        if st.session_state.generated_query:
            st.subheader("Generated SQL Query")
            sql_query = st_ace(value=st.session_state.generated_query, language="sql", theme="monokai", height=100)
            st.session_state.generated_query = sql_query
            st.code(sql_query, language="sql")
            
            if st.button("Execute", use_container_width=True):
                execute_query()

            if st.session_state.query_results is not None:
                st.subheader("Query Results")
                try:
                    if isinstance(st.session_state.query_results, pd.DataFrame):
                        st.dataframe(
                            st.session_state.query_results,
                            use_container_width=True,
                            hide_index=True
                        )
                    else:
                        st.write(st.session_state.query_results)
                except Exception as e:
                    st.error(f"Error displaying results: {str(e)}")

def render_sidebar():
    with st.sidebar:
        st.header("Database Configuration")
        
        db_type = st.selectbox(
            "Select Database Type", 
            ["SQLite", "PostgreSQL", "MySQL"],
            key="db_type_select"
        )
        st.session_state.db_data["db_type"] = db_type

        # Get connection details based on database type
        connection_details = db_manager.get_connection_form(db_type)
        
        # Update session state with form values
        for field, value in connection_details.items():
            st.session_state.db_data[field] = value

        if st.button("Test Connection"):
            connection_status = db_manager.test_connection(st.session_state.db_data)
            st.session_state.db_connection = connection_status.get('success', False)
            if connection_status['success']:
                st.success(connection_status['message'])
            else:
                st.error(connection_status['message'])

        st.subheader("Database Schema")
        if st.checkbox("Show Schema") and st.session_state.db_connection:
            schema_data = db_manager.get_schema(st.session_state.db_data)
            if schema_data.get('success'):
                st.session_state.db_data["db_schema"] = schema_data['schema']
                st.code(schema_data['schema'], language="sql")
            else:
                st.error(schema_data['message'])

        st.markdown("---")
        st.markdown("### About")
        st.markdown("Convert natural language to SQL queries and execute them.")
        
st.set_page_config(
    page_title="SQL Query Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)
def main():
    render_main_interface()
    render_sidebar()

if __name__ == "__main__":
    main()