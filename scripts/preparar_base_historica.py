from pathlib import Path
import pandas as pd

# Pasta do projeto e dos arquivos originais
PASTA_PROJETO = Path(__file__).resolve().parent.parent
PASTA_ORIGINAIS = PASTA_PROJETO / "dados" / "originais"
PASTA_PROCESSADOS = PASTA_PROJETO / "dados" / "processados"

# Teste inicial: um arquivo. Depois ampliaremos para os dez anos.
ARQUIVO = PASTA_ORIGINAIS / "DENGBR25.csv"

# Códigos IBGE dos estados: Ceará = 23; Rio de Janeiro = 33
ESTADOS = {"23", "33"}

COLUNAS = [
    "NU_ANO",
    "DT_NOTIFIC",
    "DT_SIN_PRI",
    "SG_UF",
    "ID_MN_RESI",
    "CLASSI_FIN",
]

def processar_arquivo(caminho):
    PASTA_PROCESSADOS.mkdir(parents=True, exist_ok=True)
    saida = PASTA_PROCESSADOS / f"{caminho.stem}_CE_RJ.csv"

    total_lido = 0
    total_filtrado = 0
    primeira_parte = True

    for bloco in pd.read_csv(
        caminho,
        dtype=str,
        usecols=lambda coluna: coluna in COLUNAS,
        chunksize=100_000,
        low_memory=False,
    ):
        total_lido += len(bloco)

        # Mantém apenas registros dos dois estados
        bloco = bloco[bloco["SG_UF"].isin(ESTADOS)].copy()

        if bloco.empty:
            continue

        total_filtrado += len(bloco)

        bloco.to_csv(
            saida,
            index=False,
            mode="w" if primeira_parte else "a",
            header=primeira_parte,
        )
        primeira_parte = False

    print(f"Arquivo lido: {caminho.name}")
    print(f"Registros lidos: {total_lido:,}")
    print(f"Registros de CE e RJ: {total_filtrado:,}")
    print(f"Arquivo gerado: {saida}")

if __name__ == "__main__":
    processar_arquivo(ARQUIVO)