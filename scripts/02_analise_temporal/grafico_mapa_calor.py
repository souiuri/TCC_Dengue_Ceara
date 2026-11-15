
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

entrada = Path("resultados/serie_historica_mensal.csv")
saida = Path("resultados/graficos/mapa_calor_2016_2025.png")

# Carrega a série histórica já validada
serie = pd.read_csv(entrada)

# Organiza os anos nas linhas e os meses nas colunas
matriz = serie.pivot(
    index="ANO_SINTOMAS",
    columns="MES_SINTOMAS",
    values="REGISTROS"
)

meses = [
    "Jan", "Fev", "Mar", "Abr",
    "Mai", "Jun", "Jul", "Ago",
    "Set", "Out", "Nov", "Dez"
]

# Cria o mapa de calor
fig, ax = plt.subplots(figsize=(13, 6))

imagem = ax.imshow(
    matriz.values,
    cmap="YlOrRd",
    aspect="auto"
)

ax.set_xticks(range(12))
ax.set_xticklabels(meses)

ax.set_yticks(range(len(matriz.index)))
ax.set_yticklabels(matriz.index)

ax.set_xlabel("Mês de início dos sintomas")
ax.set_ylabel("Ano")
ax.set_title(
    "Distribuição mensal dos registros de dengue no Ceará (2016–2025)"
)

barra = fig.colorbar(imagem, ax=ax)
barra.set_label("Número de registros")

fig.tight_layout()

saida.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(saida, dpi=300)
plt.close(fig)

print("Mapa de calor gerado com sucesso!")
print("Arquivo:", saida)
print("Dimensões da matriz:", matriz.shape)
print("Total de registros:", int(matriz.values.sum()))
