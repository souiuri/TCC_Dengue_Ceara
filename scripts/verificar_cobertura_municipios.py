
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent

arquivo = RAIZ / "dados" / "processados" / "dengue_ceara_analitica.csv"

base = pd.read_csv(
    arquivo,
    sep=None,
    engine="python",
    dtype={"ID_MN_RESI": "string"}
)

base = base[
    base["ATRASO_EXTREMO"].astype(str).str.lower() == "false"
].copy()

codigos = base["ID_MN_RESI"].str.strip()

ceara = codigos[
    codigos.str.fullmatch(r"23\d{4}").fillna(False)
]

print("\n=== COBERTURA MUNICIPAL DO CEARÁ ===")

print(f"Total de registros: {len(base):,}")
print(f"Registros com código do Ceará: {len(ceara):,}")
print(f"Registros sem código: {codigos.isna().sum():,}")
print(f"Registros fora do padrão do Ceará: {len(base) - len(ceara) - codigos.isna().sum():,}")

print(f"\nCódigos distintos do Ceará: {ceara.nunique()}")

print("\nDistribuição de registros por município:")
contagem = ceara.value_counts()

print(f"Menor quantidade: {contagem.min():,}")
print(f"Maior quantidade: {contagem.max():,}")

print("\nMunicípios com menos registros:")
print(contagem.tail(10))

print("\nMunicípios com mais registros:")
print(contagem.head(10))
