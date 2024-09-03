import streamlit as st


def insert_into_db(email, name, password, role):

    conn = st.connection("postgresql", type="sql")
    query = (
        f"""
        INSERT INTO public.dashboard_users (
            email,
            name,
            password,
            role)
        VALUES 
        ({email},
        {name},
        {password},
        {role});

    """,
    )
    conn.query(query, ttl=0, show_spinner=False)


def show_add_user():
    with st.container():

        username = st.text_input(
            "Username",
            key="input_username",
            placeholder="type a username",
        )

        name = st.text_input("Name", key="input_name", placeholder="type a name")

        password = st.text_input(
            "Password", key="input_password", placeholder="type a password"
        )

        email = st.text_input("Email", key="input_email", placeholder="type a email")

        role = st.selectbox(
            "Role", ("admin", "seller", "supervisor"), key="selectbox_role"
        )

        if st.button("Atualizar"):
            st.write("credentials -> ", name, username, password, email, role)
