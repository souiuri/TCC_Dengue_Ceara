
import pandas as pd
from pathlib import Path

# Caminho do arquivo original
arquivo_entrada = Path(
    r"C:\Users\Verônica\Downloads\DENGBR24.csv\DENGBR24.csv"
)

# Pasta do projeto
pasta_projeto = Path(__file__).resolve().parent.parent

# Arquivo de saída
arquivo_saida = pasta_projeto / "dados" / "dengue_ceara_2024.csv"

# Colunas necessárias para a análise
colunas = [
    "NU_ANO",
    "DT_NOTIFIC",
    "DT_SIN_PRI",
    "SG_UF",
    "ID_MN_RESI",
    "CLASSI_FIN",
]

print("Iniciando a leitura do arquivo...")
print("Isso pode levar alguns minutos.")

total_linhas = 0
total_ceara = 0
primeiro_bloco = True

for bloco in pd.read_csv(
    arquivo_entrada,
    sep=",",
    encoding="latin1",
    usecols=colunas,
    chunksize=100_000,
    dtype=str,
):
    total_linhas += len(bloco)

    ceara = bloco[bloco["SG_UF"].str.strip() == "23"]

    if not ceara.empty:
        ceara.to_csv(
            arquivo_saida,
            mode="w" if primeiro_bloco else "a",
            header=primeiro_bloco,
            index=False,
            encoding="utf-8",
        )
        primeiro_bloco = False
        total_ceara += len(ceara)

    print(f"Linhas examinadas: {total_linhas:,}")

print("\nProcessamento concluído!")
print(f"Registros encontrados no Ceará: {total_ceara:,}")

if total_ceara > 0:
    print(f"Arquivo criado em: {arquivo_saida}")
else:
    print("Nenhum registro do Ceará foi encontrado.")