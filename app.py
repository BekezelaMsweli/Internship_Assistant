import streamlit as st
import pandas as pd
from difflib import get_close_matches

st.set_page_config(
    page_title="Internship Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

faq = pd.read_csv("data/faq.csv", sep=";")


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
    Bekezela Bongumusa Msweli
    """)

st.title("🤖 Internship Knowledge Assistant")

st.info(
    "Ask questions about internship procedures, ICT support, HR processes, and office guidelines."
)

question = st.text_input(
    "💬 Ask a Question:",
    placeholder="Example: How do I apply for leave?"
)

# Search FAQ
if question:

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

        st.success("Answer Found")

        st.markdown(f"""
        ### ✅ Answer

        {answer}
        """)

    else:

        st.warning(
            "I couldn't find an answer. Please consult your supervisor."
        )