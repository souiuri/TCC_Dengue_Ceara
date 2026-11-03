
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

entrada = Path("resultados/serie_historica_mensal.csv")
saida = Path("resultados/graficos/serie_mensal_2016_2025.png")

serie = pd.read_csv(entrada)

# Constrói a data de referência de cada mês
serie["DATA"] = pd.to_datetime(
    dict(
        year=serie["ANO_SINTOMAS"],
        month=serie["MES_SINTOMAS"],
        day=1
    )
)

serie = serie.sort_values("DATA")

# Cria o gráfico
fig, ax = plt.subplots(figsize=(14, 5))

ax.plot(
    serie["DATA"],
    serie["REGISTROS"],
    linewidth=1.8
)

ax.set_title(
    "Registros classificados como dengue no Ceará (2016–2025)"
)
ax.set_xlabel("Ano de início dos sintomas")
ax.set_ylabel("Número de registros")

ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

ax.grid(True, alpha=0.3)

fig.tight_layout()

saida.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(saida, dpi=300)
plt.close(fig)

# Identifica o mês com maior número de registros
pico = serie.loc[serie["REGISTROS"].idxmax()]

print("Gráfico gerado com sucesso!")
print("Arquivo:", saida)

print(
    "Mês com maior número de registros:",
    f"{int(pico['MES_SINTOMAS']):02d}/{int(pico['ANO_SINTOMAS'])}"
)
print("Registros nesse mês:", int(pico["REGISTROS"]))
