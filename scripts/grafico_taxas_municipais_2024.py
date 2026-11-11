
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent

ENTRADA = (
    RAIZ / "resultados/taxas_dengue_municipios_2016_2025.csv"
)

SAIDA = (
    RAIZ / "resultados/graficos/top10_taxas_dengue_2024.png"
)


def main():
    dados = pd.read_csv(ENTRADA)

    dados_2024 = dados[dados["ANO_SINTOMAS"] == 2024]

    top10 = dados_2024.nlargest(
        10, "TAXA_100MIL"
    ).sort_values("TAXA_100MIL")

    fig, ax = plt.subplots(figsize=(11, 6))

    barras = ax.barh(
        top10["MUNICIPIO"],
        top10["TAXA_100MIL"],
        color="#2563eb"
    )

    ax.bar_label(
        barras,
        fmt="%.1f",
        padding=4,
        fontsize=9
    )

    ax.set_title(
        "Ceará — 10 maiores taxas municipais de dengue (2024)"
    )

    ax.set_xlabel(
        "Registros classificados por 100 mil habitantes"
    )

    ax.set_xlim(0, top10["TAXA_100MIL"].max() * 1.18)

    ax.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()

    SAIDA.parent.mkdir(parents=True, exist_ok=True)

    fig.savefig(SAIDA, dpi=300, bbox_inches="tight")

    plt.close(fig)

    print("Gráfico gerado:", SAIDA)


if __name__ == "__main__":
    main()
