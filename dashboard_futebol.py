import streamlit as st
import pandas as pd
import sqlite3

# Configuração da página (deixa a tabela mais larga)
st.set_page_config(page_title="Dashboard Brasileirão", layout="centered")

st.title("⚽ Brasileirão Série A - Temporada 2024")
st.write("Tabela de classificação atualizada diretamente do Banco de Dados SQL.")
st.divider()


conexao = sqlite3.connect("banco_futebol.db")

df_classificacao = pd.read_sql("SELECT * FROM classificacao", con=conexao)

conexao.close()

st.dataframe(
    df_classificacao,
    hide_index=True, 
    use_container_width=True 
)