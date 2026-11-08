
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent

ARQUIVO = RAIZ / "resultados/taxas_municipais_2025.csv"

dados = pd.read_csv(ARQUIVO)

total_registros = int(dados["TOTAL_REGISTROS"].sum())
populacao_total = int(dados["POPULACAO"].sum())

taxa_estadual = total_registros / populacao_total * 100000

taxas_recalculadas = (
    dados["TOTAL_REGISTROS"] / dados["POPULACAO"] * 100000
)

assert len(dados) == 184
assert dados["CODIGO_MUNICIPIO"].nunique() == 184
assert total_registros == 5048
assert populacao_total == 9268836
assert (dados["POPULACAO"] > 0).all()
assert (abs(dados["TAXA_100MIL"] - taxas_recalculadas) < 0.000001).all()

print("Municípios validados:", len(dados))
print("Total de registros:", total_registros)
print("População estadual:", populacao_total)
print(f"Taxa estadual: {taxa_estadual:.2f} por 100 mil habitantes")
print("Validação concluída com sucesso!")
