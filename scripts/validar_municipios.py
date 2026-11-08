
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent

ARQUIVO = RAIZ / "dados" / "processados" / "dengue_ceara_analitica.csv"

base = pd.read_csv(
    ARQUIVO,
    sep=None,
    engine="python",
    dtype={"ID_MN_RESI": "string"}
)

# Mesmo critério da análise temporal
base = base[base["ATRASO_EXTREMO"].astype(str).str.lower() == "false"].copy()

municipios = base["ID_MN_RESI"].str.strip()

print("\n=== VALIDAÇÃO DOS MUNICÍPIOS ===")
print(f"Total de registros analisados: {len(base):,}")
print(f"Códigos ausentes: {municipios.isna().sum():,}")

print("\nQuantidade de dígitos dos códigos:")
print(municipios.dropna().str.len().value_counts().sort_index())

print("\nCódigos que não possuem 6 ou 7 dígitos:")
invalidos = municipios[
    municipios.notna()
    & ~municipios.str.fullmatch(r"\d{6,7}").fillna(False)
]
print(invalidos.value_counts().head(20))

print("\nCódigos que não começam com 23 (Ceará):")
fora_ceara = municipios[
    municipios.notna()
    & ~municipios.str.startswith("23").fillna(False)
]
print(f"Registros: {len(fora_ceara):,}")
print(fora_ceara.value_counts().head(20))

print("\nTotal de códigos municipais distintos:")
print(municipios.dropna().nunique())

print("\n10 códigos municipais com mais registros:")
print(municipios.value_counts().head(10))
