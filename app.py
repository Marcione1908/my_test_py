```python
import streamlit as st
from datetime import date

st.title("Verificador de Alistamento Militar")

st.write("Informe seus dados para verificar sua idade.")

# Campo para digitar o nome
nome = st.text_input("Digite seu nome:")

# Campo para informar o ano de nascimento
ano_nascimento = st.number_input(
    "Digite seu ano de nascimento:",
    min_value=1900,
    max_value=date.today().year,
    step=1
)

# Botão para verificar
if st.button("Verificar aptidão"):

    if nome.strip() == "":
        st.warning("Por favor, digite seu nome.")

    else:
        ano_atual = date.today().year
        idade = ano_atual - ano_nascimento

        st.write(f"Nome: {nome}")
        st.write(f"Idade: {idade} anos")

        if idade >= 18:
            st.success("Você está apto para se alistar!")
        else:
            st.error("Você ainda não está apto para se alistar.")
```
