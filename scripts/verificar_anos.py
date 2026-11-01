
from pathlib import Path
import pandas as pd

PASTA_PROJETO = Path(__file__).resolve().parent.parent
PASTA_DADOS = PASTA_PROJETO / "dados" / "processados"

for ano in range(2016, 2026):
    arquivo = PASTA_DADOS / f"DENGBR{str(ano)[-2:]}_CE.csv"

    df = pd.read_csv(
        arquivo,
        dtype=str,
        usecols=["DT_SIN_PRI"]
    )

    datas = pd.to_datetime(df["DT_SIN_PRI"], errors="coerce")
    contagem = datas.dt.year.value_counts().sort_index()

    print(f"\nArquivo: {arquivo.name}")
    print(contagem.to_string())
    print(f"Datas ausentes ou inválidas: {datas.isna().sum()}")