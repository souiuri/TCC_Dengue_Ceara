
from pathlib import Path
import pandas as pd

entrada = Path("dados/processados/dengue_ceara_analitica.csv")
saida = Path("resultados/serie_historica_mensal.csv")

base = pd.read_csv(entrada)

# Ignora atrasos extremos somente nesta análise
base = base[base["ATRASO_EXTREMO"] == False].copy()

# Agrupa os registros por ano e mês dos sintomas
serie = (
    base.groupby(["ANO_SINTOMAS", "MES_SINTOMAS"])
    .size()
    .reset_index(name="REGISTROS")
)

# Garante a presença de todos os 120 meses do período
meses = pd.MultiIndex.from_product(
    [range(2016, 2026), range(1, 13)],
    names=["ANO_SINTOMAS", "MES_SINTOMAS"]
)

serie = (
    serie.set_index(["ANO_SINTOMAS", "MES_SINTOMAS"])
    .reindex(meses, fill_value=0)
    .reset_index()
)

saida.parent.mkdir(parents=True, exist_ok=True)
serie.to_csv(saida, index=False, encoding="utf-8-sig")

print("Registros utilizados:", len(base))
print("Meses analisados:", len(serie))

print("\nTotal de registros por ano:")
print(
    serie.groupby("ANO_SINTOMAS")["REGISTROS"]
    .sum()
    .to_string()
)

print("\nPrimeiros 12 meses:")
print(serie.head(12).to_string(index=False))

print("\nArquivo salvo em:", saida)
