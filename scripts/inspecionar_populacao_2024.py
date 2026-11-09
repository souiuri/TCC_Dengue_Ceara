from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO = RAIZ / "dados/originais/populacao/POP2024_20241230.xls"

excel = pd.ExcelFile(ARQUIVO, engine="xlrd")

print("Planilhas:", excel.sheet_names)

for nome in excel.sheet_names:
    print(f"\nPlanilha: {nome}")
    dados = pd.read_excel(excel, sheet_name=nome, header=None, nrows=8)
    print(dados.to_string(index=True, header=False))