import streamlit as st
import streamlit_authenticator as stauth
from streamlit_cookies_controller import CookieController
import dash  # Importa o arquivo dash.py
import add_user  # Importa o arquivo add_user.py

# Payload com senhas hashificadas
users = {
    "usernames": {
        "admin": {
            "name": "admin",
            "password": "$2b$12$7PkByo572DsR/Gpxm4ojyOW87SvxF5fMKP7784qrzb9fyyONQ3p12",
            "role": "admin",
        },
    }
}

st.set_page_config(page_title="Realtime Data Streaming", page_icon="☺", layout="wide")

# Inicializa o autenticador
authenticator = stauth.Authenticate(
    credentials=users,
    cookie_name="streamlit_auth",
    cookie_key="some_random_key",
    cookie_expiry_days=0,
)

# Cria um controlador para os cookies
cookie_controller = CookieController()

# Verifica se o usuário está autenticado e se a tela de login deve ser exibida
if (
    "authentication_status" in st.session_state
    and st.session_state.authentication_status
):

    name = st.session_state.name
    username = st.session_state.username

    # Adiciona o botão de logout na barra lateral
    with st.sidebar:
        st.write(f"Bem-vindo, {name}!")

        # Exibe o botão "Add user" apenas para o usuário com o papel de "admin"
        if username == "admin":
            if st.button("👤 Add user", key="add_user_button"):
                add_user.show_add_user()

        # Botão de logout
        if st.button("Logout", key="logout_button"):
            authenticator.logout(location="sidebar")
            if cookie_controller.get("streamlit_auth"):
                cookie_controller.remove(
                    "streamlit_auth"
                )  # Remove o cookie 'streamlit_auth' que foi atribuído no login
            st.session_state.clear()  # Limpa o estado da sessão
            st.rerun()  # Recarrega a página para mostrar a tela de login

        # Garante que a sessão seja limpa ao recarregar
        if st.session_state.get("clear_on_rerun", False) is False:
            if "authentication_status" in st.session_state:
                del st.session_state["authentication_status"]
            st.session_state["clear_on_rerun"] = True

    # Chama a função para mostrar a dashboard
    dash.show_dashboard()

else:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("")

    with col2:
        st.header("📊 Realtime Data Streaming", divider=True)
        # Exibe a tela de login no meio
        name, authentication_status, username = authenticator.login(location="main")

        if authentication_status:
            st.session_state.authentication_status = authentication_status
            st.session_state.name = name
            st.session_state.username = username
            st.rerun()  # Recarrega a página para mostrar a dashboard
        elif authentication_status == False:
            st.error("Usuário ou senha incorretos")
        elif authentication_status == None:
            st.warning("Por favor, insira seu nome de usuário e senha")

    with col3:
        st.write("")
