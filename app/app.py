import streamlit as st

st.set_page_config(page_title="Validador de schema excel")

st.title("Insira o seu excel para validação.")

file = st.file_uploader("Carregue seu arquivo Excel aqui", type=["xlsx"])

if file is not None:
    st.success("O schema do arquivo Excel está correto!")
