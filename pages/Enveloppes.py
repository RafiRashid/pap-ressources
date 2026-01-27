import streamlit as st
from utils.loader import load_markdown

st.markdown(load_markdown("content/fiches/enveloppes.md"),
            unsafe_allow_html=True)
