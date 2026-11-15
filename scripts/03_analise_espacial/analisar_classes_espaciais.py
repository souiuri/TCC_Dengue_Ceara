
from pathlib import Path
import pandas as pd

ENTRADA = Path("resultados/taxas_dengue_municipios_2016_2025.csv")
SAIDA = Path("resultados/classes_espaciais_2016_2025.csv")

df = pd.read_csv(ENTRADA)

# Mesmas classes utilizadas nos mapas históricos
limites = [-0.01, 0, 100, 300, 700, 1500, float("inf")]

rotulos = [
    "0 - Sem registros",
    ">0 a 100",
    ">100 a 300",
    ">300 a 700",
    ">700 a 1500",
    ">1500"
]

assert len(df) == 1840, "Quantidade inesperada de registros"
assert df["TAXA_100MIL"].notna().all(), "Existem taxas ausentes"

df["CLASSE"] = pd.cut(
    df["TAXA_100MIL"],
    bins=limites,
    labels=rotulos,
    include_lowest=True
)

# Contar municípios em cada classe por ano
resultado = pd.crosstab(
    df["ANO_SINTOMAS"],
    df["CLASSE"]
)

resultado = resultado.reindex(
    index=range(2016, 2026),
    columns=rotulos,
    fill_value=0
)

# Verificar os 184 municípios em cada ano
assert (resultado.sum(axis=1) == 184).all(), (
    "Algum ano não possui 184 municípios"
)

# Salvar tabela
SAIDA.parent.mkdir(parents=True, exist_ok=True)

resultado.to_csv(
    SAIDA,
    encoding="utf-8-sig",
    index_label="ANO"
)

print("\nMunicípios por classe de taxa:")
print(resultado.to_string())

print("\nMunicípios com taxas acima de 700:")
print(
    (resultado[">700 a 1500"] + resultado[">1500"])
    .to_string()
)

print("\nArquivo salvo em:", SAIDA)
