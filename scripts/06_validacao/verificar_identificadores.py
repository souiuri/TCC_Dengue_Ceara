
from pathlib import Path
import pandas as pd

PASTA_DADOS = Path("dados/originais")

# Campos que podem ajudar a identificar registros
COLUNAS_PROCURADAS = [
    "ANO_NASC",
    "NU_IDADE_N",
    "CS_SEXO",
    "ID_UNIDADE",
    "ID_MUNICIP",
    "DT_DIGITA",
    "NDUPLIC_N"
]

for ano in range(2016, 2026):
    nome = f"DENGBR{str(ano)[-2:]}.csv"
    caminho = PASTA_DADOS / nome

    # Lê somente o cabeçalho, sem carregar os registros
    colunas = pd.read_csv(
        caminho,
        nrows=0
    ).columns.tolist()

    encontradas = [
        coluna for coluna in COLUNAS_PROCURADAS
        if coluna in colunas
    ]

    print(f"\n--- Arquivo {ano} ---")
    print("Colunas encontradas:", encontradas)
    print("NU_NOTIFIC presente:", "NU_NOTIFIC" in colunas)
