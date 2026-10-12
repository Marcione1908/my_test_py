
import streamlit as st

st.title("Meu primeiro aplicativo")

st.write("Olá! Meu aplicativo está funcionando.")

nome = st.text_input("Qual é o seu nome?")

if nome:
    st.success(f"Seja bem-vindo, {nome}!")
