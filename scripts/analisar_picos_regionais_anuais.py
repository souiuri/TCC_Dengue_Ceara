
from pathlib import Path
import pandas as pd

ENTRADA = Path(
    "resultados/dengue_mensal_regional_2016_2025.csv"
)

SAIDA = Path(
    "resultados/picos_regionais_anuais_2016_2025.csv"
)

df = pd.read_csv(ENTRADA)

# Encontrar o maior número mensal em cada região e ano
picos = df.loc[
    df.groupby(["CD_RGI", "ANO_SINTOMAS"])[
        "TOTAL_REGISTROS"
    ].idxmax()
].copy()

picos = picos.sort_values(
    ["NM_RGI", "ANO_SINTOMAS"]
)

picos = picos[
    [
        "CD_RGI",
        "NM_RGI",
        "ANO_SINTOMAS",
        "MES_SINTOMAS",
        "TOTAL_REGISTROS"
    ]
]

assert len(picos) == 180

SAIDA.parent.mkdir(parents=True, exist_ok=True)
picos.to_csv(
    SAIDA,
    index=False,
    encoding="utf-8-sig"
)

# Tabela: regiões nas linhas, anos nas colunas
tabela = picos.pivot(
    index="NM_RGI",
    columns="ANO_SINTOMAS",
    values="MES_SINTOMAS"
)

print("\nMês de pico por região e ano:")
print(tabela.to_string())

# Quantidade de picos por mês
print("\nDistribuição dos 180 picos:")
print(
    picos["MES_SINTOMAS"]
    .value_counts()
    .sort_index()
    .to_string()
)

# Investigar especificamente Itapagé em novembro
itapage = df[
    (df["NM_RGI"] == "Itapagé")
    & (df["MES_SINTOMAS"] == 11)
]

print("\nRegistros de novembro em Itapagé, por ano:")
print(
    itapage[
        ["ANO_SINTOMAS", "TOTAL_REGISTROS"]
    ].to_string(index=False)
)

print("\nArquivo salvo em:", SAIDA)
