# config.py

HASURA_URL = "http://localhost:9090/v1/graphql" 
HASURA_ADMIN_SECRET = "myadminsecretkey" 
HEADERS = {
    "Content-Type": "application/json",
    "x-hasura-admin-secret": HASURA_ADMIN_SECRET
}


