
from pathlib import Path
import pandas as pd

arquivo = Path(
    "dados/processados/dengue_ceara_2016_2025.csv"
)

# Lê somente os campos necessários
base = pd.read_csv(
    arquivo,
    usecols=["DT_SIN_PRI", "CLASSI_FIN"],
    dtype="string"
)

print("Total de registros:", len(base))

# Seleciona registros classificados como dengue
codigos_dengue = ["10", "11", "12"]

dengue = base[
    base["CLASSI_FIN"].isin(codigos_dengue)
].copy()

print("Registros classificados como dengue:", len(dengue))

# Converte a data para formato datetime
dengue["DATA_SINTOMAS"] = pd.to_datetime(
    dengue["DT_SIN_PRI"],
    format="%Y-%m-%d",
    errors="coerce"
)

# Identifica datas ausentes ou inválidas
datas_invalidas = dengue["DATA_SINTOMAS"].isna().sum()

print("Datas ausentes ou inválidas:", datas_invalidas)

# Extrai o ano dos primeiros sintomas
dengue["ANO_SINTOMAS"] = dengue["DATA_SINTOMAS"].dt.year

print("\nRegistros por ano de início dos sintomas:")
print(
    dengue["ANO_SINTOMAS"]
    .value_counts(dropna=False)
    .sort_index()
    .to_string()
)

# Identifica registros fora do período estudado
fora_periodo = (
    dengue["DATA_SINTOMAS"].notna()
    & ~dengue["ANO_SINTOMAS"].between(2016, 2025)
)

print(
    "\nRegistros com sintomas fora de 2016-2025:",
    int(fora_periodo.sum())
)

print(
    "Registros com sintomas dentro de 2016-2025:",
    int(
        dengue["ANO_SINTOMAS"]
        .between(2016, 2025)
        .sum()
    )
)

# Carrega os campos necessários para investigar a origem
detalhes = pd.read_csv(
    arquivo,
    usecols=[
        "DT_SIN_PRI",
        "DT_NOTIFIC",
        "CLASSI_FIN",
        "ARQUIVO_ORIGEM"
    ],
    dtype="string"
)

detalhes = detalhes[
    detalhes["CLASSI_FIN"].isin(codigos_dengue)
].copy()

detalhes["DATA_SINTOMAS"] = pd.to_datetime(
    detalhes["DT_SIN_PRI"],
    format="%Y-%m-%d",
    errors="coerce"
)

detalhes["DATA_NOTIFICACAO"] = pd.to_datetime(
    detalhes["DT_NOTIFIC"],
    format="%Y-%m-%d",
    errors="coerce"
)

fora = detalhes[
    detalhes["DATA_SINTOMAS"].notna()
    & ~detalhes["DATA_SINTOMAS"].dt.year.between(2016, 2025)
].copy()

print("\nRegistros fora do período por arquivo de origem:")
print(
    fora["ARQUIVO_ORIGEM"]
    .value_counts()
    .sort_index()
    .to_string()
)

print("\nRegistros fora do período por ano de sintomas:")
print(
    fora["DATA_SINTOMAS"]
    .dt.year
    .value_counts()
    .sort_index()
    .to_string()
)

print("\nExemplos de datas fora do período:")
print(
    fora[[
        "ARQUIVO_ORIGEM",
        "DT_SIN_PRI",
        "DT_NOTIFIC"
    ]]
    .head(20)
    .to_string(index=False)
)

# Seleciona os registros dentro do período do estudo
dentro = detalhes[
    detalhes["DATA_SINTOMAS"].dt.year.between(2016, 2025)
].copy()

# Calcula o intervalo entre sintomas e notificação
dentro["INTERVALO_DIAS"] = (
    dentro["DATA_NOTIFICACAO"]
    - dentro["DATA_SINTOMAS"]
).dt.days

print("\nQualidade dos intervalos dentro de 2016-2025:")

print(
    "Intervalos negativos:",
    int((dentro["INTERVALO_DIAS"] < 0).sum())
)

print(
    "Intervalos de 0 a 30 dias:",
    int(dentro["INTERVALO_DIAS"].between(0, 30).sum())
)

print(
    "Intervalos de 31 a 365 dias:",
    int(dentro["INTERVALO_DIAS"].between(31, 365).sum())
)

print(
    "Intervalos superiores a 365 dias:",
    int((dentro["INTERVALO_DIAS"] > 365).sum())
)

print(
    "Intervalos ausentes:",
    int(dentro["INTERVALO_DIAS"].isna().sum())
)

# Investiga intervalos superiores a 365 dias
suspeitos = dentro[
    dentro["INTERVALO_DIAS"] > 365
].copy()

print("\nRegistros com intervalo superior a 365 dias:")
print("Total:", len(suspeitos))

print("\nDistribuição por arquivo de origem:")
print(
    suspeitos["ARQUIVO_ORIGEM"]
    .value_counts()
    .sort_index()
    .to_string()
)

print("\nOs 10 maiores intervalos:")
print(
    suspeitos[
        [
            "ARQUIVO_ORIGEM",
            "DT_SIN_PRI",
            "DT_NOTIFIC",
            "INTERVALO_DIAS"
        ]
    ]
    .sort_values("INTERVALO_DIAS", ascending=False)
    .head(10)
    .to_string(index=False)
)
