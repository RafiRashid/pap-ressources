import streamlit as st
from utils.loader import load_markdown
from utils.search import parse_definitions

markdown = load_markdown("content/glossaire.md")
definitions = parse_definitions(markdown)

query = st.text_input("Rechercher un terme")

if query:
    results = {k: v for k, v in definitions.items() if query.lower() in k}

    for term, definition in results.items():
        st.markdown(f"### **{term.capitalize()}**")
        st.markdown(definition)
else:
    st.markdown(markdown)
