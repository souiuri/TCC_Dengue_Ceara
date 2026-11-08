
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent

ARQUIVO_DENGUE = RAIZ / "resultados/municipios_dengue_por_ano.csv"
ARQUIVO_POPULACAO = RAIZ / "dados/processados/populacao_ceara_2025.csv"
ARQUIVO_SAIDA = RAIZ / "resultados/taxas_municipais_2025.csv"

dengue = pd.read_csv(
    ARQUIVO_DENGUE,
    dtype={"CODIGO_MUNICIPIO": "string"}
)

populacao = pd.read_csv(
    ARQUIVO_POPULACAO,
    dtype={"CODIGO_IBGE": "string"}
)

# Seleciona os registros de dengue de 2025.
dengue = dengue[dengue["ANO_SINTOMAS"] == 2025].copy()

# Compatibiliza os códigos municipais de seis dígitos.
populacao["CODIGO_MUNICIPIO"] = populacao["CODIGO_IBGE"].str[:6]

resultado = dengue.merge(
    populacao[["CODIGO_MUNICIPIO", "POPULACAO"]],
    on="CODIGO_MUNICIPIO",
    how="left",
    validate="one_to_one"
)

assert len(resultado) == 184
assert resultado["POPULACAO"].notna().all()
assert (resultado["POPULACAO"] > 0).all()
assert resultado["TOTAL_REGISTROS"].sum() == 5048

resultado["TAXA_100MIL"] = (
    resultado["TOTAL_REGISTROS"]
    / resultado["POPULACAO"]
    * 100000
)

resultado = resultado.sort_values(
    "TAXA_100MIL",
    ascending=False
)

resultado.to_csv(
    ARQUIVO_SAIDA,
    index=False,
    encoding="utf-8-sig"
)

print("Municípios analisados:", len(resultado))
print("Registros de dengue em 2025:", resultado["TOTAL_REGISTROS"].sum())

print("\n10 maiores taxas por 100 mil habitantes:")
print(
    resultado[
        ["MUNICIPIO", "TOTAL_REGISTROS", "POPULACAO", "TAXA_100MIL"]
    ].head(10).to_string(index=False)
)

print("\nArquivo gerado:", ARQUIVO_SAIDA)
