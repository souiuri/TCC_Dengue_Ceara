
from pathlib import Path
import pandas as pd

entrada = Path(
    "dados/processados/dengue_ceara_2016_2025.csv"
)

saida = Path(
    "dados/processados/dengue_ceara_analitica.csv"
)

base = pd.read_csv(entrada, dtype="string")

# Seleciona registros classificados como dengue
dengue = base[
    base["CLASSI_FIN"].isin(["10", "11", "12"])
].copy()

# Converte as datas
dengue["DATA_SINTOMAS"] = pd.to_datetime(
    dengue["DT_SIN_PRI"],
    format="%Y-%m-%d",
    errors="coerce"
)

dengue["DATA_NOTIFICACAO"] = pd.to_datetime(
    dengue["DT_NOTIFIC"],
    format="%Y-%m-%d",
    errors="coerce"
)

# Calcula o intervalo entre sintomas e notificação
dengue["INTERVALO_DIAS"] = (
    dengue["DATA_NOTIFICACAO"]
    - dengue["DATA_SINTOMAS"]
).dt.days

# Seleciona o período do estudo
periodo = dengue[
    dengue["DATA_SINTOMAS"].dt.year.between(2016, 2025)
].copy()

# Identifica atrasos extremos sem excluir os registros
periodo["ATRASO_EXTREMO"] = (
    periodo["INTERVALO_DIAS"] > 365
)

# Extrai ano e mês dos sintomas
periodo["ANO_SINTOMAS"] = (
    periodo["DATA_SINTOMAS"].dt.year
)

periodo["MES_SINTOMAS"] = (
    periodo["DATA_SINTOMAS"].dt.month
)

# Salva a base analítica
periodo.to_csv(
    saida,
    index=False,
    encoding="utf-8-sig"
)

print("Base analítica criada!")
print("Total de registros:", len(periodo))
print(
    "Registros com atraso extremo:",
    int(periodo["ATRASO_EXTREMO"].sum())
)
print(
    "Registros sem atraso extremo:",
    int((~periodo["ATRASO_EXTREMO"]).sum())
)
print("Arquivo salvo em:", saida)
