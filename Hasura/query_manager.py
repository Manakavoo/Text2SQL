
from hasura_connector import HasuraConnector

class QueryManager:
    @staticmethod
    def get_table_data(table_name: str, limit: int = 10):
        query = f"""
        query {{
            {table_name} (limit: {limit}) {{
                *
            }}
        }}
        """
        data = HasuraConnector.execute_query(query)
        return data.get("data", {}).get(table_name, [])

    @staticmethod
    def get_data_by_filter(table_name: str, column: str, value: str):
        query = f"""
        query ($value: String!) {{
            {table_name} (where: {{ {column}: {{ _eq: $value }} }}) {{
                *
            }}
        }}
        """
        variables = {"value": value}
        data = HasuraConnector.execute_query(query, variables)
        return data.get("data", {}).get(table_name, [])
