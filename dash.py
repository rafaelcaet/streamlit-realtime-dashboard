import streamlit as st
import pandas as pd


def show_dashboard():

    df = pd.read_csv("01 Spotify.csv")

    # inplate = true sobreescreve o dataframe original
    df.set_index("Track", inplace=True)

    st.session_state["spotify"] = df

    df_2 = df[df["Album"] == "Garage, Inc."]

    # unique() retorna os valores distintos dessa selecao posso contar com value_counts().index e retornar os index unicos com .index
    with st.sidebar:
        artists = df["Artist"].unique()
        artist = st.selectbox("Artista", artists)

        df_filtered = df[df["Artist"] == artist]

        albuns = df_filtered["Album"].unique()
        album = st.selectbox("Album", albuns)

    df_filtered2 = df[df["Album"] == album]

    with st.container():
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.write(df_2)

        with col2:
            st.bar_chart(df_filtered2["Stream"])

        with col3:
            st.bar_chart(df_filtered2["Stream"])

        with col4:
            st.bar_chart(df_filtered2["Stream"])

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.write(df_2)

        with col2:
            st.bar_chart(df_filtered2["Stream"])

    with st.expander("Clique para expandir"):
        st.write(df_2)
