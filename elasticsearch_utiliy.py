"""
This module contains utility functions to interact with Elasticsearch.
"""

from elasticsearch import Elasticsearch
from settings import ELASTICSEARCH_API_KEY, ELASTICSEARCH_INDEX, ELASTICSEARCH_ENDPOINT
import constants


client = Elasticsearch(
    ELASTICSEARCH_ENDPOINT,
    api_key=ELASTICSEARCH_API_KEY,
)


def create_index():
    """Create an Elasticsearch index if it does not exist."""
    if not client.indices.exists(index=ELASTICSEARCH_INDEX):
        index_body = {
            "mappings": {
                "properties": {
                    "content": {"type": "text"},
                    "embedding": {
                        "type": "dense_vector",
                        "dims": constants.DOCUMENT_CHUNK_VECTOR_DIMENSION
                    }
                }
            }
        }
        client.indices.create(index=ELASTICSEARCH_INDEX, body=index_body)


def store_embedding(content, embedding):
    """Store the content and its vector embedding in Elasticsearch.

    Args:
        content (str): The text content of the document.
        embedding (list(float)): The vector embedding of the content.

    Returns:
        None
    """
    body = {
        "content": content,
        "embedding": embedding
    }
    client.index(index=ELASTICSEARCH_INDEX, body=body)


def search_embeddings(query_embedding, k=5):
    """Search for the top k similar embeddings in elasticsearch index using cosine similarity.

    Args:
        query_embedding (list(float)): The vector embedding of the query.
        k (int): The number of similar embeddings to retrieve.

    Returns:
        list: The list of top k similar embeddings.
    """
    script_query = {
        "script_score": {
            "query": {
                "match_all": {}
            },
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                "params": {
                    "query_vector": query_embedding
                }
            }
        }
    }
    response = client.search(
        index=ELASTICSEARCH_INDEX,
        body={
            "size": k,
            "query": script_query
        }
    )
    return response['hits']['hits']
