# ⚽ Pipeline Brasileirão: ETL & Dashboard Automático

Um projeto *End-to-End* de Engenharia de Dados que extrai, transforma e exibe a tabela atualizada do Campeonato Brasileiro (Série A) de forma totalmente automatizada na nuvem.

## 🏗️ Arquitetura do Projeto

O fluxo de dados segue o padrão **ETL (Extract, Transform, Load)**:
1. **Extract (Extração):** Consumo da [API-Sports (Football)](https://www.api-football.com/) para obter os dados brutos da temporada do Brasileirão.
2. **Transform (Transformação):** Limpeza e estruturação dos dados JSON usando `pandas` para manter apenas as colunas essenciais (Posição, Time, Pontos, Saldo de Gols, Escudo). Tratamento de erros robusto (`try/except`) para indisponibilidade da API.
3. **Load (Carga):** Salvamento dos dados limpos em um Banco de Dados Relacional local (`SQLite`).
4. **Deploy & Automação:** Automação do script ETL via **GitHub Actions** (rodando diariamente) e visualização dos dados em um Dashboard interativo hospedado no **Streamlit Cloud**.

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Manipulação de Dados:** Pandas
- **Banco de Dados:** SQLite (`sqlite3`)
- **Requisições & Segurança:** `requests`, `python-dotenv`
- **Frontend / Dashboard:** Streamlit
- **Nuvem & CI/CD:** GitHub Actions (Secrets) e Streamlit Community Cloud

## 📊 Features do Dashboard

- **Métricas de Destaque:** Exibição dinâmica do Líder e do Lanterna do campeonato.
- **Tabela Interativa:** Colunas ordenáveis pelo usuário.
- **Visual Rico:** Renderização automática dos escudos oficiais de cada clube.

---

## 💻 Como rodar este projeto localmente

### 1. Clone o repositório
```bash
git clone [https://github.com/Mhauuuu/pipeline-brasileirao.git](https://github.com/Mhauuuu/pipeline-brasileirao.git)
cd pipeline-brasileirao