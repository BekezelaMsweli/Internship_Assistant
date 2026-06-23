import streamlit as st
import pandas as pd
from difflib import get_close_matches

st.set_page_config(
    page_title="Interns Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

faq = pd.read_csv("data/faq.csv", sep=";")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    color: #0066cc;
}

.stTextInput > div > div > input {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


with st.sidebar:

    st.title("🤖 Menu")

    st.markdown("""
    ### About

    Internship Knowledge Assistant

    **Version:** 1.0

    **Developed by:**  
    Bekezela Msweli
    """)
    
    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

st.title("🤖 Interns Knowledge Assistant")

st.info(
    "Ask questions about internship procedures, ICT support, HR processes, and office guidelines."
)

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
question = st.chat_input(
    "💬 Ask a Question...",
)

# Search FAQ
if question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)
        
    questions = faq["Question"].tolist()

    match = get_close_matches(
        question,
        questions,
        n=1,
        cutoff=0.3
    )

    if match:

        answer = faq.loc[
            faq["Question"] == match[0],
            "Answer"
        ].values[0]

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
          {
            "role": "assistant",
            "content": answer
           }
        )
    
        

    else:
        answer = (
            "I couldn't find an answer. "
            "Please consult your supervisor."
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )
