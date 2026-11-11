
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent

ARQUIVO_DENGUE = (
    RAIZ / "resultados/municipios_dengue_por_ano.csv"
)

ARQUIVO_POPULACAO = (
    RAIZ / "dados/processados/populacao_ceara_historica.csv"
)

SAIDA = (
    RAIZ / "resultados/taxas_dengue_municipios_2016_2025.csv"
)


def main():
    dengue = pd.read_csv(
        ARQUIVO_DENGUE,
        dtype={"CODIGO_MUNICIPIO": str}
    )

    populacao = pd.read_csv(
        ARQUIVO_POPULACAO,
        dtype={"CODIGO_IBGE": str}
    )

    # Padroniza os códigos municipais para seis dígitos.
    dengue["CODIGO_MUNICIPIO"] = (
        dengue["CODIGO_MUNICIPIO"].str.zfill(6)
    )

    populacao["CODIGO_MUNICIPIO"] = (
        populacao["CODIGO_IBGE"].str[:6]
    )

    # Verifica a integridade das chaves.
    assert not dengue.duplicated(
        ["CODIGO_MUNICIPIO", "ANO_SINTOMAS"]
    ).any()

    assert not populacao.duplicated(
        ["CODIGO_MUNICIPIO", "ANO"]
    ).any()

    assert len(dengue) == 1840
    assert len(populacao) == 1840

    # Relaciona município e ano.
    resultado = dengue.merge(
        populacao[
            ["CODIGO_MUNICIPIO", "ANO", "POPULACAO"]
        ],
        left_on=["CODIGO_MUNICIPIO", "ANO_SINTOMAS"],
        right_on=["CODIGO_MUNICIPIO", "ANO"],
        how="left",
        validate="one_to_one",
        indicator=True
    )

    # Nenhum município-ano pode ficar sem população.
    assert (resultado["_merge"] == "both").all()
    assert resultado["POPULACAO"].notna().all()
    assert (resultado["POPULACAO"] > 0).all()

    resultado["TAXA_100MIL"] = (
        resultado["TOTAL_REGISTROS"]
        / resultado["POPULACAO"]
        * 100000
    ).round(2)

    resultado = resultado[
        [
            "CODIGO_MUNICIPIO",
            "MUNICIPIO",
            "ANO_SINTOMAS",
            "TOTAL_REGISTROS",
            "POPULACAO",
            "TAXA_100MIL"
        ]
    ]

    resultado = resultado.sort_values(
        ["ANO_SINTOMAS", "CODIGO_MUNICIPIO"]
    ).reset_index(drop=True)

    assert len(resultado) == 1840

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    resultado.to_csv(
        SAIDA,
        index=False,
        encoding="utf-8-sig"
    )

    print("Cruzamento concluído!")
    print("Municípios:", resultado["CODIGO_MUNICIPIO"].nunique())
    print("Anos:", resultado["ANO_SINTOMAS"].nunique())
    print("Registros:", len(resultado))
    print("Total de registros de dengue:", resultado["TOTAL_REGISTROS"].sum())
    print("\nPrimeiras linhas:")
    print(resultado.head(10).to_string(index=False))
    print("\nArquivo gerado:", SAIDA)


if __name__ == "__main__":
    main()
