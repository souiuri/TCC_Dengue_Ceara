
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Localizar as pastas do projeto
projeto = Path(__file__).resolve().parent.parent
arquivo = projeto / "dados" / "dengue_ceara_2024.csv"
pasta_graficos = projeto / "resultados" / "graficos"

pasta_graficos.mkdir(parents=True, exist_ok=True)

# Ler os dados filtrados
df = pd.read_csv(arquivo, dtype=str)

# Manter somente o ano de 2024
df = df[df["NU_ANO"] == "2024"].copy()

# Converter as datas
df["DT_NOTIFIC"] = pd.to_datetime(
    df["DT_NOTIFIC"], errors="coerce"
)

# Contar notificações por mês
df["MES"] = df["DT_NOTIFIC"].dt.month

contagem = (
    df.groupby("MES")
    .size()
    .reindex(range(1, 13), fill_value=0)
)

nomes_meses = [
    "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
    "Jul", "Ago", "Set", "Out", "Nov", "Dez"
]

# Criar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(
    nomes_meses,
    contagem.values,
    marker="o"
)

plt.title("Notificações de dengue no Ceará — 2024")
plt.xlabel("Mês da notificação")
plt.ylabel("Quantidade de registros")
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Salvar o gráfico
saida = pasta_graficos / "notificacoes_dengue_2024.png"
plt.savefig(saida, dpi=300)
plt.show()

print("Total de registros de 2024:", len(df))
print("Gráfico salvo em:", saida)
print("\nQuantidade por mês:")
print(contagem)