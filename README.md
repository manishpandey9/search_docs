# **search_docs**  
### *Simple RAG-Based Document Search*

This project demonstrates how to build a semantic search system using OpenAI models and Elasticsearch. It extracts text from documents, generates embeddings using OpenAI, stores these embeddings in Elasticsearch, and retrieves semantically relevant results based on user queries.

---

## **Setup**

- Run the following command to setup the project
  ```bash
  pip install -r requirements.txt

- Make sure elasticsearch is setup on your system

## **Key Features**

### **Document Processing**
- Extract text from a PDF document.
- Split the text into manageable chunks for embedding making sure semantic meanings are reatained in chunks.

### **Embedding Generation**
- Generate embeddings for each chunk using OpenAI models.

### **Elasticsearch Integration**
- Store embeddings in an Elasticsearch index.
- Perform efficient semantic searches on stored embeddings.

### **Interactive Search**
- Accept user queries.
- Generate an embedding for the query using OpenAI.
- Search Elasticsearch to retrieve semantically similar results.

---

## **Working**

1. **Configuration**:
   - Update the necessary variables in the `settings.py` file according to your environment and needs.

2. **Indexing a PDF Document**:
   - Run the following command to process and index a PDF file:
   ```bash
   python main.py --pdf /path/to/your/document.pdf



Future Scopes:-
1. Improve the chunking methodologies to retain the sematic meanings.
2. Multi-Document Support