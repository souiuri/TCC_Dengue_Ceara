
from pathlib import Path
import pandas as pd

pasta_entrada = Path("dados/processados")
arquivo_saida = pasta_entrada / "dengue_ceara_2016_2025.csv"

bases = []

for ano in range(2016, 2026):
    arquivo = pasta_entrada / f"DENGBR{str(ano)[-2:]}_CE.csv"

    print(f"Lendo arquivo de {ano}...")

    df = pd.read_csv(
        arquivo,
        dtype="string"
    )

    # Identifica de qual arquivo veio o registro
    df["ARQUIVO_ORIGEM"] = ano

    bases.append(df)

# Reúne os dez arquivos
base_historica = pd.concat(
    bases,
    ignore_index=True
)

# Salva a base consolidada
base_historica.to_csv(
    arquivo_saida,
    index=False,
    encoding="utf-8-sig"
)

print("\nConsolidação concluída!")
print("Total de registros:", len(base_historica))
print("Total de colunas:", len(base_historica.columns))
print("Arquivo salvo em:", arquivo_saida)

print("\nRegistros por arquivo de origem:")
print(
    base_historica["ARQUIVO_ORIGEM"]
    .value_counts()
    .sort_index()
    .to_string()
)

print("\nValores de SG_UF:")
print(
    base_historica["SG_UF"]
    .value_counts(dropna=False)
    .to_string()
)

print("\nRegistros completamente repetidos:")
print(
    base_historica.duplicated().sum()
)
