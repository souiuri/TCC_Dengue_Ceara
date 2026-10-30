
import pandas as pd
from pathlib import Path

projeto = Path(__file__).resolve().parent.parent
arquivo = projeto / "dados" / "dengue_ceara_2024.csv"

df = pd.read_csv(arquivo, dtype=str)

# Considerar apenas registros de 2024
df = df[df["NU_ANO"] == "2024"].copy()

# Contar registros por código de município
municipios = (
    df.groupby("ID_MN_RESI")
    .size()
    .sort_values(ascending=False)
    .reset_index(name="quantidade")
)

print("=== 10 MUNICÍPIOS COM MAIS REGISTROS ===")
print(municipios.head(10).to_string(index=False))

# Salvar a tabela completa
saida = projeto / "resultados" / "municipios_dengue_2024.csv"
municipios.to_csv(saida, index=False, encoding="utf-8-sig")

print("\nTabela salva em:", saida)