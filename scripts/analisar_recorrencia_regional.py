
from pathlib import Path
import pandas as pd

ENTRADA = Path(
    "resultados/taxas_dengue_regionais_2016_2025.csv"
)

SAIDA = Path(
    "resultados/recorrencia_regional_2016_2025.csv"
)

df = pd.read_csv(ENTRADA)

# Taxa estadual: soma dos registros e das populações
# das 18 regiões, em cada ano
estadual = (
    df.groupby("ANO_SINTOMAS", as_index=False)
    .agg(
        REGISTROS_CEARA=("TOTAL_REGISTROS", "sum"),
        POPULACAO_CEARA=("POPULACAO", "sum")
    )
)

estadual["TAXA_CEARA"] = (
    estadual["REGISTROS_CEARA"]
    / estadual["POPULACAO_CEARA"]
    * 100000
)

df = df.merge(
    estadual[["ANO_SINTOMAS", "TAXA_CEARA"]],
    on="ANO_SINTOMAS",
    validate="many_to_one"
)

# Comparar taxas sem arredondamento intermediário
df["TAXA_REGIONAL_EXATA"] = (
    df["TOTAL_REGISTROS"]
    / df["POPULACAO"]
    * 100000
)

df["ACIMA_CEARA"] = (
    df["TAXA_REGIONAL_EXATA"] > df["TAXA_CEARA"]
)

# Contar quantos anos cada região ficou acima do Ceará
resultado = (
    df.groupby(["CD_RGI", "NM_RGI"], as_index=False)
    .agg(
        ANOS_ACIMA=("ACIMA_CEARA", "sum"),
        MAIOR_TAXA=("TAXA_100MIL", "max"),
        TOTAL_REGISTROS=("TOTAL_REGISTROS", "sum")
    )
)

resultado = resultado.sort_values(
    ["ANOS_ACIMA", "MAIOR_TAXA"],
    ascending=[False, False]
)

assert len(resultado) == 18
assert df.groupby("ANO_SINTOMAS").size().eq(18).all()

SAIDA.parent.mkdir(parents=True, exist_ok=True)

resultado.to_csv(
    SAIDA,
    index=False,
    encoding="utf-8-sig"
)

print("\nRecorrência regional acima da taxa estadual:")
print(resultado.to_string(index=False))

print("\nRegiões acima da taxa estadual em cada ano:")
print(
    df.groupby("ANO_SINTOMAS")["ACIMA_CEARA"]
    .sum()
    .to_string()
)

print("\nArquivo salvo em:", SAIDA)
