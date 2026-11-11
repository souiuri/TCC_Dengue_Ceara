
from pathlib import Path
import pandas as pd
import geopandas as gpd

DADOS = Path("dados/processados/dengue_ceara_analitica.csv")
MALHA = "dados/geograficos/CE_Municipios_2024.zip"
SAIDA = Path("resultados/dengue_mensal_regional_2016_2025.csv")

# 1. Carregar dados epidemiológicos
df = pd.read_csv(DADOS, low_memory=False)

df = df[
    df["ANO_SINTOMAS"].between(2016, 2025)
    & df["MES_SINTOMAS"].between(1, 12)
    & (df["ATRASO_EXTREMO"] != True)
].copy()

# 2. Padronizar códigos municipais (6 dígitos)
df["CODIGO_MUNICIPIO"] = (
    pd.to_numeric(df["ID_MN_RESI"], errors="coerce")
    .astype("Int64")
    .astype("string")
    .str[:6]
)

# 3. Carregar regiões oficiais do IBGE
malha = gpd.read_file(MALHA)

regioes = malha[
    ["CD_MUN", "CD_RGI", "NM_RGI"]
].copy()

regioes["CODIGO_MUNICIPIO"] = (
    regioes["CD_MUN"].astype(str).str[:6]
)

assert regioes["CODIGO_MUNICIPIO"].is_unique
assert len(regioes) == 184
assert regioes["CD_RGI"].nunique() == 18

# 4. Associar município à região
df = df.merge(
    regioes[
        ["CODIGO_MUNICIPIO", "CD_RGI", "NM_RGI"]
    ],
    on="CODIGO_MUNICIPIO",
    how="left",
    validate="many_to_one"
)

sem_regiao = df["CD_RGI"].isna().sum()

print("Total de registros temporais:", len(df))
print("Registros sem região:", sem_regiao)
print("Registros regionalizados:", len(df) - sem_regiao)

# 5. Contagem mensal por região
mensal = (
    df.dropna(subset=["CD_RGI"])
    .groupby(
        ["CD_RGI", "NM_RGI", "ANO_SINTOMAS", "MES_SINTOMAS"]
    )
    .size()
    .reset_index(name="TOTAL_REGISTROS")
)

# 6. Garantir todos os meses de todas as regiões
identificacao = (
    regioes[["CD_RGI", "NM_RGI"]]
    .drop_duplicates()
)

periodos = pd.MultiIndex.from_product(
    [range(2016, 2026), range(1, 13)],
    names=["ANO_SINTOMAS", "MES_SINTOMAS"]
).to_frame(index=False)

grade = identificacao.merge(periodos, how="cross")

mensal = grade.merge(
    mensal,
    on=["CD_RGI", "NM_RGI", "ANO_SINTOMAS", "MES_SINTOMAS"],
    how="left",
    validate="one_to_one"
)

mensal["TOTAL_REGISTROS"] = (
    mensal["TOTAL_REGISTROS"].fillna(0).astype(int)
)

mensal = mensal.sort_values(
    ["CD_RGI", "ANO_SINTOMAS", "MES_SINTOMAS"]
)

# 7. Validações
assert len(mensal) == 2160
assert mensal["TOTAL_REGISTROS"].sum() == len(df) - sem_regiao

SAIDA.parent.mkdir(parents=True, exist_ok=True)
mensal.to_csv(SAIDA, index=False, encoding="utf-8-sig")

# 8. Picos regionais no conjunto dos dez anos
acumulado = (
    mensal.groupby(["NM_RGI", "MES_SINTOMAS"], as_index=False)
    ["TOTAL_REGISTROS"].sum()
)

picos = acumulado.loc[
    acumulado.groupby("NM_RGI")["TOTAL_REGISTROS"].idxmax()
].sort_values("NM_RGI")

print("\nMês de maior concentração por região (2016–2025):")
print(
    picos[
        ["NM_RGI", "MES_SINTOMAS", "TOTAL_REGISTROS"]
    ].to_string(index=False)
)

print("\nLinhas geradas:", len(mensal))
print("Total regionalizado:", mensal["TOTAL_REGISTROS"].sum())
print("Arquivo salvo em:", SAIDA)
