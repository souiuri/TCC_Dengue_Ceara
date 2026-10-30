
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

projeto = Path(__file__).resolve().parent.parent
arquivo = projeto / "dados" / "dengue_ceara_2024.csv"
pasta_graficos = projeto / "resultados" / "graficos"
pasta_graficos.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(arquivo, dtype=str)
df = df[df["NU_ANO"] == "2024"].copy()

# Códigos municipais conferidos na tabela do IBGE
nomes = {
    "230440": "Fortaleza",
    "230250": "Brejo Santo",
    "231110": "Porteiras",
    "230370": "Caucaia",
    "230420": "Crato",
    "231330": "Tauá",
    "230730": "Juazeiro do Norte",
    "231060": "Penaforte",
    "231340": "Tianguá",
    "230465": "Graça",
}

contagem = (
    df.groupby("ID_MN_RESI")
    .size()
    .sort_values(ascending=False)
    .head(10)
    .rename_axis("codigo")
    .reset_index(name="registros")
)

contagem["municipio"] = contagem["codigo"].map(nomes)
contagem["municipio"] = contagem["municipio"].fillna(
    contagem["codigo"]
)
contagem = contagem.sort_values("registros")

plt.figure(figsize=(10, 6))
plt.barh(contagem["municipio"], contagem["registros"])
plt.title("Dez municípios com mais registros de dengue — Ceará, 2024")
plt.xlabel("Quantidade de registros")
plt.ylabel("Município")
plt.tight_layout()

saida = pasta_graficos / "top10_municipios_dengue_2024.png"
plt.savefig(saida, dpi=300)
plt.show()

print("Gráfico salvo em:", saida)
print(contagem[["municipio", "registros"]].to_string(index=False))