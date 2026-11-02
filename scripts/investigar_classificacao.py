
import pandas as pd

arquivo = "dados/originais/DENGBR25.csv"

df = pd.read_csv(
    arquivo,
    dtype=str,
    usecols=["SG_UF", "CLASSI_FIN", "CRITERIO", "ID_AGRAVO"]
)

# Seleciona apenas os registros do Ceará
df = df[df["SG_UF"] == "23"]

print("\n1. Agravos registrados:")
print(df["ID_AGRAVO"].value_counts(dropna=False))

print("\n2. Classificação por critério:")
print(
    pd.crosstab(
        df["CLASSI_FIN"].fillna("VAZIO"),
        df["CRITERIO"].fillna("VAZIO")
    )
)

print("\n3. Classificação por agravo:")
print(
    pd.crosstab(
        df["CLASSI_FIN"].fillna("VAZIO"),
        df["ID_AGRAVO"].fillna("VAZIO")
    )
)
