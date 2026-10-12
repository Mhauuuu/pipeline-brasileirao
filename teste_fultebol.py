import requests
import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://v3.football.api-sports.io/standings?league=71&season=2024"
headers = {
    "x-apisports-key": os.getenv("API_KEY_FUTEBOL")
}

print("Buscando dados da API...")
resposta = requests.get(url, headers=headers)
dados = resposta.json()

try:
    
    tabela_suja = dados['response'][0]['league']['standings'][0]

    
    linhas_limpas = []
    for linha in tabela_suja:
        linhas_limpas.append({
            "Posicao": linha['rank'],
            "Time": linha['team']['name'],
            "Pontos": linha['points'],
            "Saldo_Gols": linha['goalsDiff']
        })

    df = pd.DataFrame(linhas_limpas)
    print("\nTabela limpa formatada com sucesso!")

    
    conexao = sqlite3.connect("banco_futebol.db")
    df.to_sql(name="classificacao", con=conexao, if_exists="replace", index=False)
    conexao.close()
    print("Banco de Dados 'banco_futebol.db' atualizado!")

except IndexError:
    
    print("\n❌ ERRO: A API não enviou os times. Lista vazia!")
    print("Resposta crua:", dados)

except KeyError:
    
    print("\n❌ ERRO: A estrutura do JSON está diferente do esperado!")
    print("Resposta crua:", dados)

except Exception as erro_geral:
    
    print(f"\n❌ ERRO : {erro_geral}")