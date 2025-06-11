import streamlit as st

st.set_page_config(page_title="Page streamlit", layout="wide")

st.markdown("""
# Trabalhando com Streamlit
""")

nome = st.text_input("nome", placeholder="digite seu nomme")

btn_enviar = st.button("Enviar")

if btn_enviar:
    st.write(nome)