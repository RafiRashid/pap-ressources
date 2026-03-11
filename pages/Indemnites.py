import streamlit as st
from utils.loader import load_markdown

col1, col2, col3 = st.columns([1,6,1])


with col2:
    st.markdown(load_markdown("content/fiches/indemnites.md"),
            unsafe_allow_html=True)

    st.image("assets/images/versement_indemnites.png", width=1800)
