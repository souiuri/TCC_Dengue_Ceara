
from pathlib import Path
import pandas as pd

pasta = Path(__file__).resolve().parent.parent / "dados" / "originais"

colunas_necessarias = [
    "NU_ANO",
    "DT_NOTIFIC",
    "DT_SIN_PRI",
    "SG_UF",
    "ID_MN_RESI",
    "CLASSI_FIN",
    "CRITERIO",
    "ID_AGRAVO"
]

for ano in range(2016, 2026):
    arquivo = pasta / f"DENGBR{str(ano)[-2:]}.csv"

    df = pd.read_csv(arquivo, nrows=0)

    faltando = [
        coluna
        for coluna in colunas_necessarias
        if coluna not in df.columns
    ]

    if faltando:
        print(f"{ano}: FALTANDO {faltando}")
    else:
        print(f"{ano}: OK - todas as colunas encontradas")