
from pathlib import Path

import pandas as pd
import geopandas as gpd

ENTRADA = Path(
    "resultados/taxas_dengue_municipios_2016_2025.csv"
)
MALHA = "dados/geograficos/CE_Municipios_2024.zip"
SAIDA = Path(
    "resultados/taxas_dengue_regionais_2016_2025.csv"
)

df = pd.read_csv(
    ENTRADA,
    dtype={"CODIGO_MUNICIPIO": "string"}
)

malha = gpd.read_file(MALHA)

regioes = malha[
    ["CD_MUN", "CD_RGI", "NM_RGI"]
].copy()

regioes["CODIGO_MUNICIPIO"] = (
    regioes["CD_MUN"].astype(str).str[:6]
)

# Associar municípios às regiões
df = df.merge(
    regioes[
        ["CODIGO_MUNICIPIO", "CD_RGI", "NM_RGI"]
    ],
    on="CODIGO_MUNICIPIO",
    how="left",
    validate="many_to_one"
)

assert len(df) == 1840
assert df["CD_RGI"].notna().all()

# Somar registros e população dos municípios
regional = (
    df.groupby(
        ["CD_RGI", "NM_RGI", "ANO_SINTOMAS"],
        as_index=False
    )
    .agg(
        TOTAL_REGISTROS=("TOTAL_REGISTROS", "sum"),
        POPULACAO=("POPULACAO", "sum"),
        MUNICIPIOS=("CODIGO_MUNICIPIO", "nunique")
    )
)

# Taxa regional ponderada pela população
regional["TAXA_100MIL"] = (
    regional["TOTAL_REGISTROS"]
    / regional["POPULACAO"]
    * 100000
).round(2)

assert len(regional) == 180
assert (regional["POPULACAO"] > 0).all()
assert regional["TOTAL_REGISTROS"].sum() == 215243

SAIDA.parent.mkdir(parents=True, exist_ok=True)

regional.to_csv(
    SAIDA,
    index=False,
    encoding="utf-8-sig"
)

# Comparar regiões em 2024
ranking = regional[
    regional["ANO_SINTOMAS"] == 2024
].sort_values(
    "TAXA_100MIL",
    ascending=False
)

print("\nTaxas regionais de dengue em 2024:")
print(
    ranking[
        [
            "NM_RGI",
            "TOTAL_REGISTROS",
            "POPULACAO",
            "TAXA_100MIL"
        ]
    ].to_string(index=False)
)

print("\nRegiões analisadas:", regional["CD_RGI"].nunique())
print("Linhas geradas:", len(regional))
print("Total de registros:", regional["TOTAL_REGISTROS"].sum())
print("Arquivo salvo em:", SAIDA)
