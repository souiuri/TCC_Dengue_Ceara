
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "resultados/taxas_dengue_municipios_2016_2025.csv"
SAIDA = RAIZ / "resultados/graficos/comparativo_brejo_ceara_2016_2025.png"

dados = pd.read_csv(ENTRADA)

ceara = dados.groupby("ANO_SINTOMAS").agg(
    registros=("TOTAL_REGISTROS", "sum"),
    populacao=("POPULACAO", "sum")
)
ceara["taxa"] = ceara["registros"] / ceara["populacao"] * 100000

brejo = dados[
    dados["MUNICIPIO"].str.upper() == "BREJO SANTO"
].set_index("ANO_SINTOMAS")

fig, ax = plt.subplots(figsize=(11, 6))

ax.plot(
    ceara.index,
    ceara["taxa"],
    marker="o",
    linewidth=2,
    label="Ceará"
)

ax.plot(
    brejo.index,
    brejo["TAXA_100MIL"],
    marker="o",
    linewidth=2,
    label="Brejo Santo"
)

ax.set_title("Taxas de dengue — Brejo Santo e Ceará (2016–2025)")
ax.set_xlabel("Ano de início dos sintomas")
ax.set_ylabel("Registros classificados por 100 mil habitantes")
ax.set_xticks(range(2016, 2026))
ax.grid(alpha=0.25)
ax.legend()

fig.tight_layout()

SAIDA.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(SAIDA, dpi=300, bbox_inches="tight")
plt.close(fig)

print("Gráfico gerado:", SAIDA)
