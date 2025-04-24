# 🔄 Contentful to Elasticsearch Sync

This script fetches entries from a specified Contentful content type and indexes them into an Elasticsearch cluster.

---

## 📦 Requirements

- Python 3.7+
- [Elasticsearch](https://www.elastic.co/elasticsearch/)
- [Contentful space and access token](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- Environment variables set in a `.env` file

---

## 🛠 Installation

```bash
# Clone the repo
git clone https://github.com/jabercrombia/contentful-to-elasticsearch.git
cd contentful-to-elasticsearch

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
