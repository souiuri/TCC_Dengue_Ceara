
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# Caminhos do projeto
MALHA = Path("dados/geograficos/CE_Municipios_2024.zip")
TAXAS = Path("resultados/taxas_dengue_municipios_2016_2025.csv")
SAIDA = Path("resultados/graficos/mapa_taxas_dengue_2024.png")

# Carregar malha municipal do IBGE
municipios = gpd.read_file(MALHA)
municipios["CODIGO_MUNICIPIO"] = municipios["CD_MUN"].astype(str).str[:6]

# Carregar taxas de dengue
taxas = pd.read_csv(
    TAXAS,
    dtype={"CODIGO_MUNICIPIO": str}
)

# Selecionar o ano de 2024
taxas_2024 = taxas.loc[
    taxas["ANO_SINTOMAS"] == 2024,
    ["CODIGO_MUNICIPIO", "TAXA_100MIL"]
].copy()

# Cruzar dados epidemiológicos e geográficos
mapa = municipios.merge(
    taxas_2024,
    on="CODIGO_MUNICIPIO",
    how="left",
    validate="one_to_one"
)

# Validar a junção
assert len(mapa) == 184, "Quantidade inesperada de municípios"
assert mapa["TAXA_100MIL"].notna().all(), "Existem taxas ausentes"

# Criar mapa
fig, ax = plt.subplots(figsize=(11, 10))

mapa.plot(
    column="TAXA_100MIL",
    ax=ax,
    cmap="YlOrRd",
    legend=True,
    edgecolor="#777777",
    linewidth=0.25,
    legend_kwds={
        "label": "Registros classificados de dengue por 100 mil habitantes",
        "shrink": 0.65
    }
)

ax.set_title(
    "Distribuição municipal das taxas de dengue\n"
    "Ceará — 2024",
    fontsize=15,
    fontweight="bold",
    pad=18
)

ax.set_axis_off()

fig.text(
    0.5, 0.035,
    "Fontes: Ministério da Saúde (SINAN) e IBGE. "
    "Elaboração própria.",
    ha="center",
    fontsize=9
)

SAIDA.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(SAIDA, dpi=300, bbox_inches="tight")
plt.close(fig)

print("Municípios representados:", len(mapa))
print("Taxas ausentes:", mapa["TAXA_100MIL"].isna().sum())
print("Menor taxa:", mapa["TAXA_100MIL"].min())
print("Maior taxa:", mapa["TAXA_100MIL"].max())
print("Mapa salvo em:", SAIDA)