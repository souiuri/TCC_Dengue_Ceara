
from pathlib import Path
import pandas as pd

pasta = Path("dados/processados")

colunas = [
    "ID_AGRAVO",
    "DT_NOTIFIC",
    "NU_ANO",
    "DT_SIN_PRI",
    "SG_UF",
    "ID_MN_RESI",
    "CLASSI_FIN",
    "CRITERIO"
]

bases = []

for ano in range(2016, 2026):
    arquivo = pasta / f"DENGBR{str(ano)[-2:]}_CE.csv"

    df = pd.read_csv(
        arquivo,
        dtype="string",
        usecols=colunas
    )

    df["arquivo_origem"] = ano
    bases.append(df)

base = pd.concat(bases, ignore_index=True)

# Uma assinatura representa a combinação das oito variáveis.
assinatura = pd.util.hash_pandas_object(
    base[colunas],
    index=False
)


# Identifica combinações repetidas dentro de cada arquivo
repetidos = base.duplicated(
    subset=["arquivo_origem"] + colunas,
    keep=False
)

print("\nRepetições dentro dos arquivos:")

for ano in range(2016, 2026):
    mascara = base["arquivo_origem"] == ano

    quantidade = (repetidos & mascara).sum()

    print(f"{ano}: {quantidade} registros")

print("\nTotal de registros envolvidos em repetições:",
      int(repetidos.sum()))


# Conta quantas vezes cada combinação aparece
frequencias = (
    base.groupby(
        ["arquivo_origem"] + colunas,
        dropna=False
    )
    .size()
    .sort_values(ascending=False)
)

print("\nAs 10 combinações mais frequentes:")
print(frequencias.head(10).to_string())

print("\nDistribuição das frequências:")
print(
    frequencias.value_counts()
    .sort_index()
    .head(20)
    .to_string()
)

print("\nMaior frequência encontrada:", frequencias.max())
