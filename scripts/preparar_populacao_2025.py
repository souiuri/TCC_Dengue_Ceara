
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent

ARQUIVO = RAIZ / "dados/originais/populacao/POP2025_20260828.xls"
SAIDA = RAIZ / "dados/processados/populacao_ceara_2025.csv"

# Lê a tabela municipal, ignorando o título inicial.
dados = pd.read_excel(
    ARQUIVO,
    sheet_name="Municípios",
    header=1,
    engine="xlrd",
    dtype={"COD. UF": str, "COD. MUNIC": str}
)

# Seleciona apenas os municípios do Ceará.
dados = dados[dados["COD. UF"].str.strip() == "23"].copy()

dados["CODIGO_IBGE"] = (
    dados["COD. UF"].str.strip().str.zfill(2)
    + dados["COD. MUNIC"].str.strip().str.zfill(5)
)

dados["POPULACAO"] = pd.to_numeric(
    dados["POPULAÇÃO ESTIMADA"],
    errors="coerce"
)

resultado = dados[
    ["CODIGO_IBGE", "NOME DO MUNICÍPIO", "POPULACAO"]
].rename(
    columns={"NOME DO MUNICÍPIO": "MUNICIPIO"}
)

resultado.insert(1, "ANO", 2025)

# Valida a integridade dos dados extraídos.
assert len(resultado) == 184, "Quantidade inesperada de municípios."
assert resultado["CODIGO_IBGE"].nunique() == 184
assert resultado["POPULACAO"].notna().all()
assert (resultado["POPULACAO"] > 0).all()
assert resultado["POPULACAO"].sum() == 9268836

SAIDA.parent.mkdir(parents=True, exist_ok=True)

resultado.to_csv(
    SAIDA,
    index=False,
    encoding="utf-8-sig"
)

print("Municípios:", len(resultado))
print("Códigos IBGE únicos:", resultado["CODIGO_IBGE"].nunique())
print("População total:", int(resultado["POPULACAO"].sum()))

print("\nPrimeiros municípios:")
print(resultado.head(10).to_string(index=False))

print("\nArquivo gerado:", SAIDA)
