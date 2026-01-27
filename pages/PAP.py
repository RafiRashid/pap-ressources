import streamlit as st
from utils.loader import load_markdown

st.markdown(load_markdown("content/presentation/pap.md"),
            unsafe_allow_html=True)
