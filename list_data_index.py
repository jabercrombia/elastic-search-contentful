from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

# Replace with your actual credentials and host
ES_HOST = os.getenv("ELASTICSEARCH_HOST")
ES_USER = os.getenv("ES_USER")
ES_PASSWORD = os.getenv("ES_PASSWORD")
INDEX_NAME = os.getenv("INDEX_NAME")

# Initialize Elasticsearch client with authentication
es = Elasticsearch(
    ES_HOST,
    basic_auth=(ES_USER, ES_PASSWORD),  # Basic authentication with username and password
    verify_certs=False  # Disable SSL verification if using localhost (optional)
)

# Query to retrieve all records from the index
response = es.search(index=INDEX_NAME, body={
    "query": {
        "match_all": {}
    },
    "size": 10  # Limit to the first 10 records
})

# Print out the results
for hit in response['hits']['hits']:
    print(hit['_source'])
