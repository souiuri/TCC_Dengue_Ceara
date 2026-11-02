
from pathlib import Path
import pandas as pd

pasta = Path("dados/originais")

colunas = [
    "ID_AGRAVO", "DT_NOTIFIC", "NU_ANO",
    "DT_SIN_PRI", "SG_UF", "ID_MN_RESI",
    "CLASSI_FIN", "CRITERIO",
    "NU_IDADE_N", "CS_SEXO",
    "ID_UNIDADE", "ID_MUNICIP"
]

partes = []

for ano in range(2016, 2026):
    arquivo = pasta / f"DENGBR{str(ano)[-2:]}.csv"

    for bloco in pd.read_csv(
        arquivo,
        usecols=colunas,
        dtype="string",
        chunksize=100000
    ):
        ce = bloco[bloco["SG_UF"] == "23"].copy()
        ce["arquivo_origem"] = ano
        partes.append(ce)

base = pd.concat(partes, ignore_index=True)

# Agrupa combinações de 12 campos
grupos = base.groupby(
    colunas,
    dropna=False
)["arquivo_origem"].nunique()

sobreposicoes = grupos[grupos > 1]

print("Total de registros:", len(base))
print(
    "Combinações presentes em arquivos diferentes:",
    len(sobreposicoes)
)
