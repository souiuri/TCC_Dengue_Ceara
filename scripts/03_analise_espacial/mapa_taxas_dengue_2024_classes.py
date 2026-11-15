
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib.patches import Patch

# Caminhos
MALHA = Path("dados/geograficos/CE_Municipios_2024.zip")
TAXAS = Path("resultados/taxas_dengue_municipios_2016_2025.csv")
SAIDA = Path("resultados/graficos/mapa_taxas_dengue_2024_classes.png")

# Carregar malha
municipios = gpd.read_file(MALHA)
municipios["CODIGO_MUNICIPIO"] = (
    municipios["CD_MUN"].astype(str).str[:6]
)

# Carregar taxas de 2024
taxas = pd.read_csv(
    TAXAS,
    dtype={"CODIGO_MUNICIPIO": str}
)

taxas_2024 = taxas.loc[
    taxas["ANO_SINTOMAS"] == 2024,
    ["CODIGO_MUNICIPIO", "TAXA_100MIL"]
].copy()

# Cruzar dados
mapa = municipios.merge(
    taxas_2024,
    on="CODIGO_MUNICIPIO",
    how="left",
    validate="one_to_one"
)

assert len(mapa) == 184
assert mapa["TAXA_100MIL"].notna().all()

# Classes descritivas definidas para o estudo
limites = [-0.01, 0, 100, 300, 700, 1500, float("inf")]

rotulos = [
    "0 — Sem registros",
    ">0 a 100",
    ">100 a 300",
    ">300 a 700",
    ">700 a 1.500",
    ">1.500"
]

cores = [
    "#f2f2f2",
    "#ffffcc",
    "#ffeda0",
    "#feb24c",
    "#f03b20",
    "#800026"
]

mapa["CLASSE"] = pd.cut(
    mapa["TAXA_100MIL"],
    bins=limites,
    labels=rotulos,
    include_lowest=True
)

# Preparar mapa
fig, ax = plt.subplots(figsize=(11, 10))

cmap = ListedColormap(cores)

for indice, rotulo in enumerate(rotulos):
    parte = mapa[mapa["CLASSE"] == rotulo]

    if not parte.empty:
        parte.plot(
            ax=ax,
            color=cores[indice],
            edgecolor="#777777",
            linewidth=0.25
        )

# Legenda
legenda = [
    Patch(facecolor=cor, edgecolor="#777777", label=rotulo)
    for cor, rotulo in zip(cores, rotulos)
]

ax.legend(
    handles=legenda,
    title="Registros por 100 mil habitantes",
    loc="lower left",
    fontsize=9,
    title_fontsize=10,
    frameon=True
)

ax.set_title(
    "Distribuição municipal das taxas de dengue\n"
    "Ceará — 2024 (classes de taxas)",
    fontsize=15,
    fontweight="bold",
    pad=18
)

ax.set_axis_off()

fig.text(
    0.5,
    0.035,
    "Fontes: Ministério da Saúde (SINAN) e IBGE. "
    "Elaboração própria.",
    ha="center",
    fontsize=9
)

SAIDA.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(
    SAIDA,
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

print("Municípios representados:", len(mapa))
print("Taxas ausentes:", mapa["TAXA_100MIL"].isna().sum())

print("\nMunicípios por classe:")
print(mapa["CLASSE"].value_counts().sort_index())

print("\nMapa salvo em:", SAIDA)
