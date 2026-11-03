
from pathlib import Path
import pandas as pd

entrada = Path("resultados/serie_historica_mensal.csv")

serie = pd.read_csv(entrada)

# Calcula a média mensal ao longo dos 10 anos
sazonalidade = (
    serie.groupby("MES_SINTOMAS")["REGISTROS"]
    .agg(["sum", "mean"])
    .reset_index()
)

sazonalidade.columns = [
    "MES",
    "TOTAL_REGISTROS",
    "MEDIA_MENSAL"
]

nomes_meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

sazonalidade["NOME_MES"] = (
    sazonalidade["MES"].map(nomes_meses)
)

print("Sazonalidade da dengue no Ceará (2016–2025):")

print(
    sazonalidade[
        ["NOME_MES", "TOTAL_REGISTROS", "MEDIA_MENSAL"]
    ].to_string(index=False)
)

print("\nMês com maior média de registros:")

pico = sazonalidade.loc[
    sazonalidade["MEDIA_MENSAL"].idxmax()
]

print(pico["NOME_MES"])
print("Média:", round(pico["MEDIA_MENSAL"], 1))
