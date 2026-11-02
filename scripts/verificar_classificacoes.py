
from pathlib import Path
import pandas as pd

pasta = Path(__file__).resolve().parent.parent / "dados" / "processados"

for ano in range(2016, 2026):
    arquivo = pasta / f"DENGBR{str(ano)[-2:]}_CE.csv"

    df = pd.read_csv(
        arquivo,
        dtype=str,
        usecols=["CLASSI_FIN"]
    )

    print(f"\nArquivo {ano}")
    print(df["CLASSI_FIN"].value_counts(dropna=False))
