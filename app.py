import streamlit as st

st.set_page_config( 
    page_title="Ressources PAP",
    layout="wide",
    page_icon="🐋"
)


home = st.Page("pages/Home.py", title="Accueil")
pap = st.Page("pages/PAP.py", title="PAP")
pilotage = st.Page("pages/Pilotage.py", title="Pilotage")
sc = st.Page("pages/SC.py", title="Service Civique")

agrement = st.Page("pages/Agrement.py", title="Agrément")
bdd = st.Page("pages/BDD.py", title="BDD")
enveloppes = st.Page("pages/Enveloppes.py", title="Enveloppes")
indicateurs = st.Page("pages/Indicateurs.py", title="Indicateurs")
intermediation = st.Page("pages/Intermediation.py", title="Intermédiation")


glossaire = st.Page("pages/Glossaire.py", title="Glossaire")



pg = st.navigation(
    {
        "Présentation": [home, pilotage, pap, sc],
        "Fiches": [agrement, bdd, indicateurs, enveloppes, intermediation],
        "Resources": [glossaire],
    },
    position="top",
)

pg.run()




