
import geopandas as gpd

malha = gpd.read_file(
    "dados/geograficos/CE_Municipios_2024.zip"
)

regioes = (
    malha.groupby(["CD_RGI", "NM_RGI"])
    .agg(
        MUNICIPIOS=("CD_MUN", "nunique")
    )
    .reset_index()
    .sort_values("NM_RGI")
)

print("Total de regiões:", len(regioes))
print("Total de municípios:", regioes["MUNICIPIOS"].sum())

print("\nRegiões Geográficas Imediatas do Ceará:")
print(regioes.to_string(index=False))

print("\nMunicípios sem região:")
print(malha["CD_RGI"].isna().sum())
