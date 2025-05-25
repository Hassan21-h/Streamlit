import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

# Création du menu qui va afficher les choix qui se trouvent dans la variable options
with st.sidebar :
    st.button("Déconnexion")
    st.write("Bienvenue root")

    selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )
    
# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

def accueil():
      st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")

if st.session_state["authentication_status"]:
    if selection == "Accueil":
                st.title("Bienvenue sur ma page ")
                url = "https://webneel.com/wallpaper/sites/default/files/images/01-2018/4-beautiful-flower-wallpaper-hd-saxyman.jpg"
                st.image(url, caption="Image depuis une URL", width = 300)
    elif selection == "Photos":
                st.write("Bienvenue sur mon album photo")
                # Création de 3 colonnes 
                col1, col2, col3 = st.columns(3)

                # Contenu de la première colonne : 
                with col1:
                        st.header("Flower")
                        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flower_jtca001.jpg/960px-Flower_jtca001.jpg"
                        st.image(url, caption="Image depuis une URL", width = 200)

                # Contenu de la deuxième colonne :
                with col2:
                        st.header("Flower")
                        url = "http://ageheureux.a.g.pic.centerblog.net/fleur-rare-21.jpg"
                        st.image(url, caption="Image depuis une URL", width = 200)

                # Contenu de la troisième colonne : 
                with col3:
                        st.header("Flower")
                        url = "https://cdn.futura-sciences.com/buildsv6/images/largeoriginal/6/a/a/6aa4b8b167_57256_050214-screen-fleur8-1610-diapo.jpg"
                        st.image(url, caption="Image depuis une URL", width = 200)
  # Le bouton de déconnexion
    authenticator.logout("Déconnexion")



elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
