import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Dashboard Brasileirão", layout="centered")
st.title("⚽ Brasileirão Série A - 2024")


conexao = sqlite3.connect("banco_futebol.db")
df = pd.read_sql("SELECT * FROM classificacao", con=conexao)
conexao.close()

coluna1, coluna2 = st.columns(2)
lider = df.iloc[0]      
lanterna = df.iloc[-1] 

with coluna1:
    st.metric(label="🏆 Líder do Campeonato", value=lider['Time'], delta=f"{lider['Pontos']} pts")

with coluna2:
    
    st.metric(label="🧨 Lanterna", value=lanterna['Time'], delta=f"{lanterna['Pontos']} pts", delta_color="inverse")

st.divider()

st.dataframe(
    df,
    hide_index=True, 
    use_container_width=True,
    column_config={
    
        "Escudo": st.column_config.ImageColumn("Escudo")
    }
)