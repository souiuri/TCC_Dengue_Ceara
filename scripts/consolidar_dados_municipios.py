
from pathlib import Path
from urllib.request import urlopen
import gzip
import json
import pandas as pd


# Configuração dos caminhos
RAIZ = Path(__file__).resolve().parent.parent

ARQUIVO = RAIZ / "dados/processados/dengue_ceara_analitica.csv"
SAIDA = RAIZ / "resultados/municipios_dengue_2016_2025.csv"

URL_IBGE = (
    "https://servicodados.ibge.gov.br/api/v1/"
    "localidades/estados/23/municipios"
)


# Carregar a base analítica
base = pd.read_csv(
    ARQUIVO,
    sep=None,
    engine="python",
    dtype={"ID_MN_RESI": "string"}
)

# Manter o critério utilizado na análise temporal
base = base[
    base["ATRASO_EXTREMO"].astype(str).str.lower() == "false"
].copy()

base["ID_MN_RESI"] = base["ID_MN_RESI"].str.strip()


# Consultar os municípios oficiais do IBGE
print("\nConsultando municípios do IBGE...")

try:
    with urlopen(URL_IBGE, timeout=30) as resposta:
        conteudo = resposta.read()

        if conteudo.startswith(b"\x1f\x8b"):
            conteudo = gzip.decompress(conteudo)

        municipios_ibge = json.loads(conteudo.decode("utf-8"))

except Exception as erro:
    print(f"Erro ao consultar o IBGE: {erro}")
    raise SystemExit(1)


# Criar tabela de referência municipal
referencia = pd.DataFrame([
    {
        "CODIGO_MUNICIPIO": str(municipio["id"])[:6],
        "CODIGO_IBGE": str(municipio["id"]),
        "MUNICIPIO": municipio["nome"]
    }
    for municipio in municipios_ibge
])

# Considerar somente municípios oficiais do Ceará
base_ceara = base[
    base["ID_MN_RESI"].isin(referencia["CODIGO_MUNICIPIO"])
].copy()


# Contar registros por município
contagem = (
    base_ceara.groupby("ID_MN_RESI")
    .size()
    .reset_index(name="TOTAL_REGISTROS")
)

# Associar os códigos aos nomes oficiais
resultado = referencia.merge(
    contagem,
    left_on="CODIGO_MUNICIPIO",
    right_on="ID_MN_RESI",
    how="left",
    validate="one_to_one"
)

resultado = resultado.drop(columns=["ID_MN_RESI"])

resultado["TOTAL_REGISTROS"] = (
    resultado["TOTAL_REGISTROS"].fillna(0).astype(int)
)

# Calcular participação percentual no total municipal
total = resultado["TOTAL_REGISTROS"].sum()

resultado["PERCENTUAL"] = (
    resultado["TOTAL_REGISTROS"] / total * 100
).round(4)

resultado = resultado.sort_values(
    "TOTAL_REGISTROS",
    ascending=False
).reset_index(drop=True)


# Validar os totais antes de salvar
assert len(resultado) == 184
assert total == len(base_ceara)
assert total + (len(base) - len(base_ceara)) == len(base)


# Salvar a tabela consolidada
SAIDA.parent.mkdir(parents=True, exist_ok=True)

resultado.to_csv(
    SAIDA,
    index=False,
    encoding="utf-8-sig"
)


# Exibir resultados
print("\n=== CONSOLIDAÇÃO MUNICIPAL ===")
print(f"Registros analisados: {len(base):,}")
print(f"Registros com município do Ceará: {total:,}")
print(f"Registros sem município cearense válido: {len(base) - total:,}")
print(f"Municípios na tabela: {len(resultado)}")

print("\n10 municípios com mais registros:")
print(
    resultado[
        ["MUNICIPIO", "TOTAL_REGISTROS", "PERCENTUAL"]
    ].head(10).to_string(index=False)
)

print(f"\nArquivo salvo em: {SAIDA}")
