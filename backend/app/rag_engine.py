import logging
from .config import COHERE_API_KEY, PDF_PATH, CHROMA_COLLECTION_NAME
from .pdf_ingest import get_pdf_texts
from langchain.text_splitter import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import cohere

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_chromadb():

    logger.info(f"Loading PDF: {PDF_PATH}")
    pdf_texts = get_pdf_texts(PDF_PATH)

    char_splitter = RecursiveCharacterTextSplitter(
        separators = ["\n\n", "\n", ". ", " ",""],
        chunk_size = 1000,
        chunk_overlap = 0,
    
    )

    char_split_texts = char_splitter.split_text('\n\n'.join(pdf_texts))
    token_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=0,tokens_per_chunk=256)
    token_split_texts = []

    for text in char_split_texts:
        token_split_texts += token_splitter.split_text(text)
    
    logger.info(f"Total chunks: {len(token_split_texts)}")
    # Embedding and Vector DB

    embedding_function = SentenceTransformerEmbeddingFunction()
    chroma_client = chromadb.Client()

    collection = chroma_client.create_collection(CHROMA_COLLECTION_NAME, embedding_function=embedding_function)

    ids = [str(i) for i in range(len(token_split_texts))]
    collection.add(ids=ids, documents=token_split_texts)

    return collection

chroma_collection = setup_chromadb()
co = cohere.Client(COHERE_API_KEY)

def answer_user_query(query):

    try:

        logger.info(f"RAG: Searching for: {query}")
        results = chroma_collection.query(query_texts=[query], n_results=5)
        docs = results['documents'][0]

        # Generation

        messages = [
            {
                "role":"system",
                "content":"""You are a helpful expert medical research assistant. Your users are asking questions about information contained in an annual report.
                             You will be shown the user's question and the relevant information from Encyclopedia od Medicine. Answer the user's question using only
                             this information.
                           """
            },
            {
                "role":"user",
                "content":f"Question:{query}\nInformation:{chr(10).join(docs)}"

            },
        ]

        response = co.chat(
            model = "command",
            message=query,
            documents=messages
        )

        logger.info("RAG: Response generated")
        return response.text, docs

    
    except Exception as e:

        return f"Error: {str(e)}",""
