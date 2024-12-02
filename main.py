"""
Entry point for the QA System for PDFs.
"""

import ingest_docs
import elasticsearch_utiliy
import embedding_utility
import query_processors


def index_pdf(pdf_file_path):
    """Create embeddings for the chunks of text extracted from the PDF and store them in Elasticsearch."""
    text = ingest_docs.extract_text_from_pdf(pdf_file_path)
    chunks = ingest_docs.chunk_text(text)
    elasticsearch_utiliy.create_index()

    for chunk in chunks:
        embedding = embedding_utility.get_embedding(chunk)
        elasticsearch_utiliy.store_embedding(chunk, embedding)


def interactive_question_answering():
    """Answer questions interactively using the indexed PDF."""
    print("\nPlease enter 'exit' to quit the program.\n")
    while True:
        try:
            question = input("Ask a question Relevant to PDF Provided: ")
            if question.lower() == 'exit':
                print("Exiting the program.")
                break
            answer = query_processors.process_query(question)
            print(f"Answer: {answer}\n")
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='QA System for PDFs')
    parser.add_argument('--pdf', required=True, help='Pdf file path')
    args = parser.parse_args()

    # Index the PDF file
    print("Processing the PDF file. This may take a few moments...")
    index_pdf(args.pdf)
    print("Processing completed.")

    # Interactive Question Answering
    interactive_question_answering()
