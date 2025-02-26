
import json
from hasura_connector import HasuraConnector

class SchemaManager:
    @staticmethod
    def fetch_schema():
        introspection_query = """
        query {
            __schema {
                types {
                    name
                    kind
                    fields {
                        name
                        type {
                            name
                            kind
                        }
                    }
                }
            }
        }
        """
        data = HasuraConnector.execute_query(introspection_query)
        return data.get("data", {}).get("__schema", {}).get("types", [])

    @staticmethod
    def format_schema(schema_data):
        formatted_schema = {}
        for table in schema_data:
            if table["kind"] == "OBJECT" and table["fields"]:  # Filter valid tables
                table_name = table["name"]
                columns = [{col["name"]: col["type"]["name"]} for col in table["fields"]]
                formatted_schema[table_name] = columns
        return formatted_schema

    @staticmethod
    def save_schema_to_file(schema_data, file_path="schema.json"):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(schema_data, file, indent=4)
        print(f"Schema saved in {file_path}")

    @staticmethod
    def get_schema():
        schema_data = SchemaManager.fetch_schema()
        formatted_schema = SchemaManager.format_schema(schema_data)
        SchemaManager.save_schema_to_file(formatted_schema)
        return formatted_schema


