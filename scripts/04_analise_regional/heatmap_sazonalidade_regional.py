
from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ENTRADA = Path(
    "resultados/dengue_mensal_regional_2016_2025.csv"
)
SAIDA = Path(
    "resultados/graficos/heatmap_sazonalidade_regional.png"
)

df = pd.read_csv(ENTRADA)

# Somar os registros de cada mês nos dez anos
mensal = (
    df.groupby(["NM_RGI", "MES_SINTOMAS"], as_index=False)
    ["TOTAL_REGISTROS"].sum()
)

# Total acumulado de cada região
mensal["TOTAL_REGIAO"] = (
    mensal.groupby("NM_RGI")["TOTAL_REGISTROS"]
    .transform("sum")
)

assert (mensal["TOTAL_REGIAO"] > 0).all()

# Participação percentual de cada mês na região
mensal["PERCENTUAL"] = (
    mensal["TOTAL_REGISTROS"]
    / mensal["TOTAL_REGIAO"]
    * 100
)

tabela = mensal.pivot(
    index="NM_RGI",
    columns="MES_SINTOMAS",
    values="PERCENTUAL"
)

assert tabela.shape == (18, 12)
assert tabela.notna().all().all()

# Ordenar regiões pelo mês de maior concentração
mes_pico = tabela.idxmax(axis=1)
tabela = tabela.loc[
    mes_pico.sort_values(kind="stable").index
]

meses = [
    "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
    "Jul", "Ago", "Set", "Out", "Nov", "Dez"
]

tabela.columns = meses

plt.figure(figsize=(14, 10))

sns.heatmap(
    tabela,
    cmap="YlOrRd",
    annot=True,
    fmt=".1f",
    linewidths=0.4,
    cbar_kws={"label": "% dos registros da região"}
)

plt.title(
    "Sazonalidade regional da dengue no Ceará (2016–2025)\n"
    "Distribuição percentual mensal dos registros",
    fontsize=14,
    pad=15
)

plt.xlabel("Mês de início dos sintomas")
plt.ylabel("Região Geográfica Imediata")

plt.tight_layout()

SAIDA.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(SAIDA, dpi=300, bbox_inches="tight")
plt.close()

print("Regiões analisadas:", len(tabela))
print("Meses analisados:", len(tabela.columns))

print("\nSoma percentual por região:")
print(tabela.sum(axis=1).round(2).to_string())

print("\nFigura salva em:", SAIDA)