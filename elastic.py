import os
from dotenv import load_dotenv
import contentful
from elasticsearch import Elasticsearch

# Load env vars
load_dotenv()

SPACE_ID = os.getenv("CONTENTFUL_SPACE_ID")
ACCESS_TOKEN = os.getenv("CONTENTFUL_ACCESS_TOKEN")
ES_HOST = os.getenv("ELASTICSEARCH_HOST")
ES_USER = os.getenv("ES_USER")
ES_PASS = os.getenv("ES_PASSWORD")
INDEX_NAME = os.getenv("INDEX_NAME")
CONTENT_TYPE="projects"
# Init Contentful client
client = contentful.Client(SPACE_ID, ACCESS_TOKEN)

# Init Elasticsearch client
es = Elasticsearch(
    ES_HOST,
    basic_auth=(ES_USER, ES_PASS),
    verify_certs=False
)

entries = client.entries({'content_type': CONTENT_TYPE})

# Fetch entries from Contentful
# entries = client.entries()

# Index each entry into Elasticsearch
for entry in entries:
    doc = {
        "title": getattr(entry, "title", "Untitled"),
        "content": getattr(entry, "description", ""),
        "content_type": entry.sys.get("content_type", {}).id if hasattr(entry, 'sys') else "unknown",
    }
    print(f"Indexing: {doc['title']}")
    es.index(index=INDEX_NAME, id=entry.sys.get("id"), document=doc)

print("✅ Sync complete.")
