
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent

ARQUIVO = RAIZ / "dados/originais/populacao/POP2024_20241230.xls"
SAIDA = RAIZ / "dados/processados/populacao_ceara_2024.csv"

# Carrega os dados municipais do IBGE.
dados = pd.read_excel(
    ARQUIVO,
    sheet_name="MUNICÍPIOS",
    header=1,
    engine="xlrd",
    dtype={"COD. UF": str, "COD. MUNIC": str}
)

# Seleciona somente os municípios do Ceará.
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
].rename(columns={"NOME DO MUNICÍPIO": "MUNICIPIO"})

resultado.insert(1, "ANO", 2024)

# Valida os dados municipais.
assert len(resultado) == 184, "Quantidade incorreta de municípios."
assert resultado["CODIGO_IBGE"].nunique() == 184, "Códigos IBGE duplicados."
assert resultado["CODIGO_IBGE"].str.fullmatch(r"23\d{5}").all()
assert resultado["POPULACAO"].notna().all(), "Existem populações ausentes."
assert (resultado["POPULACAO"] > 0).all(), "Existem populações inválidas."

# Confere a soma municipal com o total estadual do IBGE.
estados = pd.read_excel(
    ARQUIVO,
    sheet_name="BRASIL E UFs",
    header=1,
    engine="xlrd"
)

linha_ceara = estados[
    estados.iloc[:, 0].astype(str).str.strip() == "Ceará"
]

assert len(linha_ceara) == 1, "Ceará não encontrado na tabela estadual."

populacao_oficial = int(linha_ceara.iloc[0, 1])
populacao_calculada = int(resultado["POPULACAO"].sum())

assert populacao_calculada == populacao_oficial, (
    "A soma das populações municipais difere do total estadual."
)

# Salva a base populacional processada.
SAIDA.parent.mkdir(parents=True, exist_ok=True)

resultado["POPULACAO"] = resultado["POPULACAO"].astype(int)

resultado.to_csv(
    SAIDA,
    index=False,
    encoding="utf-8-sig"
)

print("População oficial do Ceará:", populacao_oficial)
print("Conferência com a tabela estadual: OK")
print("\nMunicípios:", len(resultado))
print("Códigos IBGE únicos:", resultado["CODIGO_IBGE"].nunique())
print("População total:", populacao_calculada)

print("\nPrimeiros municípios:")
print(resultado.head(10).to_string(index=False))

print("\nArquivo gerado:", SAIDA)
