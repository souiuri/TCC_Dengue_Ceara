
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent

ARQUIVO_BASE = RAIZ / "dados/processados/dengue_ceara_analitica.csv"
ARQUIVO_MUNICIPIOS = RAIZ / "resultados/municipios_dengue_2016_2025.csv"
ARQUIVO_SAIDA = RAIZ / "resultados/municipios_dengue_por_ano.csv"

base = pd.read_csv(
    ARQUIVO_BASE,
    dtype={"ID_MN_RESI": "string"},
    low_memory=False
)

municipios = pd.read_csv(
    ARQUIVO_MUNICIPIOS,
    dtype={"CODIGO_MUNICIPIO": "string"},
    encoding="utf-8-sig"
)

# Aplica os mesmos critérios das análises anteriores.
base = base[base["ATRASO_EXTREMO"] == False].copy()

codigos_validos = set(municipios["CODIGO_MUNICIPIO"])

base = base[
    base["ID_MN_RESI"].isin(codigos_validos)
].copy()

# Agrupa os registros por município e ano dos sintomas.
resultado = (
    base.groupby(["ID_MN_RESI", "ANO_SINTOMAS"])
    .size()
    .reset_index(name="TOTAL_REGISTROS")
)

resultado = resultado.merge(
    municipios[["CODIGO_MUNICIPIO", "MUNICIPIO"]],
    left_on="ID_MN_RESI",
    right_on="CODIGO_MUNICIPIO",
    how="left",
    validate="many_to_one"
)

# Inclui também os anos sem registros para cada município.
anos = pd.DataFrame({"ANO_SINTOMAS": range(2016, 2026)})

grade = municipios[["CODIGO_MUNICIPIO", "MUNICIPIO"]].merge(
    anos,
    how="cross"
)

resultado = grade.merge(
    resultado[["CODIGO_MUNICIPIO", "ANO_SINTOMAS", "TOTAL_REGISTROS"]],
    on=["CODIGO_MUNICIPIO", "ANO_SINTOMAS"],
    how="left",
    validate="one_to_one"
)

resultado["TOTAL_REGISTROS"] = (
    resultado["TOTAL_REGISTROS"].fillna(0).astype(int)
)

resultado = resultado.sort_values(
    ["MUNICIPIO", "ANO_SINTOMAS"]
)

assert len(resultado) == 1840
assert resultado["TOTAL_REGISTROS"].sum() == len(base)

resultado.to_csv(
    ARQUIVO_SAIDA,
    index=False,
    encoding="utf-8-sig"
)

print("Municípios:", resultado["CODIGO_MUNICIPIO"].nunique())
print("Anos:", resultado["ANO_SINTOMAS"].nunique())
print("Linhas geradas:", len(resultado))
print("Total de registros:", resultado["TOTAL_REGISTROS"].sum())

print("\nRegistros por ano:")
print(resultado.groupby("ANO_SINTOMAS")["TOTAL_REGISTROS"].sum())

print("\nArquivo salvo em:", ARQUIVO_SAIDA)
