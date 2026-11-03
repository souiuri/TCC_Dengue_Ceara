
from pathlib import Path
import pandas as pd

arquivo = Path(
    "dados/processados/dengue_ceara_analitica.csv"
)

base = pd.read_csv(arquivo)

print("Total de registros:", len(base))

print("\nRegistros por ano de início dos sintomas:")
print(
    base["ANO_SINTOMAS"]
    .value_counts()
    .sort_index()
    .to_string()
)

print("\nVerificação dos anos:")
print("Ano inicial:", base["ANO_SINTOMAS"].min())
print("Ano final:", base["ANO_SINTOMAS"].max())

print("\nRegistros com atraso extremo:")
print(base["ATRASO_EXTREMO"].value_counts().to_string())

print("\nTotal de registros por classificação:")
print(
    base["CLASSI_FIN"]
    .value_counts()
    .sort_index()
    .to_string()
)
