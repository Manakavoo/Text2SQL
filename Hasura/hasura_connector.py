# hasura_connector.py

import requests
from config import HASURA_URL, HEADERS

class HasuraConnector:

    @staticmethod
    def execute_query(query: str, variables: dict = None):
        payload = {"query": query, "variables": variables or {}}
        response = requests.post(HASURA_URL, json=payload, headers=HEADERS)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.text}")
