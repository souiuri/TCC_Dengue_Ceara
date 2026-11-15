
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch

# Caminhos
PASTA_MALHAS = Path("dados/geograficos")
ARQUIVO_TAXAS = Path(
    "resultados/taxas_dengue_municipios_2016_2025.csv"
)
SAIDA = Path(
    "resultados/graficos/mapas_historicos_dengue_2016_2025.png"
)

# Malhas disponíveis: 2020 a 2025.
# Usaremos a malha de 2024 como referência espacial
# para todos os anos, permitindo uma comparação padronizada.
malha = gpd.read_file(
    PASTA_MALHAS / "CE_Municipios_2024.zip"
)

malha["CODIGO_MUNICIPIO"] = (
    malha["CD_MUN"].astype(str).str[:6]
)

taxas = pd.read_csv(
    ARQUIVO_TAXAS,
    dtype={"CODIGO_MUNICIPIO": str}
)

# Classes descritivas fixas
limites = [
    -0.01, 0, 100, 300, 700, 1500, float("inf")
]

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

fig, eixos = plt.subplots(
    2, 5,
    figsize=(20, 11)
)

anos = list(range(2016, 2026))

for ax, ano in zip(eixos.flat, anos):

    dados_ano = taxas.loc[
        taxas["ANO_SINTOMAS"] == ano,
        ["CODIGO_MUNICIPIO", "TAXA_100MIL"]
    ].copy()

    mapa = malha.merge(
        dados_ano,
        on="CODIGO_MUNICIPIO",
        how="left",
        validate="one_to_one"
    )

    assert len(mapa) == 184, (
        f"Quantidade incorreta de municípios em {ano}"
    )

    assert mapa["TAXA_100MIL"].notna().all(), (
        f"Taxas ausentes em {ano}"
    )

    mapa["CLASSE"] = pd.cut(
        mapa["TAXA_100MIL"],
        bins=limites,
        labels=rotulos,
        include_lowest=True
    )

    for indice, rotulo in enumerate(rotulos):
        parte = mapa.loc[
            mapa["CLASSE"] == rotulo
        ]

        if not parte.empty:
            parte.plot(
                ax=ax,
                color=cores[indice],
                edgecolor="#777777",
                linewidth=0.12
            )

    ax.set_title(
        str(ano),
        fontsize=15,
        fontweight="bold"
    )

    ax.set_axis_off()

    print(
        f"{ano}: {len(mapa)} municípios, "
        f"{mapa['TAXA_100MIL'].isna().sum()} taxas ausentes"
    )

# Legenda única para todos os mapas
legenda = [
    Patch(
        facecolor=cor,
        edgecolor="#777777",
        label=rotulo
    )
    for cor, rotulo in zip(cores, rotulos)
]

fig.legend(
    handles=legenda,
    loc="lower center",
    ncol=3,
    title="Registros classificados de dengue por 100 mil habitantes",
    fontsize=11,
    title_fontsize=12,
    frameon=False,
    bbox_to_anchor=(0.5, 0.065)
)

fig.suptitle(
    "Distribuição espacial das taxas de dengue no Ceará\n"
    "2016–2025",
    fontsize=20,
    fontweight="bold",
    y=0.98
)

fig.text(
    0.5,
    0.015,
    "Fontes: Ministério da Saúde (SINAN) e IBGE. "
    "Malha municipal de 2024. Elaboração própria.",
    ha="center",
    fontsize=10
)

fig.subplots_adjust(
    left=0.02,
    right=0.98,
    top=0.89,
    bottom=0.19,
    wspace=0.02,
    hspace=0.12
)

SAIDA.parent.mkdir(
    parents=True,
    exist_ok=True
)

fig.savefig(
    SAIDA,
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

print("\nFigura salva em:", SAIDA)
