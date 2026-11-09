
from pathlib import Path
from numbers import Real
import re
import unicodedata
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
ORIGEM = RAIZ / "dados/originais/populacao"
SAIDA = RAIZ / "dados/processados/populacao_ceara_historica.csv"

TOTAIS_CONHECIDOS = {
    2016: 8963663,
    2017: 9020460,
    2018: 9075649,
    2019: 9132078,
    2020: 9187103,
    2021: 9240580,
    2023: 8794957,
    2024: 9233656,
    2025: 9268836,
}


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", str(texto))
    texto = "".join(
        caractere for caractere in texto
        if not unicodedata.combining(caractere)
    )
    return texto.strip().upper()


def localizar_aba(abas, termo):
    for aba in abas:
        if termo in normalizar(aba):
            return aba

    raise ValueError(f"Aba não encontrada: {termo}")


def converter_populacao(valor):
    if pd.isna(valor):
        return None

    if isinstance(valor, Real):
        numero = float(valor)
        return int(numero) if numero.is_integer() else None

    texto = str(valor).strip()

    # Remove notas de rodapé do IBGE.
    texto = re.sub(
        r"\s*\(\s*(?:\d+|\*)\s*\)$",
        "",
        texto
    ).strip()

    if re.fullmatch(r"\d{1,3}(?:\.\d{3})+", texto):
        texto = texto.replace(".", "")

    if not texto.isdigit():
        return None

    return int(texto)


def processar_arquivo(arquivo):
    correspondencia = re.search(r"POP(20\d{2})", arquivo.name)

    if not correspondencia:
        raise ValueError(f"Ano não identificado: {arquivo.name}")

    ano = int(correspondencia.group(1))

    excel = pd.ExcelFile(arquivo, engine="xlrd")

    aba_municipios = localizar_aba(
        excel.sheet_names, "MUNICIPIOS"
    )

    dados = pd.read_excel(
        excel,
        sheet_name=aba_municipios,
        header=1,
        dtype={
            "COD. UF": str,
            "COD. MUNIC": str
        }
    )

    dados = dados[
        dados["COD. UF"].str.strip().str.zfill(2) == "23"
    ].copy()

    dados["CODIGO_IBGE"] = (
        dados["COD. UF"].str.strip().str.zfill(2)
        + dados["COD. MUNIC"].str.strip().str.zfill(5)
    )

    # O arquivo de 2023 possui um cabeçalho diferente.
    coluna_populacao = (
        "POPULAÇÃO"
        if ano == 2023
        else "POPULAÇÃO ESTIMADA"
    )

    dados["POPULACAO"] = dados[
        coluna_populacao
    ].apply(converter_populacao)

    invalidos = dados[dados["POPULACAO"].isna()]

    if not invalidos.empty:
        print(f"\n{ano}: populações não convertidas:")
        print(
            invalidos[
                [
                    "COD. MUNIC",
                    "NOME DO MUNICÍPIO",
                    coluna_populacao
                ]
            ].to_string(index=False)
        )

    resultado = dados[
        ["CODIGO_IBGE", "NOME DO MUNICÍPIO", "POPULACAO"]
    ].rename(
        columns={"NOME DO MUNICÍPIO": "MUNICIPIO"}
    ).copy()

    resultado.insert(1, "ANO", ano)

    assert len(resultado) == 184, (
        f"{ano}: quantidade incorreta de municípios"
    )

    assert resultado["CODIGO_IBGE"].nunique() == 184, (
        f"{ano}: códigos IBGE duplicados"
    )

    assert resultado["CODIGO_IBGE"].str.fullmatch(
        r"23\d{5}"
    ).all(), f"{ano}: códigos IBGE inválidos"

    assert resultado["POPULACAO"].notna().all(), (
        f"{ano}: existem populações não convertidas"
    )

    assert (resultado["POPULACAO"] > 0).all(), (
        f"{ano}: existem populações inválidas"
    )

    populacao_calculada = int(
        resultado["POPULACAO"].sum()
    )

    if ano != 2023:
        # Nos demais anos, confere com a aba estadual.
        aba_estados = localizar_aba(
            excel.sheet_names, "BRASIL"
        )

        estados = pd.read_excel(
            excel,
            sheet_name=aba_estados,
            header=1
        )

        primeira_coluna = estados.iloc[:, 0].map(normalizar)
        linha_ceara = estados[primeira_coluna == "CEARA"]

        assert len(linha_ceara) == 1, (
            f"{ano}: Ceará não encontrado na tabela estadual"
        )

        colunas_populacao = [
            coluna for coluna in estados.columns
            if "POPULACAO ESTIMADA" in normalizar(coluna)
        ]

        assert len(colunas_populacao) == 1, (
            f"{ano}: coluna estadual não identificada"
        )

        valor_original = linha_ceara.iloc[0][
            colunas_populacao[0]
        ]

        populacao_oficial = converter_populacao(
            valor_original
        )

        assert populacao_oficial is not None, (
            f"{ano}: população estadual inválida: "
            f"{valor_original}"
        )

        assert populacao_calculada == populacao_oficial, (
            f"{ano}: soma municipal {populacao_calculada} "
            f"difere do total estadual {populacao_oficial}"
        )

    # Verificação independente dos totais conhecidos.
    if ano in TOTAIS_CONHECIDOS:
        esperado = TOTAIS_CONHECIDOS[ano]

        assert populacao_calculada == esperado, (
            f"{ano}: população {populacao_calculada} "
            f"diferente da referência {esperado}"
        )

    resultado["POPULACAO"] = resultado[
        "POPULACAO"
    ].astype(int)

    print(
        f"{ano}: 184 municípios | "
        f"População: {populacao_calculada:,} | "
        f"Validação: OK"
    )

    return resultado


def processar_censo_2022():
    arquivo = ORIGEM / "tabela4714(1).xlsx"

    dados = pd.read_excel(
        arquivo,
        sheet_name="Tabela",
        header=None,
        skiprows=4,
        engine="openpyxl",
        dtype={1: str}
    )

    municipios = dados[
        (dados[0] == "MU")
        & dados[1].str.fullmatch(r"23\d{5}", na=False)
    ].copy()

    resultado = pd.DataFrame({
        "CODIGO_IBGE": municipios[1],
        "ANO": 2022,
        "MUNICIPIO": municipios[2].str.replace(
            r"\s*\(CE\)$", "", regex=True
        ),
        "POPULACAO": pd.to_numeric(
            municipios[3], errors="coerce"
        )
    })

    assert len(resultado) == 184
    assert resultado["CODIGO_IBGE"].nunique() == 184
    assert resultado["POPULACAO"].notna().all()
    assert (resultado["POPULACAO"] > 0).all()
    assert (resultado["POPULACAO"] % 1 == 0).all()

    total = int(resultado["POPULACAO"].sum())

    assert total == 8794957, (
        f"2022: população inesperada: {total}"
    )

    resultado["POPULACAO"] = resultado[
        "POPULACAO"
    ].astype(int)

    print(
        f"2022: 184 municípios | "
        f"População: {total:,} | "
        f"Validação: OK"
    )

    return resultado

def main():
    arquivos = sorted(ORIGEM.glob("POP20*.xls*"))

    if not arquivos:
        raise FileNotFoundError(
            "Nenhum arquivo populacional encontrado."
        )

    resultados = []

    for arquivo in arquivos:
        if not re.search(r"POP20\d{2}", arquivo.name):
            continue

        resultados.append(processar_arquivo(arquivo))

    if not resultados:
        raise ValueError(
            "Nenhum arquivo válido foi processado."
        )
    
    resultados.append(processar_censo_2022())

    historico = pd.concat(
        resultados,
        ignore_index=True
    )

    assert not historico.duplicated(
        ["CODIGO_IBGE", "ANO"]
    ).any(), "Existem municípios duplicados no mesmo ano."

    anos = sorted(
        historico["ANO"].unique().tolist()
    )

    assert len(historico) == 184 * len(anos), (
        "Quantidade de registros inconsistente."
    )

    historico = historico.sort_values(
        ["ANO", "CODIGO_IBGE"]
    ).reset_index(drop=True)

    SAIDA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    historico.to_csv(
        SAIDA,
        index=False,
        encoding="utf-8-sig"
    )

    print("\nAnos processados:", anos)
    print("Municípios por ano: 184")
    print("Total de linhas:", len(historico))
    print("Arquivo gerado:", SAIDA)
    print("Consolidação concluída com sucesso!")


if __name__ == "__main__":
    main()
