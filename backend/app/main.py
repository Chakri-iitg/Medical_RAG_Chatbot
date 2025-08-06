import logging
from fastapi import FastAPI, Request
from .rag_engine import answer_user_query
from uuid import uuid4

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

chat_histories = {}
@app.post("/api/ask")
async def ask_question(request: Request):

    data = await request.json()

    query = data.get("query", "")

    session_id = data.get("query", "")

    if not session_id:
        session_id = str(uuid4)
        logger.info(f"New Session: {session_id}")

    logger.info(f"Query received: {query} (session: {session_id})")

    if not query:
        logger.warning("No query provided")
        return {"error": "Query missing"}

    response, sources = answer_user_query(query)

    if session_id not in chat_histories:
        chat_histories[session_id] = []
    
    chat_histories[session_id].append({
        "query" : query,
        "response": response,
        "sources": sources
    })

    logger.info(f"Returning response for session {session_id}")
    return {
        "response":response, 
        "sources": sources,
        "session_id": session_id,
        "history": chat_histories[session_id]
        }

@app.post("/api/history")

async def get_history(request: Request):

    data = await request.json()
    session_id = data.get("session_id", None)
    logger.info(f"History requested for session: {session_id}")
    if not session_id or session_id not in chat_histories:
        return {"history": [], "session_id": session_id}

    return {"history": chat_histories[session_id], "session_id":session_id}
