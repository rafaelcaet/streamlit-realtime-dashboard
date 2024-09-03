import streamlit_authenticator as stauth

# Senhas em texto plano
passwords = ['123', '456']

# Hashifica as senhas
hashed_passwords = stauth.Hasher(passwords).generate()

# Exibe as senhas hashificadas
print(hashed_passwords)
