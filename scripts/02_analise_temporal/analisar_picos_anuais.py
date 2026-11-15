
import pandas as pd

serie = pd.read_csv(
    "resultados/serie_historica_mensal.csv"
)

nomes_meses = {
    1: "Janeiro", 2: "Fevereiro",
    3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho",
    7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro",
    11: "Novembro", 12: "Dezembro"
}

# Identifica o mês de maior registro em cada ano
indices = serie.groupby("ANO_SINTOMAS")[
    "REGISTROS"
].idxmax()

picos = serie.loc[
    indices,
    ["ANO_SINTOMAS", "MES_SINTOMAS", "REGISTROS"]
].copy()

picos["MES"] = picos["MES_SINTOMAS"].map(nomes_meses)

print("Picos mensais por ano:")
print(
    picos[
        ["ANO_SINTOMAS", "MES", "REGISTROS"]
    ].to_string(index=False)
)

print("\nFrequência dos meses de pico:")
print(
    picos["MES"]
    .value_counts()
    .to_string()
)
