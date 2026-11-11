
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent

ENTRADA = RAIZ / "resultados/taxas_dengue_municipios_2016_2025.csv"
SAIDA = RAIZ / "resultados/graficos/heatmap_taxas_municipais.png"

dados = pd.read_csv(ENTRADA)

estadual = dados.groupby("ANO_SINTOMAS").agg(
    registros=("TOTAL_REGISTROS", "sum"),
    populacao=("POPULACAO", "sum")
)

estadual["TAXA_ESTADUAL"] = (
    estadual["registros"] / estadual["populacao"] * 100000
)

dados = dados.merge(
    estadual[["TAXA_ESTADUAL"]],
    left_on="ANO_SINTOMAS",
    right_index=True,
    validate="many_to_one"
)

dados["ACIMA_ESTADUAL"] = (
    dados["TAXA_100MIL"] > dados["TAXA_ESTADUAL"]
)

ranking = (
    dados.groupby(["CODIGO_MUNICIPIO", "MUNICIPIO"])
    .agg(
        ANOS_ACIMA=("ACIMA_ESTADUAL", "sum"),
        MAIOR_TAXA=("TAXA_100MIL", "max")
    )
    .reset_index()
    .sort_values(
        ["ANOS_ACIMA", "MAIOR_TAXA"],
        ascending=False
    )
)

top15 = ranking.head(15)["CODIGO_MUNICIPIO"]

selecionados = dados[
    dados["CODIGO_MUNICIPIO"].isin(top15)
]

matriz = selecionados.pivot(
    index="MUNICIPIO",
    columns="ANO_SINTOMAS",
    values="TAXA_100MIL"
)

ordem = ranking.head(15)["MUNICIPIO"].tolist()
matriz = matriz.reindex(ordem)

fig, ax = plt.subplots(figsize=(14, 9))

sns.heatmap(
    matriz,
    cmap="YlOrRd",
    annot=True,
    fmt=".0f",
    linewidths=0.5,
    cbar_kws={
        "label": "Registros classificados por 100 mil habitantes"
    },
    ax=ax
)

ax.set_title(
    "Ceará — Taxas municipais de dengue (2016–2025)\n"
    "15 municípios com maior recorrência acima da taxa estadual"
)

ax.set_xlabel("Ano de início dos sintomas")
ax.set_ylabel("Município")

fig.tight_layout()

SAIDA.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(SAIDA, dpi=300, bbox_inches="tight")

plt.close(fig)

print("Mapa de calor gerado:", SAIDA)
