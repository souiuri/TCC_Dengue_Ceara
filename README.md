# Análise Temporal e Espacial da Dengue no Ceará com Python

Projeto de Trabalho de Conclusão de Curso (TCC) em Ciência da Computação, voltado à análise de dados epidemiológicos de dengue no estado do Ceará, utilizando Python e dados públicos do Ministério da Saúde.

## Objetivo

Investigar a evolução temporal e a distribuição espacial dos registros de dengue no Ceará entre 2016 e 2025, considerando notificações e casos confirmados, com foco na identificação de padrões sazonais e tendências ao longo do período.

### Objetivos específicos

- Organizar e processar as bases históricas de dengue.
- Avaliar a qualidade dos dados, identificando datas inconsistentes, informações ausentes e possíveis duplicidades.
- Identificar os registros classificados como casos confirmados, conforme a documentação oficial.
- Analisar a distribuição anual e mensal das notificações e dos casos confirmados.
- Investigar a distribuição dos registros entre os municípios cearenses.
- Aplicar técnicas de análise de séries temporais para identificar tendências e padrões sazonais.

## Tecnologias

- Python
- pandas
- Matplotlib
- Git e GitHub

## Estrutura do projeto

```text
TCC_Dengue_Ceara/
├── dados/
│   ├── originais/
│   └── processados/
├── scripts/
│   ├── preparar_base_historica.py
│   ├── verificar_anos.py
│   └── verificar_intervalos.py
├── resultados/
│   └── graficos/
├── .gitignore
└── README.md
```

A estrutura acima apresenta os principais diretórios e scripts utilizados ou preparados até o momento, não necessariamente todos os arquivos do repositório.

## Fonte dos dados

Ministério da Saúde — Portal de Dados Abertos.

[Base de dados de arboviroses — Dengue](https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue)

O projeto utiliza os arquivos históricos `DENGBR16.csv` até `DENGBR25.csv`.

As bases originais e os arquivos processados são armazenados localmente na pasta `dados/`, que não é incluída no GitHub devido ao volume dos arquivos.

## Metodologia

A pesquisa está organizada em cinco etapas:

1. **Preparação:** leitura dos arquivos históricos e filtragem dos registros de residentes no Ceará, identificados pelo código `SG_UF = 23`.
2. **Validação:** investigação de datas inconsistentes, registros ausentes e possíveis duplicidades.
3. **Classificação:** identificação das notificações e dos casos confirmados, conforme os critérios oficiais.
4. **Análise exploratória:** investigação da distribuição anual, mensal e municipal dos registros.
5. **Análise de tendências:** aplicação de técnicas estatísticas para investigar a evolução temporal e a sazonalidade da dengue.

A data dos primeiros sintomas (`DT_SIN_PRI`) será utilizada como referência principal para a análise temporal, sujeita aos critérios de validação dos dados.

## Progresso do projeto

### Etapas concluídas

- Organização do ambiente e do repositório GitHub.
- Obtenção das dez bases históricas de 2016 a 2025.
- Desenvolvimento do processamento em blocos com pandas.
- Filtragem dos registros do Ceará nos dez arquivos.
- Produção de gráficos exploratórios preliminares referentes a 2024.
- Investigação inicial da consistência das datas.

O processamento identificou **416.095 registros nos dez arquivos**, antes da consolidação, deduplicação e aplicação dos critérios definitivos de validação.

### Etapas em andamento

- Avaliação da qualidade das datas nos dez arquivos.
- Investigação de possíveis registros duplicados.
- Definição dos critérios para identificação de casos confirmados.
- Consolidação da base histórica.

### Próximas etapas

- Análise descritiva das notificações e dos casos confirmados.
- Análise temporal e espacial dos registros.
- Cálculo de taxas considerando a população.
- Análise de tendências e sazonalidade.
- Redação e discussão dos resultados do artigo científico.

## Status

**Em desenvolvimento.**

Os resultados apresentados são preliminares e não devem ser interpretados como contagens definitivas de casos confirmados, incidência ou tendências epidemiológicas sem a validação dos dados e dos critérios metodológicos.