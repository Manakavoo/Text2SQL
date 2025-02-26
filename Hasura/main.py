# main.py

from schema_manager import SchemaManager
from query_manager import QueryManager

if __name__ == "__main__":
    print("Fetching and saving schema...")
    schema = SchemaManager.get_schema()

    print("\nFetching sample data from 'users' table...")
    user_data = QueryManager.get_table_data("users", limit=5)
    print(user_data)

    print("\nFetching data by filter (email = 'test@example.com')...")
    filtered_data = QueryManager.get_data_by_filter("users", "email", "test@example.com")
    print(filtered_data)
