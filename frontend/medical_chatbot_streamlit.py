import streamlit as st
import requests
import uuid

BACKEND_URL = "http://localhost:8000"

if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("Medical Research Assistant Chatbot")

with st.form("chat_form", clear_on_submit=True):
    query = st.text_area("Ask a medical question", height= 60)
    submitted = st.form_submit_button("Ask")

if submitted and query.strip():
    resp = requests.post(
        f"{BACKEND_URL}/api/ask",
        json = {"query": query.strip(), "session_id": st.session_state.session_id}
    )

    data = resp.json()

    st.session_state.session_id = data.get("session_id", st.session_state.session_id)
    st.session_state.chat_history = data.get("history", [])

st.subheader("Chat History")

if st.session_state.chat_history:

    for idx, item in enumerate(st.session_state.chat_history):
        st.markdown(f"**Q{idx+1}:** {item['query']}")
        st.markdown(f"**A{idx+1}:** {item['response']}")
        with st.expander(f"Show Source (Q{idx+1})"):
            for src in item.get("sources",[]):
                st.markdown(f"<div style = 'background:#f7afd; padding:7px;border-radius:4px'>{src}</div>",unsafe_allow_html=True)

if st.button("Clear Chat"):
    st.session_state.chat_history = []