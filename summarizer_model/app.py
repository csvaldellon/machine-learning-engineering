import streamlit as st
from summarizer import summarize_text


def main():
    st.title("Text Summarizer")

    text = st.text_area("Enter text to summarize")

    if st.button("Summarize"):
        if text:
            summarized_text = summarize_text(text)
            st.subheader("Original Text")
            st.write(text)

            st.subheader("Summarized Text")
            st.write(summarized_text)
        else:
            st.warning("Please enter some text to summarize")


if __name__ == "__main__":
    main()
