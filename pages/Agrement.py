import streamlit as st
from utils.loader import load_markdown

st.markdown(load_markdown("content/fiches/agrement.md"),
            unsafe_allow_html=True)
