import os

from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.environ.get("COHERE_API_KEY")

PDF_PATH = os.environ.get("PDF_PATH","Encyclopedia of Medicine.pdf")

CHROMA_COLLECTION_NAME = "info_medical"