
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Verificador de Alistamento",
    page_icon="🎖️"
)

st.title("🎖️ Verificador de Alistamento Militar")

st.write("Preencha seus dados abaixo.")

nome = st.text_input("Nome completo")

data_nascimento = st.date_input(
    "Data de nascimento",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    format="DD/MM/YYYY"
)

if st.button("Verificar aptidão", type="primary"):

    if not nome.strip():
        st.warning("Digite seu nome completo.")

    else:
        hoje = date.today()

        idade = (
            hoje.year
            - data_nascimento.year
            - (
                (hoje.month, hoje.day)
                < (data_nascimento.month, data_nascimento.day)
            )
        )

        st.subheader("Resultado")

        st.write(f"**Nome:** {nome}")
        st.write(f"**Idade:** {idade} anos")

        if idade >= 18:
            st.success("Você está apto pelo critério de idade.")
        else:
            st.error("Você ainda não atingiu 18 anos.")
