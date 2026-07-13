import streamlit as st
from rag import get_answer

st.set_page_config(
    page_title="YouTube Chatbot",
    page_icon=":robot:"
)

st.title("YouTube Chatbot")

youtube_url = st.text_input(
    "Enter YouTube URL"
)

question = st.text_input(
    "Ask a question"
)

if st.button("Generate Answer"):

    if youtube_url == "" or question == "":
        st.warning("Please enter both fields.")

    else:

        with st.spinner("Generating answer..."):

            answer = get_answer(
                youtube_url,
                question
            )

        st.success("Done!")

        st.write(answer)