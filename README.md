# Medical RAG Chatbot

An AI-powered **Medical Retrieval-Augmented Generation (RAG) Chatbot** that answers clinical and medical questions by retrieving relevant information from an encyclopedia PDF and generating contextually accurate responses using Cohere LLMs, LangChain, and ChromaDB.

This project is designed with industry best practices: a modular backend API using FastAPI and a Python-based interactive frontend using Streamlit.

## Features

- **Accurate medical question answering** leveraging RAG techniques.
- **PDF ingestion and vector database** creation for document retrieval.
- **Session-based chat history** allowing users to track previous queries and answers.
- **Backend logging** for enhanced debugging and monitoring.
- **Interactive and easy-to-use Streamlit frontend**.
- Clear **frontend-backend separation** for maintainability and scalability.

## Project Structure

medical-rag-chatbot/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── rag_engine.py
│   │   ├── pdf_ingest.py
│   │   ├── config.py
│   ├── requirements.txt
├── frontend/
│   ├── medical_chatbot_streamlit.py
│   ├── requirements.txt
├── .env
├── README.md


## Prerequisites

- Python 3.8 or higher
- [Cohere API Key](https://cohere.ai/)
- The medical encyclopedia PDF file (e.g., `Encyclopedia of Medicine.pdf`)

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Chakri-iitg/Medical_RAG_Chatbot.git
cd medical-rag-chatbot


### 2. Backend Setup

cd backend
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt


- Create a `.env` file in the `backend/` folder with:

COHERE_API_KEY=your_cohere_api_key_here
PDF_PATH=/absolute/path/to/Encyclopedia of Medicine.pdf


- Start the backend server:

uvicorn app.main:app --reload


By default, the API runs at `http://localhost:8000`.

### 3. Frontend Setup

From the root directory:

cd frontend
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt


- Run the Streamlit app:

streamlit run medical_chatbot_streamlit.py


- The frontend will open in your browser (usually at `http://localhost:8501`).

## Usage

- Enter a medical question in the input box.
- Click **Ask** to receive an answer sourced from the provided medical encyclopedia PDF.
- View the response, source text, and your chat history within the interface.
- Use **Clear chat** to reset the conversation.

## Code Highlights

- `backend/app/rag_engine.py`: Handles PDF ingestion, text chunking, embedding, and query retrieval using ChromaDB and Cohere.
- `backend/app/main.py`: FastAPI defines REST APIs to process user queries and manage session histories.
- `frontend/medical_chatbot_streamlit.py`: Streamlit app manages user input, sessions, and displays chat history interacting with backend APIs.

## Future Improvements

- Support PDF upload via UI
- User authentication and role-based access
- Persistent chat history storage (database/Redis)
- Enhanced UI styling and accessibility
- Deployment with Docker for production readiness

## Troubleshooting

- Ensure your Cohere API key is valid and set in the `.env`
- Confirm the PDF path is correct and accessible
- Backend errors and info logs appear in the terminal running `uvicorn`
- Frontend network errors usually indicate backend is not running or incorrect URL

## License

This project is licensed under the MIT License.

## Contact

For questions or contributions, please contact [your email or GitHub profile].

*Thank you for using the Medical RAG Chatbot!*

