import streamlit as st

st.set_page_config( 
    page_title="Ressources PAP",
    layout="wide",
    page_icon="🐋"
)

# Presentation
home = st.Page("pages/Home.py", title="Accueil")
pap = st.Page("pages/PAP.py", title="PAP")
pilotage = st.Page("pages/Pilotage.py", title="Pilotage")
sc = st.Page("pages/SC.py", title="Service Civique")
principes = st.Page("pages/Principes.py", title="Principes du SC")

# Acteurs
asc = st.Page("pages/ASC.py", title="Agence du Service Civique (ASC)")
asp = st.Page("pages/ASP.py", title="Agence de Service et de Paiement (ASP)")
volontaire = st.Page("pages/Volontaire.py", title="Volontaires")
service_deconcentres = st.Page("pages/ServicesDeconcentres.py", title="Services déconcentrés")
oa = st.Page("pages/OrganismeAccueil.py", title="Organisme d'accueil")

# Fiches
agrement = st.Page("pages/Agrement.py", title="Agrément")
bdd = st.Page("pages/BDD.py", title="BDD")
enveloppes = st.Page("pages/Enveloppes.py", title="Enveloppes")
indicateurs = st.Page("pages/Indicateurs.py", title="Indicateurs")
intermediation = st.Page("pages/Intermediation.py", title="Intermédiation")
indemnites = st.Page("pages/Indemnites.py", title="Indemnités")

# Glossaire
glossaire = st.Page("pages/Glossaire.py", title="Glossaire")


# Navigation
pg = st.navigation(
    {
        "Présentation": [home, pilotage, pap, sc, principes],
        "Acteurs": [asc, asp, volontaire, service_deconcentres, oa],
        "Fiches": [agrement, bdd, indicateurs, enveloppes, intermediation, indemnites],      
        "Resources": [glossaire],
    },
    position="top",
)

pg.run()




