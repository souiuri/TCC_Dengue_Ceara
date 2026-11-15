
from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ENTRADA = Path(
    "resultados/taxas_dengue_regionais_2016_2025.csv"
)

SAIDA = Path(
    "resultados/graficos/heatmap_taxas_regionais_2016_2025.png"
)

df = pd.read_csv(ENTRADA)

# Organizar regiões nas linhas e anos nas colunas
tabela = df.pivot(
    index="NM_RGI",
    columns="ANO_SINTOMAS",
    values="TAXA_100MIL"
)

assert tabela.shape == (18, 10)
assert tabela.notna().all().all()

# Ordenar pela maior taxa observada na década
ordem = tabela.max(axis=1).sort_values(
    ascending=False
).index

tabela = tabela.loc[ordem]

plt.figure(figsize=(16, 11))

sns.heatmap(
    tabela,
    cmap="YlOrRd",
    annot=True,
    fmt=".0f",
    linewidths=0.5,
    cbar_kws={
        "label": "Registros por 100 mil habitantes"
    }
)

plt.title(
    "Evolução regional das taxas de dengue no Ceará (2016–2025)",
    fontsize=15,
    pad=15
)

plt.xlabel("Ano de início dos sintomas")
plt.ylabel("Região Geográfica Imediata")

plt.tight_layout()

SAIDA.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(
    SAIDA,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Regiões analisadas:", len(tabela))
print("Anos analisados:", len(tabela.columns))

# Identificar a maior taxa regional de cada ano
picos = df.loc[
    df.groupby("ANO_SINTOMAS")["TAXA_100MIL"].idxmax()
].sort_values("ANO_SINTOMAS")

print("\nRegião com maior taxa em cada ano:")
print(
    picos[
        ["ANO_SINTOMAS", "NM_RGI", "TAXA_100MIL"]
    ].to_string(index=False)
)

print("\nFigura salva em:", SAIDA)
