
from pathlib import Path
import pandas as pd

PASTA_DADOS = Path("dados/processados")
resultados = []

for ano in range(2016, 2026):
    nome_arquivo = f"DENGBR{str(ano)[-2:]}_CE.csv"
    caminho = PASTA_DADOS / nome_arquivo

    dados = pd.read_csv(
        caminho,
        usecols=["CLASSI_FIN", "CRITERIO"],
        dtype=str
    )

    # Seleciona os registros classificados como dengue
    casos_dengue = dados[
        dados["CLASSI_FIN"].isin(["10", "11", "12"])
    ]

    # Conta os critérios, incluindo valores ausentes
    contagem = casos_dengue["CRITERIO"].value_counts(
        dropna=False
    )
    resultados.append({
    "arquivo_ano": ano,
    "laboratorial": int(contagem.get("1", 0)),
    "clinico_epidemiologico": int(contagem.get("2", 0)),
    "em_investigacao": int(contagem.get("3", 0)),
    "total_dengue": len(casos_dengue)
    })

    print(f"\n--- Arquivo {ano} ---")
    print(f"Registros classificados como dengue: {len(casos_dengue)}")
    print(contagem)

# Organiza os resultados em uma tabela
resumo = pd.DataFrame(resultados)

# Calcula os totais de todas as colunas numéricas
totais = resumo[
    ["laboratorial", "clinico_epidemiologico",
     "em_investigacao", "total_dengue"]
].sum()

print("\n=== RESUMO HISTÓRICO ===")
print(resumo.to_string(index=False))

print("\n=== TOTAIS ===")
print(totais)

# Salva o relatório para consultas posteriores
resumo.to_csv(
    "resultados/criterios_dengue_2016_2025.csv",
    index=False
)