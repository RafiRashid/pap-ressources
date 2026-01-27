import streamlit as st
from utils.loader import load_markdown

st.markdown(load_markdown("content/fiches/bdd.md"),
            unsafe_allow_html=True)

st.image("assets/images/bdd.png", width=900,caption="Schéma rapide des différentes BDD et le rôle d'un OA")
