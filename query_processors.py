from embedding_utility import get_embedding
from elasticsearch_utiliy import search_embeddings
import openai
import settings
import constants
import json

client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_answer(question, context):
    """Give LLM generated answer for the question based on the context."""
    try:
        messages = [
            {"role": "system", "content": constants.SYSTEM_PROMPT},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}\n\nAnswer according to the context. If the answer cannot be found in the context."}
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=500,
        )

        answer = response.choices[0].message.content
        return json.loads(answer)

    except Exception as e:
        print(f"Error generating answer: {e}")
        return "Data Not Available"


def process_query(question):
    question_embedding = get_embedding(question)
    search_results = search_embeddings(question_embedding)

    if not search_results:
        return "Data Not Available"

    contexts = [hit['_source']['content'] for hit in search_results]
    combined_context = "\n\n".join(contexts)
    answer = generate_answer(question, combined_context)
    return answer
