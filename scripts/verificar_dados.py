
import pandas as pd
from pathlib import Path

pasta_projeto = Path(__file__).resolve().parent.parent
arquivo = pasta_projeto / "dados" / "dengue_ceara_2024.csv"

df = pd.read_csv(arquivo, dtype=str)

print("=== TAMANHO DO ARQUIVO ===")
print(f"Quantidade de registros: {len(df)}")
print(f"Quantidade de colunas: {len(df.columns)}")

print("\n=== ANOS DAS NOTIFICAÇÕES ===")
print(df["NU_ANO"].value_counts(dropna=False).sort_index())

print("\n=== CLASSIFICAÇÕES FINAIS ===")
print(df["CLASSI_FIN"].value_counts(dropna=False))

print("\n=== DATAS DAS NOTIFICAÇÕES ===")
print("Primeira data:", df["DT_NOTIFIC"].min())
print("Última data:", df["DT_NOTIFIC"].max())

print("\n=== PRIMEIROS REGISTROS ===")
print(df.head().to_string(index=False))

print("\n=== REGISTROS FORA DE 2024 ===")

fora_2024 = df[df["NU_ANO"] != "2024"]

print(fora_2024.to_string(index=False))

print("\n=== REGISTROS SEM CLASSIFICAÇÃO ===")

sem_classificacao = df[df["CLASSI_FIN"].isna()]

print(sem_classificacao.to_string(index=False))

print("\n=== DISTRIBUIÇÃO POR MÊS ===")

datas = pd.to_datetime(df["DT_NOTIFIC"], errors="coerce")

print(
    datas.dt.month.value_counts()
    .sort_index()
    .rename_axis("Mês")
    .to_string()
)