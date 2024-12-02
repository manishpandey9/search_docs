"""
Handle document ingestion in elasticsearch.
"""
import fitz


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file while preserving the document structure.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def chunk_text(text, words_per_chunk=100):
    """Create around 100 words chunks from the text without losing sentence semantics.

    Args:
        text (str): The text to be chunked.
        words_per_chunk (int): The maximum number of words per chunk.

    Returns:
        list: The list of text chunks.
    """
    import nltk
    nltk.download('punkt', quiet=True)
    from nltk.tokenize import sent_tokenize, word_tokenize

    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ''
    current_chunk_word_count = 0

    for sentence in sentences:
        sentence_word_count = len(word_tokenize(sentence))

        if current_chunk_word_count + sentence_word_count <= words_per_chunk:
            if current_chunk:
                current_chunk += ' ' + sentence
            else:
                current_chunk = sentence
            current_chunk_word_count += sentence_word_count
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = sentence
            current_chunk_word_count = sentence_word_count

    if current_chunk:
        chunks.append(current_chunk)

    return chunks
