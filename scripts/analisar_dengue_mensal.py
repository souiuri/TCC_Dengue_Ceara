
from pathlib import Path

import pandas as pd

ENTRADA = Path("dados/processados/dengue_ceara_analitica.csv")
SAIDA = Path("resultados/dengue_mensal_2016_2025.csv")

df = pd.read_csv(
    ENTRADA,
    low_memory=False
)

# Manter somente registros válidos para a análise
df = df[
    (df["ANO_SINTOMAS"].between(2016, 2025))
    & (df["MES_SINTOMAS"].between(1, 12))
    & (df["ATRASO_EXTREMO"] != True)
].copy()

# Contagem mensal
mensal = (
    df.groupby(
        ["ANO_SINTOMAS", "MES_SINTOMAS"]
    )
    .size()
    .reset_index(name="TOTAL_REGISTROS")
)

# Garantir todos os 120 meses
periodos = pd.MultiIndex.from_product(
    [range(2016, 2026), range(1, 13)],
    names=["ANO_SINTOMAS", "MES_SINTOMAS"]
)

mensal = (
    mensal.set_index(["ANO_SINTOMAS", "MES_SINTOMAS"])
    .reindex(periodos, fill_value=0)
    .reset_index()
)

SAIDA.parent.mkdir(parents=True, exist_ok=True)
mensal.to_csv(SAIDA, index=False, encoding="utf-8-sig")

# Resumo por mês do calendário
resumo = (
    mensal.groupby("MES_SINTOMAS")["TOTAL_REGISTROS"]
    .agg(["sum", "mean"])
    .round(1)
)

# Identificar o mês de maior registro em cada ano
picos = mensal.loc[
    mensal.groupby("ANO_SINTOMAS")["TOTAL_REGISTROS"].idxmax()
]

print("Total de registros analisados:", mensal["TOTAL_REGISTROS"].sum())
print("Meses analisados:", len(mensal))

print("\nDistribuição por mês do calendário:")
print(resumo)

print("\nMês de pico em cada ano:")
print(
    picos[
        ["ANO_SINTOMAS", "MES_SINTOMAS", "TOTAL_REGISTROS"]
    ].to_string(index=False)
)

print("\nArquivo salvo em:", SAIDA)
