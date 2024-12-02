"""
Here we define the constants that are used in the project.
"""


DOCUMENT_CHUNK_VECTOR_DIMENSION = 1024

SYSTEM_PROMPT = """
You are a helpful assistant that answers questions based on the provided context.

Output JSON Format:
{
"question": "What is the capital of Heaven?",
"answer": "The capital of Heaven is Paradise City."
}

If the answer can not be found put answer as "Data Not Available"
like this:

JSON Output:
{
"question": "What is the capital of Heaven?",
"answer": "Data Not Available"
}
"""
