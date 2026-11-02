
from pathlib import Path
import pandas as pd

pasta = Path("dados/originais")

colunas_8 = [
    "ID_AGRAVO",
    "DT_NOTIFIC",
    "NU_ANO",
    "DT_SIN_PRI",
    "SG_UF",
    "ID_MN_RESI",
    "CLASSI_FIN",
    "CRITERIO"
]

colunas_12 = colunas_8 + [
    "NU_IDADE_N",
    "CS_SEXO",
    "ID_UNIDADE",
    "ID_MUNICIP"
]

resultados = []

for ano in range(2016, 2026):
    arquivo = pasta / f"DENGBR{str(ano)[-2:]}.csv"

    partes = []

    # Leitura em blocos para economizar memória
    for bloco in pd.read_csv(
        arquivo,
        usecols=colunas_12,
        dtype="string",
        chunksize=100000
    ):
        ce = bloco[bloco["SG_UF"] == "23"].copy()
        partes.append(ce)

    base = pd.concat(partes, ignore_index=True)

    repetidos_8 = base.duplicated(
        subset=colunas_8,
        keep=False
    ).sum()

    repetidos_12 = base.duplicated(
        subset=colunas_12,
        keep=False
    ).sum()

    resultados.append({
        "arquivo": ano,
        "total_registros": len(base),
        "repeticoes_8": int(repetidos_8),
        "repeticoes_12": int(repetidos_12)
    })

    print(
        f"{ano}: {len(base)} registros | "
        f"8 campos: {repetidos_8} | "
        f"12 campos: {repetidos_12}"
    )

# Consolida os resultados
tabela = pd.DataFrame(resultados)

# Salva relatório
saida = Path("resultados/repeticoes_historicas_2016_2025.csv")
saida.parent.mkdir(parents=True, exist_ok=True)

tabela.to_csv(
    saida,
    index=False,
    encoding="utf-8-sig"
)

print("\nTOTAL:")
print(tabela[[
    "total_registros",
    "repeticoes_8",
    "repeticoes_12"
]].sum().to_string())

print("\nRelatório salvo em:", saida)
