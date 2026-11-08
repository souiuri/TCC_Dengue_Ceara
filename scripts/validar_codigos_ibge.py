
from pathlib import Path
from urllib.request import urlopen
import json
import pandas as pd
import gzip


# Caminhos e fonte oficial do IBGE
RAIZ = Path(__file__).resolve().parent.parent

ARQUIVO = (
    RAIZ / "dados" / "processados"
    / "dengue_ceara_analitica.csv"
)

URL_IBGE = (
    "https://servicodados.ibge.gov.br/api/v1/"
    "localidades/estados/23/municipios"
)


# Carregar a base e aplicar o filtro temporal
base = pd.read_csv(
    ARQUIVO,
    sep=None,
    engine="python",
    dtype={"ID_MN_RESI": "string"}
)

base = base[
    base["ATRASO_EXTREMO"].astype(str).str.lower() == "false"
].copy()

codigos = base["ID_MN_RESI"].str.strip()


# Consultar os municípios oficiais do Ceará
print("\nConsultando municípios do IBGE...")

try:
    with urlopen(URL_IBGE, timeout=30) as resposta:
        conteudo = resposta.read()

        # Descompactar quando a resposta estiver em GZIP
        if conteudo.startswith(b"\x1f\x8b"):
            conteudo = gzip.decompress(conteudo)

        municipios_ibge = json.loads(
            conteudo.decode("utf-8")
        )

except Exception as erro:
    print(f"Erro ao consultar o IBGE: {erro}")
    raise SystemExit(1)


# Relacionar códigos de 6 dígitos aos códigos oficiais de 7
referencia = {}

for municipio in municipios_ibge:
    codigo_completo = str(municipio["id"])
    codigo_reduzido = codigo_completo[:6]

    referencia[codigo_reduzido] = {
        "nome": municipio["nome"],
        "codigo_ibge": codigo_completo
    }


# Selecionar códigos municipais do Ceará
mascara_ceara = codigos.str.fullmatch(
    r"23\d{4}"
).fillna(False)

codigos_ceara = codigos[mascara_ceara]

codigos_encontrados = set(codigos_ceara.dropna().unique())
codigos_oficiais = set(referencia.keys())


# Comparar os códigos com a lista oficial
validos = codigos_encontrados & codigos_oficiais
invalidos = codigos_encontrados - codigos_oficiais
ausentes = codigos_oficiais - codigos_encontrados


# Exibir os resultados da validação
print("\n=== VALIDAÇÃO OFICIAL DOS MUNICÍPIOS ===")

print(f"Registros analisados: {len(base):,}")
print(f"Municípios cadastrados no IBGE: {len(referencia)}")
print(f"Códigos distintos na base: {len(codigos_encontrados)}")
print(f"Códigos reconhecidos pelo IBGE: {len(validos)}")
print(f"Códigos não reconhecidos: {len(invalidos)}")
print(f"Municípios ausentes na base: {len(ausentes)}")


# Mostrar possíveis inconsistências
if invalidos:
    print("\nCódigos não reconhecidos:")
    for codigo in sorted(invalidos):
        print(codigo)
else:
    print("\nNenhum código cearense não reconhecido.")

if ausentes:
    print("\nMunicípios ausentes:")
    for codigo in sorted(ausentes):
        print(codigo, referencia[codigo]["nome"])
else:
    print("Todos os municípios oficiais estão representados.")


# Mostrar os municípios com mais registros
print("\n=== 10 MUNICÍPIOS COM MAIS REGISTROS ===")

contagem = codigos_ceara.value_counts()

for codigo, quantidade in contagem.head(10).items():
    nome = referencia.get(codigo, {}).get(
        "nome", "Código não reconhecido"
    )

    print(f"{nome} ({codigo}): {quantidade:,}")


print("\nValidação concluída!")
print("Nenhum arquivo foi modificado.")
