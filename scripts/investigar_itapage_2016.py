
import pandas as pd
import geopandas as gpd

df = pd.read_csv(
    "dados/processados/dengue_ceara_analitica.csv",
    low_memory=False
)

malha = gpd.read_file(
    "dados/geograficos/CE_Municipios_2024.zip"
)

municipios = malha.loc[
    malha["NM_RGI"] == "Itapagé",
    ["CD_MUN", "NM_MUN"]
].copy()

municipios["CODIGO_MUNICIPIO"] = (
    municipios["CD_MUN"].astype(str).str[:6]
)

df = df[
    (df["ANO_SINTOMAS"] == 2016)
    & (df["MES_SINTOMAS"] == 11)
    & (df["ATRASO_EXTREMO"] != True)
].copy()

df["CODIGO_MUNICIPIO"] = (
    pd.to_numeric(df["ID_MN_RESI"], errors="coerce")
    .astype("Int64")
    .astype("string")
    .str[:6]
)

df = df.merge(
    municipios[["CODIGO_MUNICIPIO", "NM_MUN"]],
    on="CODIGO_MUNICIPIO",
    how="inner",
    validate="many_to_one"
)

resultado = (
    df.groupby("NM_MUN")
    .size()
    .sort_values(ascending=False)
)

print("Registros em novembro de 2016:", len(df))
print("\nDistribuição por município:")
print(resultado.to_string())

print("\nParticipação percentual:")
print((resultado / len(df) * 100).round(2).to_string())


import pandas as pd

df = pd.read_csv(
    "dados/processados/dengue_ceara_analitica.csv",
    low_memory=False
)

df["CODIGO_MUNICIPIO"] = (
    pd.to_numeric(df["ID_MN_RESI"], errors="coerce")
    .astype("Int64")
    .astype("string")
    .str[:6]
)

# Código IBGE de Pentecoste: 231040
import geopandas as gpd

malha = gpd.read_file(
    "dados/geograficos/CE_Municipios_2024.zip"
)

codigo_pentecoste = (
    malha.loc[malha["NM_MUN"] == "Pentecoste", "CD_MUN"]
    .iloc[0][:6]
)

print("Código de Pentecoste:", codigo_pentecoste)

dados = df[
    (df["CODIGO_MUNICIPIO"] == codigo_pentecoste)
    & (df["ANO_SINTOMAS"] == 2016)
    & (df["ATRASO_EXTREMO"] != True)
].copy()

mensal = (
    dados.groupby("MES_SINTOMAS")
    .size()
    .reindex(range(1, 13), fill_value=0)
)

print("Total de registros em Pentecoste em 2016:", len(dados))

print("\nRegistros por mês:")
print(mensal.to_string())

print("\nClassificação final:")
print(
    dados["CLASSI_FIN"]
    .value_counts(dropna=False)
    .to_string()
)

print("\nPrimeira data de sintomas:", dados["DATA_SINTOMAS"].min())
print("Última data de sintomas:", dados["DATA_SINTOMAS"].max())


# Investigar a distribuição diária em novembro
novembro = dados[
    dados["MES_SINTOMAS"] == 11
].copy()

novembro["DATA_SINTOMAS"] = pd.to_datetime(
    novembro["DATA_SINTOMAS"],
    errors="coerce"
)

diario = (
    novembro.groupby("DATA_SINTOMAS")
    .size()
    .sort_values(ascending=False)
)

print("\nDatas com mais registros em novembro:")
print(diario.head(15).to_string())

print("\nDatas distintas:", diario.size)
print("Registros sem data válida:", novembro["DATA_SINTOMAS"].isna().sum())

print("\nCritérios de confirmação:")
print(
    novembro["CRITERIO"]
    .value_counts(dropna=False)
    .to_string()
)
