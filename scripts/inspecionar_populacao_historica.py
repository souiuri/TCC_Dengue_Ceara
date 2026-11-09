
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "dados/originais/populacao"

arquivos = sorted(PASTA.glob("POP20*.xls"))

for arquivo in arquivos:
    print(f"\n{'=' * 60}")
    print("ARQUIVO:", arquivo.name)

    try:
        excel = pd.ExcelFile(arquivo, engine="xlrd")

        print("ABAS:", excel.sheet_names)

        for aba in excel.sheet_names:
            dados = pd.read_excel(
                excel,
                sheet_name=aba,
                header=None,
                nrows=5
            )

            print(f"\nABA: {aba}")
            print(dados.to_string(index=False, header=False))

    except Exception as erro:
        print("ERRO:", erro)
