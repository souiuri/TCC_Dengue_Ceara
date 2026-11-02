
import pandas as pd

arquivo = "dados/originais/DENGBR24.csv"

colunas = [
    "ID_AGRAVO",
    "DT_NOTIFIC",
    "NU_ANO",
    "DT_SIN_PRI",
    "SG_UF",
    "ID_MN_RESI",
    "CLASSI_FIN",
    "CRITERIO",
    "NU_IDADE_N",
    "CS_SEXO",
    "ID_UNIDADE",
    "ID_MUNICIP"
]

total = 0
repetidos_8 = 0
repetidos_12 = 0

# Lê o arquivo nacional em blocos
partes = []

for bloco in pd.read_csv(
    arquivo,
    usecols=colunas,
    dtype="string",
    chunksize=100000
):
    ce = bloco[bloco["SG_UF"] == "23"].copy()
    partes.append(ce)

base = pd.concat(partes, ignore_index=True)

colunas_8 = colunas[:8]

repetidos_8 = base.duplicated(
    subset=colunas_8,
    keep=False
).sum()

repetidos_12 = base.duplicated(
    subset=colunas,
    keep=False
).sum()

print("Registros do Ceará:", len(base))
print("Repetições com 8 campos:", repetidos_8)
print("Repetições com 12 campos:", repetidos_12)

# Investiga as combinações repetidas com 12 variáveis
frequencias = (
    base.groupby(colunas, dropna=False)
    .size()
)

grupos_repetidos = frequencias[frequencias > 1]

print("\nGrupos com combinações repetidas:",
      len(grupos_repetidos))

print("Maior frequência encontrada:",
      int(frequencias.max()))

print("\nDistribuição dos grupos repetidos:")
print(
    grupos_repetidos.value_counts()
    .sort_index()
    .to_string()
)

# Seleciona registros envolvidos em repetições com 12 campos
mascara_repetidos = base.duplicated(
    subset=colunas,
    keep=False
)

registros_repetidos = base[mascara_repetidos]

print("\nClassificação dos 208 registros:")
print(
    registros_repetidos["CLASSI_FIN"]
    .value_counts(dropna=False)
    .to_string()
)

# Verifica quantos estão classificados como dengue
codigos_dengue = ["10", "11", "12"]

quantidade_dengue = (
    registros_repetidos["CLASSI_FIN"]
    .isin(codigos_dengue)
    .sum()
)

print("\nRegistros classificados como dengue:",
      int(quantidade_dengue))

# Campos clínicos adicionais para comparação
campos_clinicos = [
    "FEBRE",
    "MIALGIA",
    "CEFALEIA",
    "EXANTEMA",
    "HOSPITALIZ"
]

# Lê os campos adicionais preservando a ordem original
extras = pd.read_csv(
    arquivo,
    usecols=["SG_UF"] + campos_clinicos,
    dtype="string"
)

extras_ce = (
    extras[extras["SG_UF"] == "23"]
    [campos_clinicos]
    .reset_index(drop=True)
)

# Acrescenta os campos à base já filtrada
base_ampliada = pd.concat(
    [base.reset_index(drop=True), extras_ce],
    axis=1
)

colunas_17 = colunas + campos_clinicos

repetidos_17 = base_ampliada.duplicated(
    subset=colunas_17,
    keep=False
)

print("\nRepetições com 17 campos:",
      int(repetidos_17.sum()))

print("Classificação dessas repetições:")
print(
    base_ampliada.loc[repetidos_17, "CLASSI_FIN"]
    .value_counts(dropna=False)
    .to_string()
)

frequencias_17 = (
    base_ampliada.groupby(
        colunas_17,
        dropna=False
    )
    .size()
)

grupos_17 = frequencias_17[frequencias_17 > 1]

print("\nGrupos repetidos com 17 campos:",
      len(grupos_17))

print("\nDistribuição das frequências:")
print(
    grupos_17.value_counts()
    .sort_index()
    .to_string()
)

print("\nMaior frequência:",
      int(frequencias_17.max()))
