
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# Caminhos dos arquivos
RAIZ = Path(__file__).resolve().parent.parent

ENTRADA = RAIZ / "resultados/municipios_dengue_2016_2025.csv"
SAIDA = RAIZ / "resultados/graficos/top10_municipios_2016_2025.png"


# Carregar os dados consolidados
base = pd.read_csv(ENTRADA)

top10 = base.nlargest(10, "TOTAL_REGISTROS")
top10 = top10.sort_values("TOTAL_REGISTROS")


# Construir o gráfico
fig, ax = plt.subplots(figsize=(11, 6))

barras = ax.barh(
    top10["MUNICIPIO"],
    top10["TOTAL_REGISTROS"],
    color="#2878B5"
)

ax.bar_label(
    barras,
    labels=[
        f"{valor:,.0f}".replace(",", ".")
        for valor in top10["TOTAL_REGISTROS"]
    ],
    padding=4
)

ax.set_title(
    "Municípios com mais registros de dengue no Ceará (2016–2025)",
    fontsize=13,
    pad=15
)

ax.set_xlabel("Quantidade de registros")
ax.set_ylabel("Município")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.set_xlim(0, top10["TOTAL_REGISTROS"].max() * 1.15)

ax.grid(axis="x", alpha=0.2)
ax.set_axisbelow(True)

plt.tight_layout()


# Salvar a figura
SAIDA.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(SAIDA, dpi=300, bbox_inches="tight")
plt.close()

print("\nGráfico gerado com sucesso!")
print(f"Arquivo: {SAIDA}")
