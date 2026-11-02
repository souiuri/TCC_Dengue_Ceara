
from pathlib import Path
import pandas as pd

pasta = Path(__file__).resolve().parent.parent / "dados" / "processados"
resultados = []

for ano in range(2016, 2026):
    arquivo = pasta / f"DENGBR{str(ano)[-2:]}_CE.csv"

    df = pd.read_csv(
        arquivo,
        dtype=str,
        usecols=["DT_NOTIFIC", "DT_SIN_PRI"]
    )

    notificacao = pd.to_datetime(df["DT_NOTIFIC"], errors="coerce")
    sintomas = pd.to_datetime(df["DT_SIN_PRI"], errors="coerce")

    intervalo = (notificacao - sintomas).dt.days

    print(f"\nArquivo {ano}")
    print(f"Total: {len(df)}")
    print(f"Antes dos sintomas: {(intervalo < 0).sum()}")
    print(f"0 a 30 dias: {intervalo.between(0, 30).sum()}")
    print(f"31 a 365 dias: {intervalo.between(31, 365).sum()}")
    print(f"Mais de 365 dias: {(intervalo > 365).sum()}")
    print(f"Datas inválidas: {intervalo.isna().sum()}")
    resultados.append({
        "arquivo_ano": ano,
        "total": len(df),
        "antes_dos_sintomas": int((intervalo < 0).sum()),
        "ate_30_dias": int(intervalo.between(0, 30).sum()),
        "de_31_a_365_dias": int(intervalo.between(31, 365).sum()),
        "mais_de_365_dias": int((intervalo > 365).sum()),
        "datas_invalidas": int(intervalo.isna().sum())
    })
pasta_resultados = Path(__file__).resolve().parent.parent / "resultados"
pasta_resultados.mkdir(parents=True, exist_ok=True)

relatorio = pd.DataFrame(resultados)

saida = pasta_resultados / "qualidade_datas_2016_2025.csv"

relatorio.to_csv(saida, index=False)

print(f"\nRelatório salvo em: {saida}")
