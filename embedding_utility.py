"""Utility functions for working with embeddings."""

import openai
import time
import constants
import settings


def get_embedding(text, model="text-embedding-3-small"):
    """Get the embedding of a text using the OpenAI Embedding API."""
    max_retries = 3
    client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
    for retry in range(max_retries):
        try:
            response = client.embeddings.create(
                input=[text],
                model=model,
                dimensions=constants.DOCUMENT_CHUNK_VECTOR_DIMENSION
            )
            embedding = response.data[0].embedding
            return embedding
        except Exception as e:
            if retry < max_retries - 1:
                time.sleep(2 ** retry)
            else:
                raise e
