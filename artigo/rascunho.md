# Análise Temporal e Espacial da Dengue no Estado do Ceará entre 2016 e 2025 Utilizando Python

**Trabalho de Conclusão de Curso — Ciência da Computação**

**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) — Campus Maracanaú

**Situação:** Rascunho inicial do artigo científico

## Resumo

*A elaborar após a conclusão das análises e da discussão dos resultados.*

**Palavras-chave provisórias:** Dengue. Análise de Dados. Séries Temporais. Python. Saúde Pública.

## 1. Introdução

A dengue representa um importante desafio para a saúde pública brasileira, exigindo estratégias de vigilância epidemiológica e acompanhamento de sua distribuição ao longo do tempo e do espaço.

A disponibilidade de bases públicas de dados epidemiológicos permite o desenvolvimento de estudos computacionais voltados à investigação de padrões de ocorrência de doenças. Nesse contexto, ferramentas de programação e análise de dados podem contribuir para a organização, o processamento e a visualização de informações epidemiológicas.

Este trabalho propõe analisar os registros de dengue no estado do Ceará entre 2016 e 2025, considerando sua distribuição temporal e espacial, a distinção entre notificações e casos confirmados e a identificação de tendências ao longo do período.

### 1.1 Objetivo geral

Analisar a evolução temporal e a distribuição espacial dos registros de dengue no estado do Ceará entre 2016 e 2025, utilizando técnicas computacionais de processamento e análise de dados.

### 1.2 Objetivos específicos

- Processar e organizar os dados históricos de dengue.
- Avaliar a qualidade e a consistência dos registros.
- Identificar notificações e casos confirmados conforme critérios oficiais.
- Investigar a distribuição anual e mensal dos registros.
- Analisar a distribuição dos registros entre os municípios cearenses.
- Identificar tendências temporais e padrões sazonais.

## 2. Fundamentação teórica

*A desenvolver mediante levantamento bibliográfico.*

Temas previstos:

- Dengue e vigilância epidemiológica.
- Sistemas de informação em saúde.
- Qualidade de dados epidemiológicos.
- Análise exploratória de dados.
- Séries temporais e sazonalidade.

## 3. Metodologia

### 3.1 Caracterização da pesquisa

O estudo propõe uma abordagem quantitativa, de caráter observacional e retrospectivo, baseada na análise de dados secundários disponibilizados publicamente.

### 3.2 Fonte e período dos dados

Serão utilizados dados históricos de dengue disponibilizados pelo Ministério da Saúde, abrangendo os arquivos de origem de 2016 a 2025.

A área geográfica de interesse é o estado do Ceará, identificado pelo código 23 na variável `SG_UF`.

### 3.3 Ferramentas computacionais

O processamento será realizado em Python, com utilização da biblioteca pandas para manipulação de dados e Matplotlib para visualização gráfica.

### 3.4 Preparação dos dados

Os arquivos históricos são processados por meio de leitura em blocos, permitindo a manipulação de grandes volumes de registros.

A filtragem geográfica seleciona os registros referentes ao Ceará. As bases originais são preservadas separadamente dos arquivos processados.

### 3.5 Avaliação da qualidade dos dados

Será avaliada a consistência das datas de notificação (`DT_NOTIFIC`) e de início dos sintomas (`DT_SIN_PRI`), incluindo a identificação de intervalos inconsistentes, datas inválidas e registros potencialmente duplicados.

A definição dos critérios de inclusão e exclusão será documentada antes da consolidação da base analítica.

### 3.6 Análise temporal e espacial

A análise contemplará a distribuição anual e mensal das notificações e dos casos confirmados, além de comparações entre municípios, considerando dados populacionais quando aplicável.

### 3.7 Análise de tendências

Na etapa final, serão aplicadas técnicas de análise de séries temporais para investigar tendências e padrões sazonais. Os métodos estatísticos específicos serão definidos após a consolidação e avaliação da qualidade da série histórica.

## 4. Resultados e discussão

*A desenvolver após a validação e consolidação das bases.*

Os resultados preliminares do processamento e da qualidade dos dados estão registrados no arquivo `diario_pesquisa.md`.

## 5. Conclusão

*A elaborar após a análise e discussão dos resultados.*

## Referências

*A construir com base nas fontes oficiais e nos trabalhos científicos consultados.*

Fonte inicial dos dados:

MINISTÉRIO DA SAÚDE. Portal de Dados Abertos — Arboviroses: Dengue. Disponível em: https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue.

*Referência bibliográfica a normalizar conforme as orientações institucionais.*
