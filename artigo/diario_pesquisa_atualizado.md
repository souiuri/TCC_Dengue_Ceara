# Diário de Pesquisa — TCC Dengue Ceará

**Projeto:** Análise temporal e espacial dos registros de dengue no Ceará entre 2016 e 2025 utilizando Python

**Curso:** Ciência da Computação — Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE), Campus Maracanaú

**Orientador:** Prof. Fabio Jose Gomes de Sousa

**Situação:** Pesquisa em desenvolvimento

**Natureza do documento:** Registro interno de acompanhamento científico e metodológico

**Nota editorial (atualizada em 18/11/2026):** este diário preserva registros históricos de etapas preliminares. As seções posteriores atualizam resultados e decisões anteriores. A seção 11 é um retrato anterior da pesquisa; para o estado de revisão do artigo e as pendências atuais, consultar também as seções 23 a 26.

---

## 1. Objetivo da pesquisa

Investigar a distribuição temporal e espacial dos registros de dengue no estado do Ceará entre 2016 e 2025, utilizando dados públicos disponibilizados pelo Ministério da Saúde e ferramentas computacionais desenvolvidas em Python.

A pesquisa pretende analisar separadamente:

- O conjunto de registros de dengue disponíveis nas bases históricas.

- Os registros classificados como casos de dengue, após validação dos critérios de classificação.

- A evolução anual e mensal dos registros.

- A distribuição espacial da dengue entre os municípios cearenses.

- As tendências temporais e os padrões de sazonalidade da doença.

Ao final, pretende-se aplicar técnicas de análise de séries temporais para investigar tendências, variações interanuais e possíveis padrões sazonais.

Os resultados serão apresentados em formato de artigo científico, como Trabalho de Conclusão de Curso em Ciência da Computação.

## 2. Fonte dos dados

Os dados utilizados foram obtidos no Portal de Dados Abertos do Ministério da Saúde, no conjunto referente às arboviroses e à dengue.

**Fonte oficial:** https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue

Foram selecionados dez arquivos históricos:

- `DENGBR16.csv`

- `DENGBR17.csv`

- `DENGBR18.csv`

- `DENGBR19.csv`

- `DENGBR20.csv`

- `DENGBR21.csv`

- `DENGBR22.csv`

- `DENGBR23.csv`

- `DENGBR24.csv`

- `DENGBR25.csv`

Esses arquivos constituem a fonte primária da pesquisa.

As bases originais são preservadas localmente na pasta `dados/originais/` e não são incluídas no repositório GitHub.

**Observação:** o ano indicado no nome do arquivo não corresponde necessariamente ao ano de início dos sintomas ou ao ano de notificação de todos os registros presentes nele.

## 3. Ambiente de desenvolvimento

O processamento e a análise dos dados estão sendo desenvolvidos em ambiente Windows, utilizando Python.

### 3.1. Ferramentas e bibliotecas utilizadas

O desenvolvimento da pesquisa foi realizado utilizando a linguagem de programação Python, em ambiente Windows, com o Visual Studio Code como editor de código e ambiente de execução dos scripts.

Para o processamento, a validação e a análise dos dados epidemiológicos e populacionais, foram utilizadas as seguintes bibliotecas:

| Biblioteca | Finalidade |
|---|---|
| **pandas** | Leitura e processamento dos arquivos CSV, filtragem, limpeza, agregação de registros, construção das séries temporais e cálculo das taxas. |
| **Matplotlib** | Elaboração de gráficos temporais, comparações municipais, mapas e personalização de elementos visuais, incluindo escalas de cores e legendas. |
| **Seaborn** | Construção de mapas de calor para visualização de padrões temporais e diferenças entre municípios. |
| **GeoPandas** | Manipulação de dados geográficos, associação de informações municipais à malha territorial e elaboração de mapas temáticos. |

Também foram utilizados módulos pertencentes à biblioteca padrão do Python:

| Módulo | Finalidade |
|---|---|
| `pathlib` | Manipulação de caminhos de arquivos e diretórios. |
| `urllib.request` | Acesso a recursos disponíveis em endereços eletrônicos. |
| `gzip` | Manipulação de dados comprimidos. |
| `json` | Leitura e manipulação de dados no formato JSON. |
| `re` | Processamento de textos por expressões regulares. |
| `unicodedata` | Normalização de caracteres e textos. |
| `numbers` | Verificação de tipos numéricos. |

Foram utilizadas as ferramentas Git e GitHub para controle de versões, organização do código-fonte e acompanhamento das alterações realizadas durante o desenvolvimento.

A preparação do artigo científico foi conduzida utilizando LaTeX, conforme o modelo acadêmico adotado pelo IFCE.

O projeto foi organizado em scripts independentes para preparação das bases, validação de dados, análises temporais, análises municipais e produção de visualizações, visando favorecer a rastreabilidade e a reprodutibilidade dos procedimentos.

### 3.2. Estratégia de processamento

Devido ao tamanho dos arquivos originais, foi adotada a leitura em blocos com pandas, utilizando:

`chunksize=100_000`

Essa estratégia permite processar os arquivos sem carregar todas as linhas simultaneamente na memória.

O projeto utiliza scripts independentes para preparação, exploração e validação dos dados, favorecendo a organização e a reprodutibilidade das análises.

## 4. Organização do projeto

A estrutura foi conferida com a listagem `estrutura_projeto.txt`, gerada no diretório principal do projeto. A árvore abaixo apresenta os diretórios e arquivos representativos, omitindo cópias de segurança (`.bak`) e caches de execução (`__pycache__`) para facilitar a leitura.

```text
TCC_Dengue_Ceara/
├── artigo/
│   ├── diario_pesquisa.md
│   ├── diario_pesquisa_atualizado.md
│   ├── rascunho.md
│   ├── rascunho_reconstruido.md
│   ├── rascunho_tcc_atualizado.md
│   └── latex/
│       ├── main.tex
│       ├── 01-Pre-Textual/        (Resumo.tex, Abstract.tex)
│       ├── 02-Secoes/             (introdução, trabalhos relacionados,
│       │                          fundamentação, metodologia, resultados, conclusão)
│       ├── 03-pos-textual/        (referencias.bib)
│       ├── Figuras/
│       └── Lib/                   (IFCE_Latex.sty, Preambulo.tex)
├── dados/
│   ├── dengue_ceara_2024.csv
│   ├── geograficos/              (malhas CE_Municipios_2020.zip a 2025.zip)
│   ├── originais/
│   │   ├── DENGBR16.csv ... DENGBR25.csv
│   │   └── populacao/            (planilhas IBGE de 2016 a 2025)
│   └── processados/              (bases Ceará, base analítica e populações)
├── resultados/
│   ├── graficos/                 (séries, mapas, rankings e mapas de calor)
│   ├── modelos/
│   ├── tabelas/
│   └── *.csv                     (resultados temporais, municipais e regionais)
├── scripts/
│   ├── 01_preparacao/
│   ├── 02_analise_temporal/
│   ├── 03_analise_espacial/
│   ├── 04_analise_regional/
│   ├── 05_machine_learning/
│   └── 06_validacao/
├── primeiro_teste.py
├── .gitignore
├── README.md
└── estrutura_projeto.txt
```

### 4.1. Finalidade dos diretórios

- **`artigo/`:** registros metodológicos, versões do rascunho e elaboração do artigo científico.
- **`artigo/latex/`:** modelo do IFCE, com arquivo principal, seções, resumo, abstract, bibliografia, figuras e arquivos de configuração.
- **`dados/originais/`:** arquivos históricos nacionais de dengue e planilhas populacionais utilizadas como fontes.
- **`dados/geograficos/`:** arquivos compactados das malhas municipais do Ceará, identificados por ano de 2020 a 2025.
- **`dados/processados/`:** arquivos filtrados para o Ceará, base analítica consolidada e bases populacionais padronizadas.
- **`scripts/`:** programas Python organizados por finalidade analítica e de validação.
- **`resultados/`:** tabelas CSV, figuras e diretórios reservados para modelos e tabelas adicionais.

### 4.2. Organização dos scripts

| Diretório | Responsabilidade | Exemplos de scripts existentes |
|---|---|---|
| `01_preparacao/` | Filtragem, consolidação e preparação das bases epidemiológicas e populacionais | `preparar_base_historica.py`, `criar_base_analitica.py`, `preparar_populacao_historica.py`, `calcular_taxas_municipais_historicas.py` |
| `02_analise_temporal/` | Séries mensais, sazonalidade e gráficos comparativos | `serie_historica_mensal.py`, `analisar_sazonalidade.py`, `grafico_serie_mensal.py`, `heatmap_taxas_municipais.py` |
| `03_analise_espacial/` | Mapas, classes espaciais e comparações entre municípios | `mapas_historicos_dengue.py`, `mapa_taxas_dengue_2024.py`, `analisar_classes_espaciais.py` |
| `04_analise_regional/` | Taxas regionais, recorrência e sazonalidade por região | `calcular_taxas_regionais.py`, `analisar_recorrencia_regional.py`, `heatmap_sazonalidade_regional.py` |
| `05_machine_learning/` | Preparação de dados para exploração de agrupamentos | `preparar_matriz_kmeans.py` |
| `06_validacao/` | Verificações de qualidade, códigos, classificações, datas e consistência | `validar_base_analitica.py`, `verificar_criterios.py`, `verificar_intervalos.py`, `verificar_regioes_ceara.py` |

A existência de um script no diretório não comprova, isoladamente, que seus resultados tenham sido executados ou validados. O diretório de *machine learning*, por exemplo, contém um script de preparação de matriz, mas a listagem não comprova a execução de um modelo de agrupamento.

### 4.3. Principais produtos identificados

**Bases e resultados tabulares:** `dengue_ceara_analitica.csv`, `populacao_ceara_historica.csv`, `serie_historica_mensal.csv`, `taxas_dengue_municipios_2016_2025.csv`, `taxas_dengue_regionais_2016_2025.csv`, `dengue_mensal_regional_2016_2025.csv`, `picos_regionais_anuais_2016_2025.csv` e `recorrencia_regional_2016_2025.csv`.

**Visualizações:** `mapas_historicos_dengue_2016_2025.png`, `mapa_taxas_dengue_2024.png`, `mapa_taxas_dengue_2024_classes.png`, `heatmap_taxas_regionais_2016_2025.png`, `heatmap_sazonalidade_regional.png`, `serie_mensal_2016_2025.png` e `comparativo_brejo_ceara_2016_2025.png`.

**Documento científico:** o modelo LaTeX está distribuído entre `main.tex`, `01-Pre-Textual/`, `02-Secoes/`, `03-pos-textual/`, `Figuras/` e `Lib/`. A presença desses arquivos indica a estrutura disponível para a redação, não que o conteúdo do artigo esteja finalizado.

**Observação de reprodutibilidade:** a estrutura acima foi verificada pelos nomes dos arquivos e diretórios fornecidos na listagem. O conteúdo, a execução e a consistência dos produtos regionais e geográficos exigem conferência específica antes da incorporação definitiva ao artigo.

## 5. Preparação das bases históricas

Foi desenvolvido o script `scripts/preparar_base_historica.py`, responsável por percorrer os dez arquivos históricos, selecionar as variáveis necessárias e filtrar os registros referentes ao Ceará.

### 5.1. Critério de filtragem geográfica

O filtro utiliza a variável `SG_UF`, selecionando os registros com código:

`SG_UF = 23`

Esse código corresponde ao estado do Ceará. A seleção por `SG_UF` não garante, por si só, que `ID_MN_RESI` identifique um dos 184 municípios cearenses. Por isso, a análise espacial realiza uma validação independente dos códigos de município de residência.

Os arquivos resultantes são armazenados em `dados/processados/`, com nomes como:

- `DENGBR16_CE.csv`

- `DENGBR25_CE.csv`

### 5.2. Variáveis preservadas

Após a atualização do processamento, foram selecionadas oito variáveis:

| Variável | Finalidade na pesquisa |

|---|---|

| `ID_AGRAVO` | Identificação do agravo registrado |

| `DT_NOTIFIC` | Data da notificação |

| `NU_ANO` | Ano registrado na base |

| `DT_SIN_PRI` | Data de início dos primeiros sintomas |

| `SG_UF` | Unidade federativa |

| `ID_MN_RESI` | Município de residência |

| `CLASSI_FIN` | Classificação final do registro |

| `CRITERIO` | Critério de confirmação ou descarte |

A ordem das colunas não interfere nas análises, desde que seus nomes sejam preservados corretamente.

### 5.3. Resultados do processamento

| Arquivo original | Registros filtrados para o Ceará |

|---|---:|

| DENGBR16.csv | 100.523 |

| DENGBR17.csv | 81.382 |

| DENGBR18.csv | 15.202 |

| DENGBR19.csv | 33.396 |

| DENGBR20.csv | 40.976 |

| DENGBR21.csv | 69.284 |

| DENGBR22.csv | 42.787 |

| DENGBR23.csv | 14.463 |

| DENGBR24.csv | 12.552 |

| DENGBR25.csv | 5.530 |

| **Total** | **416.095** |

**Observação metodológica:** os 416.095 registros representam a soma das linhas filtradas nos dez arquivos de origem.

Esse valor não deve ser interpretado automaticamente como quantidade de casos únicos, casos confirmados ou casos ocorridos exclusivamente entre 2016 e 2025.

Ainda serão investigadas possíveis duplicidades, inconsistências temporais e diferenças entre os arquivos.

### 5.4. Atualização e validação do processamento

O script `preparar_base_historica.py` foi atualizado para incluir as variáveis `CRITERIO` e `ID_AGRAVO`.

Inicialmente, ocorreu um erro de execução relacionado à utilização de uma variável não definida (`COLUNAS`). O problema foi corrigido mediante padronização do nome da variável utilizada na seleção das colunas.

Em seguida:

1. Foi verificada a presença das oito variáveis nos dez arquivos originais.

2. Todos os arquivos originais passaram na verificação.

3. O processamento histórico foi executado novamente.

4. Os dez arquivos processados foram gerados sem erros.

5. As quantidades de registros permaneceram iguais às do processamento anterior.

6. Foi confirmada a presença das oito colunas no arquivo processado de 2025.

**Situação da etapa:** processamento concluído e atualização registrada no Git.

**Validação ainda recomendada:** verificar automaticamente as oito colunas em todos os arquivos processados, além da conferência já realizada no arquivo de 2025.

## 6. Definição da referência temporal

Foram identificadas duas variáveis temporais de interesse.

### 6.1. Data de notificação

`DT_NOTIFIC`

Representa a data de notificação do registro ao sistema de vigilância.

Essa variável poderá ser utilizada para analisar o comportamento das notificações e comparar os resultados com aqueles obtidos pela data de início dos sintomas.

### 6.2. Data de início dos sintomas

`DT_SIN_PRI`

Representa a data informada para o início dos primeiros sintomas.

Foi escolhida provisoriamente como principal referência para a construção das séries temporais da pesquisa.

### 6.3. Justificativa metodológica

A data de início dos sintomas pode representar de maneira mais próxima o momento de manifestação da doença, enquanto a notificação pode ocorrer posteriormente.

Entretanto, essa escolha depende da avaliação da completude e da consistência das datas.

Foi identificado que alguns arquivos possuem registros referentes a anos diferentes daqueles indicados em seus nomes.

Por esse motivo, a pesquisa não utilizará automaticamente o nome do arquivo como referência para determinar o ano epidemiológico de cada registro.

**Decisão provisória:** utilizar `DT_SIN_PRI` na análise temporal principal e manter `DT_NOTIFIC` como referência complementar, após aplicação de critérios documentados de qualidade.

## 7. Avaliação da qualidade das datas

Foi desenvolvido o script `scripts/verificar_intervalos.py` para calcular a diferença, em dias, entre a data de notificação e a data de início dos sintomas.

O intervalo é calculado pela expressão:

**Intervalo = Data de notificação − Data de início dos sintomas**

### 7.1. Categorias utilizadas

Os registros foram distribuídos nas seguintes categorias:

- Notificação anterior ao início dos sintomas.

- Intervalo entre 0 e 30 dias.

- Intervalo entre 31 e 365 dias.

- Intervalo superior a 365 dias.

- Datas ausentes ou inválidas.

### 7.2. Resultados

| Indicador | Registros |

|---|---:|

| Intervalo de 0 a 30 dias | 407.102 |

| Intervalo de 31 a 365 dias | 8.048 |

| Intervalo superior a 365 dias | 938 |

| Notificação anterior aos sintomas | 2 |

| Datas ausentes ou inválidas | 5 |

| **Total** | **416.095** |

Aproximadamente **97,84%** dos registros apresentaram intervalo entre zero e trinta dias.

A maioria dos registros, portanto, apresentou uma diferença relativamente curta entre início dos sintomas e notificação.

Essa observação descreve apenas a distribuição dos intervalos calculados e não comprova, isoladamente, a validade epidemiológica dos registros.

### 7.3. Inconsistências identificadas

Foram encontrados dois registros no arquivo de 2022 em que a data de notificação era anterior à data de início dos sintomas.

| Data de notificação | Data de início dos sintomas |

|---|---|

| 19/04/2022 | 22/04/2022 |

| 02/02/2022 | 01/08/2022 |

Também foram identificados registros com intervalos superiores a 365 dias, incluindo datas de sintomas muito anteriores ao período esperado.

Algumas datas registradas nos arquivos históricos remontam a décadas anteriores às respectivas notificações.

### 7.4. Decisão metodológica provisória

As bases originais serão preservadas integralmente.

Os registros temporalmente inconsistentes serão identificados, contabilizados e documentados antes de qualquer exclusão da base analítica.

Os dois registros com intervalo negativo deverão ser tratados como inconsistências na análise temporal principal.

Os registros com intervalos superiores a 365 dias permanecerão sob investigação, sem exclusão automática.

As regras definitivas de limpeza deverão ser justificadas no artigo científico.

### 7.5. Relatório produzido

O script gera o arquivo:

`resultados/qualidade_datas_2016_2025.csv`

Esse relatório reúne as quantidades de registros por categoria de intervalo para cada arquivo histórico.

## 8. Investigação da classificação dos registros

Foi iniciada a investigação da variável `CLASSI_FIN`, utilizada para representar a classificação final dos registros.

Essa etapa é necessária para distinguir notificações, registros descartados e registros classificados como dengue.

### 8.1. Documentação oficial consultada

Foram examinados os seguintes documentos do Ministério da Saúde:

- **Dicionário de Dados do SINAN Online**, versão 3.0, revisado em 2015.

- **Nota Informativa nº 59/2016 — CGPNCD/DEVIT/SVS/MS**.

Esses documentos foram utilizados para interpretar os códigos de classificação e os critérios associados aos registros.

### 8.2. Códigos documentados de `CLASSI_FIN`

| Código | Classificação |

|---|---|

| 5 | Descartado |

| 10 | Dengue |

| 11 | Dengue com sinais de alarme |

| 12 | Dengue grave |

| 13 | Chikungunya |

Também foram encontrados os códigos `8`, `0`, `1` e `4` nas bases históricas.

Esses códigos não foram esclarecidos pelos documentos consultados até o momento e deverão ser investigados antes da definição final dos critérios de seleção.

### 8.3. Resultados preliminares da classificação

A análise inicial identificou a seguinte quantidade de registros com `CLASSI_FIN` igual a 10, 11 ou 12:

| Arquivo | Registros classificados como dengue |

|---|---:|

| DENGBR16 | 42.007 |

| DENGBR17 | 27.262 |

| DENGBR18 | 4.019 |

| DENGBR19 | 15.698 |

| DENGBR20 | 21.543 |

| DENGBR21 | 33.845 |

| DENGBR22 | 39.940 |

| DENGBR23 | 14.210 |

| DENGBR24 | 12.133 |

| DENGBR25 | 5.091 |

| **Total** | **215.748** |

**Observação de conferência:** O total de 215.748 registros foi confirmado por cálculo automatizado em Python, considerando os códigos 10, 11 e 12 da variável CLASSI_FIN.

Essas quantidades ainda são preliminares e não representam necessariamente casos únicos ou a contagem definitiva de casos confirmados.

### 8.4. Diferenças observadas entre os arquivos

A distribuição dos códigos de classificação apresenta diferenças importantes entre os períodos analisados.

O código `5`, correspondente a registros descartados, aparece em quantidades expressivas entre 2016 e 2021, mas não foi identificado nos arquivos de 2022 a 2025.

Essa diferença precisa ser investigada antes de interpretar alterações nas quantidades de registros classificados como dengue como tendências epidemiológicas.

Não é possível concluir, apenas com esses resultados, se a mudança decorre de alterações no sistema, no processamento, na disponibilização dos dados ou de outros fatores.

## 9. Investigação da variável `CRITERIO`

A variável `CRITERIO` foi incorporada ao processamento para permitir a análise do critério utilizado na classificação dos registros.

### 9.1. Códigos documentados

| Código | Critério |

|---|---|

| 1 | Laboratorial |

| 2 | Clínico-epidemiológico |

| 3 | Em investigação |

### 9.2. Investigação preliminar do arquivo de 2025

Foi realizada uma análise cruzada entre `CLASSI_FIN` e `CRITERIO` nos registros do Ceará presentes no arquivo original de 2025.

Entre os 5.091 registros com classificação 10, 11 ou 12, foram observados:

| Critério | Registros |

|---|---:|

| Laboratorial (1) | 4.007 |

| Clínico-epidemiológico (2) | 907 |

| Em investigação (3) | 177 |

| **Total** | **5.091** |

A presença de 177 registros classificados como dengue, mas com critério marcado como em investigação, exige uma verificação adicional da consistência e da interpretação desses campos.

### 9.3. Registros com classificação 8

No arquivo de 2025, foram identificados 411 registros com `CLASSI_FIN = 8`.

Desses, 367 apresentavam `CRITERIO` ausente.

O significado desse código e sua relação com os critérios de classificação ainda não foram estabelecidos.

### 9.4. Verificação do agravo

Na análise preliminar do arquivo original de 2025 filtrado para o Ceará, todos os 5.530 registros apresentaram:

`ID_AGRAVO = A90`

Essa observação corresponde apenas ao conjunto examinado e não deve ser generalizada automaticamente aos demais anos.

### 9.5. Decisão metodológica provisória

Os códigos 10, 11 e 12 serão utilizados inicialmente para identificar registros classificados como dengue.

Entretanto, a definição final de casos confirmados dependerá de:

- Investigação dos critérios de classificação.

- Verificação dos registros em investigação.

- Esclarecimento dos códigos não documentados.

- Avaliação de possíveis duplicidades.

- Aplicação das regras de consistência temporal.

Não serão apresentados resultados definitivos de casos confirmados antes da conclusão dessas verificações.

## 10. Análises exploratórias realizadas

Foi realizada uma análise inicial dos registros referentes ao arquivo de 2024.

### 10.1. Distribuição temporal

Foram produzidas contagens mensais utilizando a data de notificação.

O maior número de registros na exploração inicial ocorreu em abril.

Esses resultados ainda não constituem uma série temporal definitiva, pois foram obtidos antes da consolidação dos critérios de classificação e qualidade.

### 10.2. Distribuição espacial

Também foram realizadas contagens de registros por município.

Foram identificados municípios com quantidades elevadas de registros, incluindo Fortaleza e Brejo Santo.

Essas contagens representam números absolutos e não taxas de incidência.

### 10.3. Produtos gerados

Entre os resultados exploratórios produzidos estão:

- `resultados/graficos/notificacoes_dengue_2024.png`

- `resultados/graficos/top10_municipios_dengue_2024.png`

- `resultados/municipios_dengue_2024.csv`

Todos os resultados exploratórios deverão ser reavaliados após a consolidação da base analítica.

## 11. Situação das etapas e pendências metodológicas

Esta seção apresenta o estado atual da pesquisa, considerando as etapas de preparação dos dados, validação metodológica, análises temporais, espaciais e regionais, além da elaboração do artigo científico.

Os registros históricos das etapas anteriores permanecem documentados nas seções seguintes deste diário.

### 11.1. Etapas realizadas

**Preparação e validação dos dados**

- Obtenção dos dez arquivos históricos de dengue do Ministério da Saúde, referentes a 2016–2025.
- Filtragem inicial dos registros do Ceará utilizando `SG_UF = 23`, totalizando 416.095 registros.
- Seleção dos registros classificados como dengue por meio dos códigos 10, 11 e 12 de `CLASSI_FIN`.
- Construção da base analítica e aplicação dos critérios operacionais de qualidade temporal.
- Investigação exploratória de possíveis duplicidades, sem exclusão automática de registros.
- Validação dos códigos municipais de residência com referência aos 184 municípios cearenses.
- Consolidação das populações municipais do IBGE para 2016–2025.
- Cálculo das taxas anuais de registros classificados de dengue por 100 mil habitantes.

**Análise temporal**

- Construção da série histórica mensal de janeiro de 2016 a dezembro de 2025, com 120 observações.
- Análise da distribuição anual e mensal dos registros.
- Identificação de padrões descritivos de sazonalidade.
- Produção de gráficos temporais e mapas de calor.

**Análise espacial municipal**

- Consolidação dos registros dos 184 municípios cearenses.
- Comparação entre números absolutos e taxas populacionais.
- Análise histórica de Brejo Santo em relação ao Ceará.
- Produção de rankings municipais e mapas de calor.
- Desenvolvimento de scripts e geração de mapas geográficos municipais, incluindo mapas históricos e representações das taxas de 2024.

**Análise regional**

- Desenvolvimento de scripts para agregação e análise regional dos registros de dengue.
- Geração de tabelas de taxas regionais, distribuição mensal, picos anuais e recorrência.
- Produção de mapas de calor de taxas e sazonalidade regionais.

**Organização e documentação**

- Reorganização dos scripts em seis grupos funcionais.
- Atualização do diário de pesquisa e dos rascunhos do artigo.
- Preparação da estrutura LaTeX com o modelo acadêmico do IFCE.

A existência dos arquivos de análise geográfica e regional foi confirmada na estrutura do projeto. A validação integral de seus resultados depende da conferência dos respectivos scripts e tabelas.

### 11.2. Pendências metodológicas e científicas

- Esclarecer os códigos de `CLASSI_FIN` que permanecem sem interpretação consolidada.
- Investigar a consistência dos registros com `CRITERIO = 3` e definir a terminologia operacional adotada no artigo.
- Conferir a composição dos 435 registros que não integraram a janela temporal de 2016–2025.
- Avaliar a sensibilidade dos resultados à exclusão operacional dos 62 registros com intervalo superior a 365 dias.
- Verificar a completude e a comparabilidade das bases históricas, especialmente de 2025.
- Documentar as limitações da utilização das populações de 2022 e 2023.
- Conferir os critérios de classificação cartográfica, os resultados regionais e a correspondência entre tabelas e figuras.
- Distinguir os padrões espaciais observados visualmente de agrupamentos estatisticamente demonstrados.
- Revisar a fundamentação teórica, as referências bibliográficas e a redação científica do artigo.

### 11.3. Situação do artigo científico

O artigo está em fase de consolidação, com rascunhos contendo introdução, fundamentação teórica, metodologia, resultados, discussão e conclusão.

A estrutura LaTeX do IFCE está organizada na pasta `artigo/latex/`, com arquivos separados para resumo, abstract, seções principais e referências.

As próximas atividades devem priorizar a integração do conteúdo revisado ao modelo LaTeX, a seleção das figuras mais relevantes e a conferência das citações e referências.

**Prioridade:** produzir uma versão completa e revisável do artigo para avaliação do orientador, evitando a inclusão de novas análises que não possam ser verificadas dentro do prazo.

## 12. Próximas etapas da pesquisa

Considerando o desenvolvimento das análises temporais, espaciais e regionais, as próximas etapas serão concentradas na validação dos resultados e na finalização do artigo científico.

### 12.1. Conferência dos resultados

1. Verificar a consistência dos resultados apresentados nas tabelas, gráficos e mapas.
2. Conferir os resultados das análises regionais com os arquivos CSV produzidos pelos scripts.
3. Revisar os critérios metodológicos utilizados na construção dos mapas geográficos e na classificação das taxas.
4. Confirmar que os quantitativos apresentados no artigo correspondem aos conjuntos de dados utilizados em cada análise.

### 12.2. Consolidação do artigo científico

1. Unificar os rascunhos existentes em uma versão consolidada.
2. Atualizar a metodologia para incluir as análises geográficas e regionais efetivamente realizadas.
3. Selecionar as tabelas e figuras mais relevantes para apresentação dos resultados.
4. Revisar a discussão científica, destacando os principais padrões identificados e as limitações da pesquisa.
5. Completar e padronizar as referências bibliográficas.

### 12.3. Preparação e revisão em LaTeX

1. Transferir o conteúdo consolidado para o modelo LaTeX do IFCE.
2. Elaborar e revisar o resumo em português e o abstract em inglês.
3. Inserir figuras, tabelas, citações e referências.
4. Compilar o documento e corrigir eventuais erros de formatação.
5. Conferir as exigências acadêmicas do curso e encaminhar o artigo ao orientador para revisão.

### 12.4. Prioridade imediata

A prioridade é concluir uma versão integral, coerente e verificável do artigo científico, utilizando os resultados já produzidos.

Novas análises computacionais somente serão realizadas se forem indispensáveis para corrigir inconsistências ou fundamentar resultados apresentados no artigo.

As verificações metodológicas que não puderem ser concluídas deverão ser documentadas como limitações, sem apresentar resultados não validados como conclusivos.

### 13.2. Escolha da referência temporal

**Problema:** determinar a variável adequada para representar a ocorrência temporal dos registros.

**Procedimento:** análise das variáveis `DT_NOTIFIC` e `DT_SIN_PRI`.

**Resultado:** identificação de diferenças entre datas de sintomas, notificação e anos indicados nos nomes dos arquivos.

**Decisão:** adotar provisoriamente `DT_SIN_PRI` como referência temporal principal.

**Justificativa:** representar o início informado dos sintomas, mantendo a notificação como informação complementar.

### 13.3. Avaliação dos intervalos entre sintomas e notificação

**Problema:** identificar registros com datas potencialmente inconsistentes.

**Procedimento:** cálculo dos intervalos em dias e classificação em categorias.

**Resultado:** identificação de dois intervalos negativos, 938 superiores a 365 dias e cinco registros com datas ausentes ou inválidas.

**Decisão:** preservar os dados originais e investigar as inconsistências antes de aplicar exclusões.

**Justificativa:** evitar perda de informações sem critérios documentados.

### 13.4. Validação da classificação da dengue

**Problema:** distinguir registros classificados como dengue de outros registros presentes nas bases.

**Procedimento:** consulta ao dicionário de dados do SINAN Online e à Nota Informativa nº 59/2016, seguida de exploração da variável `CLASSI_FIN`.

**Resultado:** identificação dos códigos 5, 10, 11, 12 e 13 na documentação e de outros códigos nas bases históricas.

**Decisão:** utilizar provisoriamente os códigos 10, 11 e 12 para identificar registros classificados como dengue, sem considerá-los ainda uma contagem definitiva de casos confirmados.

**Justificativa:** ainda existem questões relativas à consistência, duplicidade e classificação dos registros.

**Pendências:** investigar os códigos 8, 0, 1 e 4, além das diferenças observadas entre os períodos históricos.

### 13.5. Inclusão das variáveis `CRITERIO` e `ID_AGRAVO`

**Problema:** a versão anterior dos arquivos processados não preservava todas as variáveis necessárias para aprofundar a investigação das classificações.

**Procedimento:** atualização do script de preparação, verificação das colunas nos arquivos originais e novo processamento histórico.

**Resultado:** dez arquivos processados novamente, mantendo os 416.095 registros. O arquivo processado de 2025 foi conferido e apresentou as oito variáveis previstas.

**Decisão:** manter `CRITERIO` e `ID_AGRAVO` no conjunto de variáveis selecionadas.

**Justificativa:** permitir análises mais detalhadas da classificação dos registros e da identificação do agravo.

### 13.6. Investigação preliminar dos critérios de 2025

**Problema:** verificar se a classificação final e o critério informado são consistentes.

**Procedimento:** cruzamento entre `CLASSI_FIN` e `CRITERIO` no arquivo original de 2025 filtrado para o Ceará.

**Resultado:** identificação de 177 registros com classificação de dengue e critério em investigação.

**Decisão:** aprofundar a análise antes de estabelecer os critérios definitivos de confirmação.

**Justificativa:** a presença desses registros exige cautela na interpretação dos totais.

### 13.7. Análise histórica dos critérios de classificação — 2016 a 2025

**Problema investigado:**

Verificar a distribuição da variável `CRITERIO` entre os registros classificados como dengue nos dez arquivos históricos do Ceará, identificando possíveis inconsistências entre a classificação final e o critério informado.

**Procedimento realizado:**

Foi desenvolvido o script `scripts/verificar_criterios.py`, utilizando Python e a biblioteca pandas.

Inicialmente, foram contabilizados os valores de `CRITERIO` em todos os registros filtrados para o Ceará.

Posteriormente, a análise foi restringida aos registros com `CLASSI_FIN` igual a 10, 11 ou 12, correspondentes às classificações de dengue, dengue com sinais de alarme e dengue grave.

Foram contabilizados os critérios:

- `1`: laboratorial.

- `2`: clínico-epidemiológico.

- `3`: em investigação.

Os resultados foram consolidados automaticamente e exportados para `resultados/criterios_dengue_2016_2025.csv`.

**Resultados obtidos:**

| Critério | Registros | Percentual |

|---|---:|---:|

| Laboratorial (1) | 73.588 | 34,1% |

| Clínico-epidemiológico (2) | 136.399 | 63,2% |

| Em investigação (3) | 5.761 | 2,7% |

| **Total** | **215.748** | **100%** |

A soma dos registros foi verificada automaticamente pelo Python.

O critério clínico-epidemiológico apresentou a maior frequência entre os registros classificados como dengue.

Foram identificados 5.761 registros que apresentam classificação final de dengue, mas possuem `CRITERIO = 3`, correspondente a registros em investigação no dicionário consultado.

A análise inicial de todos os registros, antes do filtro por classificação final, também identificou quatro ocorrências de `CRITERIO = 0`, sendo três no arquivo de 2023 e uma no arquivo de 2025.

**Decisão metodológica:**

Manter provisoriamente todos os registros classificados com os códigos 10, 11 e 12, sem excluir automaticamente aqueles com `CRITERIO = 3`.

A definição final dos casos confirmados dependerá de investigação adicional da consistência entre `CLASSI_FIN` e `CRITERIO`, além da avaliação de duplicidades e da qualidade das datas.

**Limitações:**

As quantidades apresentadas representam registros nos arquivos históricos, e não necessariamente casos únicos ou ocorrências pertencentes ao ano indicado no nome de cada arquivo.

Os resultados ainda não constituem uma série epidemiológica anual definitiva.

**Pendências:**

- Investigar os 5.761 registros com `CRITERIO = 3`.

- Verificar possíveis duplicidades entre os arquivos históricos.

- Definir as regras finais de inclusão e exclusão dos registros.

- Consolidar as séries temporais por data de início dos sintomas.

### 13.8. Investigação exploratória de possíveis duplicidades — 2024

Foi realizada uma análise exploratória de registros com combinações idênticas de variáveis no arquivo DENGBR24.csv, disponibilizado pelo Ministério da Saúde. Após a seleção dos registros do Ceará (`SG_UF = 23`), foram analisadas 12.552 notificações.

Inicialmente, a comparação utilizou oito variáveis: agravo, data de notificação, ano da notificação, data dos primeiros sintomas, unidade federativa de residência, município de residência, classificação final e critério de confirmação. Nessa etapa, 5.248 registros apresentaram combinações repetidas.

Posteriormente, foram acrescentadas quatro variáveis: idade codificada, sexo, unidade notificadora e município da notificação. Com 12 variáveis, o número de registros envolvidos em combinações repetidas diminuiu para 208.

Na terceira comparação, foram incluídas cinco variáveis clínicas: febre, mialgia, cefaleia, exantema e hospitalização. Com 17 variáveis, foram identificados 95 registros envolvidos em 47 grupos de combinações repetidas, sendo 46 grupos com duas ocorrências e um grupo com três ocorrências.

Todos os 95 registros estavam classificados como dengue (`CLASSI_FIN = 10`).

Os resultados demonstram que a quantidade de coincidências depende das variáveis selecionadas. Entretanto, a igualdade entre os campos analisados não comprova que os registros correspondam à mesma pessoa ou ao mesmo episódio de doença.

**Decisão metodológica:** preservar todos os registros nesta etapa, sem exclusão automática por coincidência de atributos. A investigação será posteriormente ampliada para os demais anos da série histórica, respeitando as diferenças de estrutura entre os arquivos.

**Limitação:** a ausência de um identificador individual nas variáveis examinadas impede confirmar duplicidades apenas por comparação exata dos campos disponíveis.

### 13.9. Investigação histórica de possíveis duplicidades (2016–2025)

Foi realizada uma investigação exploratória de possíveis duplicidades nos arquivos de notificações de dengue do SINAN referentes ao Ceará, abrangendo o período de 2016 a 2025.

Foram analisados 416.095 registros, distribuídos entre dez arquivos históricos.

Inicialmente, compararam-se oito variáveis comuns aos arquivos, sendo identificados 234.482 registros envolvidos em combinações repetidas dentro dos respectivos arquivos.

Posteriormente, foram acrescentadas quatro variáveis: idade codificada, sexo, unidade notificadora e município da notificação. Com 12 variáveis, a quantidade de registros envolvidos em combinações repetidas diminuiu para 7.570, correspondendo a aproximadamente 1,82% do total analisado.

Também foi realizada uma comparação entre arquivos históricos diferentes, utilizando as 12 variáveis. Não foram identificadas combinações integralmente idênticas presentes em mais de um arquivo.

Esses resultados indicam que a quantidade de coincidências depende significativamente das variáveis utilizadas na comparação. Entretanto, a igualdade entre atributos não comprova que duas notificações correspondam à mesma pessoa ou ao mesmo episódio da doença.

**Decisão metodológica:** não realizar exclusão automática de registros nesta etapa, preservando a integridade dos dados originais.

**Limitação:** a ausência de um identificador individual entre os campos examinados impede confirmar duplicidades apenas com os procedimentos realizados. A investigação não descarta registros duplicados com diferenças de preenchimento.

## 14. Modelo para os próximos registros

Utilizar a estrutura abaixo sempre que uma etapa metodológica relevante for concluída.

**Data:**

**Etapa:**

**Problema ou questão investigada:**

**Procedimento realizado:**

**Script ou ferramenta utilizada:**

**Resultado obtido:**

**Decisão e justificativa:**

**Limitações identificadas:**

**Pendências:**

## 15. Referências documentais e técnicas (levantamento inicial)

**BRASIL. Ministério da Saúde.** Portal de Dados Abertos. Conjunto de dados de arboviroses — dengue. Disponível em: https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue.

**BRASIL. Ministério da Saúde.** Dicionário de Dados do SINAN Online, versão 3.0, revisado em 2015. Documento técnico consultado durante a pesquisa.

**BRASIL. Ministério da Saúde.** Nota Informativa nº 59/2016 — CGPNCD/DEVIT/SVS/MS. Documento técnico consultado durante a pesquisa.

**Documentação do pandas:** https://pandas.pydata.org/docs/

**Documentação do Matplotlib:** https://matplotlib.org/stable/

As referências bibliográficas serão posteriormente revisadas e padronizadas conforme as exigências do artigo científico e do IFCE.

## 16. Análise temporal da dengue no Ceará (2016–2025)

### 16.1. Preparação e validação da base analítica

A base histórica consolidada contém 416.095 registros referentes ao Ceará, provenientes dos arquivos públicos de dengue do Ministério da Saúde, entre 2016 e 2025.

Foram identificados 215.748 registros classificados como dengue, considerando os códigos 10 (dengue), 11 (dengue com sinais de alarme) e 12 (dengue grave) da variável `CLASSI_FIN`.

A análise temporal utilizou a variável `DT_SIN_PRI`, correspondente à data de início dos primeiros sintomas.

Na delimitação temporal da base, 435 dos 215.748 registros classificados não integraram o conjunto de 2016 a 2025, conforme o filtro aplicado à data de início dos sintomas (`DT_SIN_PRI`). É necessário conferir no arquivo processado se esses 435 registros correspondem exclusivamente a datas válidas fora do período ou se também incluem datas ausentes ou inválidas. Eles não foram apagados dos arquivos históricos.

A base analítica resultante contém **215.313 registros** (215.748 − 435). A decomposição dos 435 registros permanece como verificação de qualidade pendente.

### 16.2. Critérios de qualidade temporal

Foi calculado o intervalo, em dias, entre o início dos sintomas (`DT_SIN_PRI`) e a data de notificação (`DT_NOTIFIC`).

Entre os 215.313 registros da base analítica, foram identificados:

- 211.881 registros com intervalo entre 0 e 30 dias;

- 3.370 registros com intervalo entre 31 e 365 dias;

- 62 registros com intervalo superior a 365 dias;

- Nenhum intervalo negativo ou ausente.

Os 62 registros com intervalo superior a 365 dias foram classificados como atrasos extremos e identificados pela variável `ATRASO_EXTREMO`.

Por decisão metodológica, esses registros permaneceram preservados na base analítica, mas foram desconsiderados nos scripts de análise temporal.

Assim, a série histórica temporal foi construída com **215.251 registros** (215.313 − 62). A série municipal, por exigir município de residência válido no Ceará, utiliza 215.243 registros; os dois totais não devem ser confundidos.

Essa decisão não representa comprovação de erro nos registros. Trata-se de um critério operacional de qualidade temporal, sujeito a avaliação de sensibilidade posterior.

### 16.3. Construção da série histórica

Foi criada uma série histórica mensal com 120 observações, correspondentes aos meses de janeiro de 2016 a dezembro de 2025.

A distribuição anual dos registros utilizados foi:

| Ano | Registros |

|---|---:|

| 2016 | 41.894 |

| 2017 | 27.055 |

| 2018 | 3.995 |

| 2019 | 15.674 |

| 2020 | 21.451 |

| 2021 | 33.845 |

| 2022 | 39.940 |

| 2023 | 14.220 |

| 2024 | 12.128 |

| 2025 | 5.049 |

| **Total** | **215.251** |

### 16.4. Análise de sazonalidade

A análise da distribuição mensal indicou concentração dos registros entre março e junho, período responsável por aproximadamente 65,5% dos registros utilizados.

Maio apresentou a maior média mensal da série, com 4.401,8 registros, seguido por abril, com 3.933,0, e junho, com 3.362,9.

O menor valor médio ocorreu em dezembro, com 325,2 registros.

A investigação dos picos anuais identificou que:

- Maio foi o mês de maior registro em cinco anos;

- Abril foi o mês de maior registro em quatro anos;

- Junho foi o mês de maior registro em um ano.

Portanto, em todos os dez anos analisados, os maiores valores mensais ocorreram entre abril e junho.

O maior pico mensal da série foi registrado em maio de 2022, com 10.601 registros.

### 16.5. Visualizações produzidas

Foram produzidos:

1. Série histórica mensal de registros classificados como dengue, de 2016 a 2025.

2. Gráfico de linha da evolução mensal.

3. Mapa de calor da distribuição mensal por ano.

Arquivos principais:

- `resultados/serie_historica_mensal.csv`

- `resultados/graficos/serie_mensal_2016_2025.png`

- `resultados/graficos/mapa_calor_2016_2025.png`

### 16.6. Limitações e próximos procedimentos

Os resultados representam registros classificados como dengue presentes nos arquivos analisados, não necessariamente casos únicos ou incidência populacional.

Ainda será necessário avaliar a completude dos dados, especialmente de 2025, investigar possíveis efeitos de diferenças na cobertura dos arquivos e realizar uma análise de sensibilidade considerando os 62 registros sinalizados.

**Registro histórico da etapa:** a análise por município de residência foi posteriormente iniciada e documentada nas seções 17 a 22.

## 17. Análise espacial da dengue no Ceará (2016–2025)

### 17.1. Validação dos códigos municipais

Foi realizada a validação da variável `ID_MN_RESI`, referente ao município de residência, utilizando a API de localidades do IBGE.

Dos 215.251 registros analisados, 215.243 apresentaram códigos municipais válidos do Ceará, seis não possuíam código municipal e dois apresentaram códigos de outros estados.

Foram identificados e validados os 184 municípios cearenses, sem códigos inválidos ou municípios ausentes.

### 17.2. Consolidação dos registros por município

Foi desenvolvido o script `scripts/consolidar_dados_municipios.py`, responsável por associar os códigos municipais aos nomes oficiais do IBGE e calcular os totais acumulados de registros.

O processamento gerou o arquivo `resultados/municipios_dengue_2016_2025.csv`, contendo os 184 municípios, seus códigos e a quantidade e participação percentual dos registros.

Os oito registros sem município cearense válido foram preservados na base analítica, mas não incluídos na agregação municipal. Essa exclusão aplica-se apenas à análise por município de residência e ao cálculo das taxas derivadas dessa agregação.

### 17.3. Resultados preliminares

Fortaleza apresentou a maior quantidade de registros (90.035; 41,83%), seguida por Brejo Santo (7.249; 3,37%) e Caucaia (6.155; 2,86%).

Foi produzido o gráfico `resultados/graficos/top10_municipios_2016_2025.png`, apresentando os dez municípios com maiores totais acumulados.

### 17.4. Limitações e próximos procedimentos

Os totais absolutos não permitem comparar diretamente o risco de dengue entre municípios com populações diferentes.

**Registro histórico da etapa:** a obtenção dos dados populacionais e o cálculo das taxas, então previstos como próximos passos, foram posteriormente concluídos e estão documentados nas seções 18 e 19.

## 18. Consolidação da base populacional histórica — 2016 a 2025

**Etapa:** concluída e validada.

### 18.1. Objetivo

Construir uma base populacional municipal histórica para permitir o cálculo de taxas de registros classificados de dengue por 100 mil habitantes, considerando os diferentes tamanhos populacionais dos municípios cearenses.

### 18.2. Fontes e processamento

Foram utilizados dados oficiais do IBGE:

- 2016 a 2021: estimativas populacionais municipais.

- 2022: Censo Demográfico 2022, tabela 4714 do SIDRA.

- 2023: valores populacionais derivados do Censo de 2022, publicados com referência à malha municipal de 2023; **não se trata de uma estimativa populacional independente para o ano de 2023**.

- 2024 e 2025: estimativas populacionais municipais.

O script `scripts/preparar_populacao_historica.py` foi utilizado para leitura, padronização, validação e consolidação dos arquivos.

A base final foi salva em `dados/processados/populacao_ceara_historica.csv`.

### 18.3. Resultados da validação

- Período: 2016–2025.

- Anos processados: 10.

- Municípios por ano: 184.

- Total de registros: 1.840.

- Códigos IBGE municipais únicos por ano: 184.

- Valores populacionais ausentes: nenhum nas verificações realizadas.

- Totais populacionais estaduais: validados.

### 18.4. Investigação das diferenças entre 2022 e 2023

Foi realizada uma comparação das populações municipais dos dois arquivos.

Ambos apresentam população estadual de 8.794.957 habitantes, mas dois municípios possuem diferenças:

| Município | 2022 | 2023 | Diferença |

|---|---:|---:|---:|

| Ereré | 6.474 | 6.247 | -227 |

| Pereiro | 15.274 | 15.501 | +227 |

Os outros 182 municípios apresentam valores idênticos.

A hipótese de ajuste ou redistribuição territorial permanece **não confirmada**; a documentação consultada até esta etapa não foi suficiente para estabelecer a causa das diferenças.

**Decisão metodológica:** preservar os valores publicados nas respectivas fontes, sem correções manuais, e documentar a diferença na interpretação dos indicadores.

### 18.5. Dificuldades encontradas

- Necessidade de instalar a biblioteca `openpyxl` para leitura da tabela 4714 em formato XLSX.

- Diferenças na estrutura dos arquivos populacionais entre os anos.

- Necessidade de tratamento específico para os dados censitários de 2022 e a publicação de 2023.

- Avisos de descontinuação futura do mecanismo `xlrd` na versão utilizada do pandas, sem comprometimento da execução atual.

### 18.6. Próxima etapa

**Registro histórico da etapa:** o cruzamento entre `populacao_ceara_historica.csv` e `municipios_dengue_por_ano.csv`, com validação dos 1.840 pares município-ano, foi posteriormente concluído, conforme descrito na seção 19.

---

## 19. Cálculo e validação das taxas municipais de dengue — 2016 a 2025

**Situação:** etapa concluída e validada.

### 19.1. Objetivo

Calcular as taxas anuais de registros classificados de dengue por 100 mil habitantes nos 184 municípios do Ceará, utilizando a base analítica do Ministério da Saúde e os dados populacionais do IBGE.

### 19.2. Procedimento

Foi desenvolvido o script `scripts/calcular_taxas_municipais_historicas.py`, responsável por relacionar os arquivos:

- `resultados/municipios_dengue_por_ano.csv`

- `dados/processados/populacao_ceara_historica.csv`

O cruzamento utilizou o código municipal de seis dígitos e o ano de início dos sintomas. Os códigos IBGE de sete dígitos foram padronizados para permitir a correspondência.

A taxa foi calculada pela fórmula:

**Taxa por 100 mil habitantes = (Total de registros / População municipal) × 100.000**

O resultado foi salvo em:

`resultados/taxas_dengue_municipios_2016_2025.csv`

### 19.3. Validação do processamento

- Municípios: 184.

- Anos: 10, de 2016 a 2025.

- Observações município-ano: 1.840.

- Registros municipais classificados de dengue: 215.243.

- Correspondência com a base populacional: completa.

- Populações ausentes após o cruzamento: nenhuma.

### 19.4. Taxas anuais agregadas do Ceará

| Ano | Registros | População | Taxa por 100 mil |

|---|---:|---:|---:|

| 2016 | 41.894 | 8.963.663 | 467,38 |

| 2017 | 27.055 | 9.020.460 | 299,93 |

| 2018 | 3.995 | 9.075.649 | 44,02 |

| 2019 | 15.674 | 9.132.078 | 171,64 |

| 2020 | 21.451 | 9.187.103 | 233,49 |

| 2021 | 33.841 | 9.240.580 | 366,22 |

| 2022 | 39.938 | 8.794.957 | 454,10 |

| 2023 | 14.220 | 8.794.957 | 161,68 |

| 2024 | 12.127 | 9.233.656 | 131,33 |

| 2025 | 5.048 | 9.268.836 | 54,46 |

As taxas estaduais apresentadas nesta seção foram calculadas pela divisão da soma dos registros **com município cearense válido** pela população total do Ceará em cada ano, evitando o uso de médias simples das taxas municipais. Por esse motivo, os numeradores de 2021, 2022, 2024 e 2025 são ligeiramente inferiores aos da série temporal estadual, que inclui oito registros sem município cearense válido.

### 19.5. Investigação da diferença entre análises temporal e municipal

Foi identificada uma diferença de oito registros entre a análise temporal estadual, com 215.251 registros, e a análise municipal, com 215.243.

A investigação da variável `ID_MN_RESI`, após a exclusão dos 62 registros com atraso extremo de notificação, identificou:

- Seis registros sem código de município de residência.

- Um registro com código municipal `353440`.

- Um registro com código municipal `420910`.

Distribuição anual dos oito registros:

| Ano | Registros sem município cearense válido |

|---|---:|

| 2021 | 4 |

| 2022 | 2 |

| 2024 | 1 |

| 2025 | 1 |

| **Total** | **8** |

**Decisão metodológica:** manter os 215.251 registros na análise temporal estadual e utilizar 215.243 registros na análise espacial municipal, excluindo desta última os oito registros sem correspondência com os municípios do Ceará.

Os arquivos originais e a base analítica foram preservados, sem alterações manuais. A inclusão desses oito registros na série temporal estadual decorre do critério inicial `SG_UF = 23`; a ausência de correspondência de `ID_MN_RESI` com um município cearense impede atribuí-los espacialmente a um dos 184 municípios. Essa diferença de campos deve ser descrita como limitação da seleção geográfica.

### 19.6. Observações e limitações

As taxas representam os registros classificados de dengue disponíveis na base analítica e não devem ser interpretadas automaticamente como indicadores oficiais de incidência.

A interpretação temporal deve considerar a descontinuidade entre estimativas populacionais e dados censitários, especialmente em 2022 e 2023. Como o denominador de 2023 foi derivado do Censo 2022, sua utilização limita a interpretação de variações anuais das taxas. Também é necessário verificar a completude dos registros de 2025.

### 19.7. Próxima etapa

Investigar os municípios com maiores taxas anuais de registros de dengue, gerar gráficos comparativos e avaliar a evolução espacial e temporal das taxas no período de 2016 a 2025.

## 20. Análise comparativa municipal — 2024

Foi realizada uma análise das taxas de registros classificados de dengue por 100 mil habitantes nos 184 municípios do Ceará, utilizando o arquivo `resultados/taxas_dengue_municipios_2016_2025.csv`.

O ranking das maiores taxas identificou Brejo Santo (4.425,60), Porteiras (2.688,08), Altaneira (2.568,15) e Penaforte (2.213,15) nas primeiras posições.

Dos 184 municípios, 37 apresentaram taxas superiores à taxa estadual de 131,33 registros por 100 mil habitantes, enquanto cinco não apresentaram registros classificados na base analisada em 2024.

Foi gerado o gráfico `resultados/graficos/top10_taxas_dengue_2024.png`, apresentando os dez municípios com maiores taxas.

Na comparação com os números absolutos, Fortaleza apresentou o maior total de registros (3.403), mas sua taxa foi de 132,19 por 100 mil habitantes. Brejo Santo apresentou 2.380 registros e taxa de 4.425,60 por 100 mil habitantes.

A comparação mostrou que os rankings por números absolutos e por taxas populacionais diferem, reforçando a importância da padronização populacional para interpretar a distribuição municipal dos registros. A comparação é descritiva; não foi realizado teste estatístico de significância.

**Encaminhamento registrado à época:** ampliar a comparação para 2016–2025. Essa investigação foi posteriormente iniciada nas seções 21 e 22.

## 21. Comparação histórica das taxas de dengue — Brejo Santo e Ceará (2016–2025)

Foi realizada uma comparação entre as taxas anuais de registros classificados de dengue em Brejo Santo e no conjunto dos municípios do Ceará, utilizando indicadores por 100 mil habitantes.

A análise identificou diferenças expressivas entre o comportamento municipal e o estadual.

Em 2017, Brejo Santo apresentou taxa de 2.877,33 registros por 100 mil habitantes, aproximadamente 9,59 vezes a taxa estadual de 299,93.

Em 2023, a taxa municipal atingiu 3.491,88, enquanto a estadual foi de 161,68, correspondendo a uma razão de 21,60.

Em 2024, Brejo Santo apresentou a maior taxa da série histórica, com 4.425,60 registros por 100 mil habitantes, aproximadamente 33,70 vezes a taxa estadual de 131,33.

Em oito dos dez anos analisados, a taxa municipal superou a estadual. As exceções ocorreram em 2016 e 2021.

Foi desenvolvido o script `scripts/grafico_comparativo_brejo_ceara.py`, responsável por gerar a figura:

`resultados/graficos/comparativo_brejo_ceara_2016_2025.png`

**Interpretação preliminar:** os resultados indicam diferenças temporais importantes entre Brejo Santo e o conjunto do Ceará. Entretanto, a análise descritiva não permite estabelecer as causas dessas diferenças.

**Limitação:** os dados de 2025 devem ser interpretados considerando a possibilidade de incompletude dos registros.

**Encaminhamento registrado à época:** investigar a distribuição histórica das taxas nos municípios. A análise exploratória de recorrência e o mapa de calor de 15 municípios foram realizados posteriormente, conforme a seção 22; a representação geográfica dos 184 municípios permanece pendente.

## 22. Análise histórica municipal por mapa de calor — 2016 a 2025

Foi desenvolvido o script `scripts/heatmap_taxas_municipais.py`, utilizando Pandas, Matplotlib e Seaborn para representar graficamente as taxas anuais de registros classificados de dengue.

Foram selecionados os 15 municípios com maior recorrência de taxas superiores à taxa estadual, considerando o período de 2016 a 2025.

O gráfico foi salvo em:

`resultados/graficos/heatmap_taxas_municipais.png`

A análise visual identificou diferenças importantes entre os padrões temporais municipais.

Brejo Santo apresentou picos em 2017, 2023 e 2024. Quixeré apresentou taxas elevadas em 2019 e 2021. Tabuleiro do Norte apresentou valores expressivos em diferentes anos, enquanto Aratuba registrou uma taxa particularmente elevada em 2022.

Quatro municípios apresentaram taxas superiores à estadual em oito dos dez anos: Brejo Santo, Quixeré, Tabuleiro do Norte e Fortaleza.

**Conclusão preliminar:** os resultados evidenciam heterogeneidade temporal entre os municípios selecionados, com períodos de maior concentração de registros classificados de dengue ocorrendo em anos distintos.

A análise é descritiva e não permite determinar as causas dessas diferenças.

**Limitações:** a seleção dos municípios baseou-se na recorrência relativa à taxa estadual. Os resultados não representam a totalidade dos padrões municipais do Ceará. Os dados de 2025 também exigem avaliação de completude.

**Próxima etapa:** ampliar a representação geográfica para os 184 municípios do Ceará. A identificação de possíveis agrupamentos espaciais exigirá método específico e não pode ser inferida apenas do mapa de calor temporal.

**Documento interno de acompanhamento da pesquisa. Os resultados apresentados são preliminares e estão sujeitos a verificações, revisões metodológicas e validação científica antes de sua utilização no artigo final.**

---

## 23. Atualização do acompanhamento científico e editorial — 18/11/2026

**Finalidade:** registrar a evolução do trabalho posterior à seção 22, sem apagar decisões históricas nem transformar informações ainda não revalidadas em resultados científicos definitivos.

### 23.1. Situação da pesquisa e do artigo

- O projeto permanece centrado na análise temporal e espacial de registros classificados como dengue no Ceará entre 2016 e 2025, utilizando dados públicos do Ministério da Saúde e denominadores populacionais do IBGE.
- O artigo científico será entregue em formato LaTeX, no modelo institucional do IFCE, Campus Maracanaú.
- **Prazo informado:** envio da versão LaTeX ao orientador em **18/11/2026**; entrega final prevista para **20/11/2026**.
- Foram preparados rascunhos do artigo em Markdown e iniciada a adaptação ao modelo LaTeX, com arquivos `main.tex`, `01-Pre-Textual/Resumo.tex` e `01-Pre-Textual/Abstract.tex`. O resumo em português foi redigido em versão preliminar, mas sua redação final depende da conferência dos resultados e da consistência com o artigo.
- **Prioridade imediata:** consolidar um manuscrito completo e revisável, com figuras, tabelas, referências verificadas e compilação do LaTeX. Novas análises opcionais não devem impedir o envio ao orientador.

### 23.2. Ampliação geográfica e regional relatada no desenvolvimento do projeto

Na revisão dos rascunhos do trabalho foram mencionadas etapas posteriores à seção 22: produção de mapas temáticos municipais para 2016–2025, exploração das 18 Regiões Geográficas Imediatas do Ceará, comparação de sazonalidade regional e investigação descritiva de registros em Pentecoste.

Os seguintes resultados foram **relatados em versão posterior do artigo**, mas **não constam deste diário original até a seção 22**. Devem ser confrontados com os arquivos de resultados, scripts e figuras antes de serem tratados como validados:

| Análise | Resultado relatado | Estado de conferência |
|---|---|---|
| Mapas municipais | 27 municípios acima de 700 registros por 100 mil habitantes em 2022; dois em 2018 | Conferir tabela de taxas e mapa/legenda |
| Sazonalidade regional | 135 das 180 combinações região-ano tiveram pico mensal entre março e junho | Conferir agregação e critério de desempate dos picos |
| Região de Brejo Santo | Taxa regional de 1.704,39 por 100 mil habitantes em 2024 | Conferir limites regionais, numerador e denominador |
| Região de Russas–Limoeiro do Norte | Taxa regional superior à estadual em dez anos | Conferir série regional anual |
| Pentecoste | Concentração de registros em novembro de 2016 | Conferir série local e não classificar automaticamente como surto |

**Decisão:** manter os itens acima como *resultados relatados, pendentes de reconciliação*, até a leitura dos respectivos CSVs, scripts e gráficos. Não inferir significância estatística, agrupamento espacial ou causalidade apenas a partir de mapas e contagens.

### 23.3. Produtos a localizar no projeto

A revisão final deverá identificar os nomes e caminhos efetivos de: scripts que produzem mapas municipais; tabelas agregadas das 18 regiões; gráficos de sazonalidade regional; análise específica de Pentecoste; figuras finais que serão incluídas no artigo; e bibliografia efetivamente consultada.

**Limitação desta atualização:** não foi disponibilizada nesta etapa uma cópia integral e atual do repositório com todos os scripts, tabelas e figuras. A seção 23.2 é um roteiro de verificação, não uma auditoria independente desses resultados.

## 24. Consolidação dos quantitativos e prevenção de inconsistências

### 24.1. Fluxo de seleção documentado

| Etapa | Quantidade de registros | Interpretação |
|---|---:|---|
| Arquivos históricos filtrados por `SG_UF = 23` | 416.095 | Linhas de origem, não casos únicos |
| Classificação `CLASSI_FIN` em {10, 11, 12} | 215.748 | Registros classificados nos arquivos históricos |
| Início dos sintomas delimitado a 2016–2025 | 215.313 | Base analítica antes do filtro de atraso extremo |
| Exclusão operacional de 62 atrasos acima de 365 dias | 215.251 | Série temporal estadual |
| Exclusão espacial de oito registros sem município cearense válido | 215.243 | Agregação municipal e taxas derivadas |

**Verificações aritméticas:** 215.748 − 435 = 215.313; 215.313 − 62 = 215.251; 215.251 − 8 = 215.243.

**Importante:** os 435 registros que não entraram no recorte temporal ainda precisam ser discriminados entre datas fora do intervalo e datas ausentes ou inválidas. Os 62 atrasos extremos foram preservados na base e excluídos das análises definidas; isso não prova erro individual. As oito linhas sem município válido não foram descartadas da série estadual.

### 24.2. Séries anuais com universos diferentes

Os totais anuais abaixo provêm das seções 16 e 19 do diário. A diferença não deve ser tratada como contradição: a coluna municipal exclui oito registros que não puderam ser atribuídos aos municípios cearenses.

| Ano | Série temporal estadual | Série municipal | Diferença |
|---|---:|---:|---:|
| 2016 | 41.894 | 41.894 | 0 |
| 2017 | 27.055 | 27.055 | 0 |
| 2018 | 3.995 | 3.995 | 0 |
| 2019 | 15.674 | 15.674 | 0 |
| 2020 | 21.451 | 21.451 | 0 |
| 2021 | 33.845 | 33.841 | 4 |
| 2022 | 39.940 | 39.938 | 2 |
| 2023 | 14.220 | 14.220 | 0 |
| 2024 | 12.128 | 12.127 | 1 |
| 2025 | 5.049 | 5.048 | 1 |
| **Total** | **215.251** | **215.243** | **8** |

Ao apresentar os resultados no artigo, informar explicitamente o universo de cada tabela, gráfico ou taxa. Não substituir os números da série temporal pelos números municipais sem explicar a mudança de critério.

### 24.3. Taxas e limites interpretativos

As taxas por 100 mil habitantes foram calculadas com registros classificados e populações municipais do IBGE. Elas **não equivalem automaticamente à incidência oficial de casos confirmados**. Os denominadores de 2022 e 2023 exigem cautela: os dados de 2023 se baseiam no Censo 2022 e não representam uma estimativa populacional independente para aquele ano. A completude de 2025 permanece não verificada.

### 24.4. Pontos que ainda exigem reconciliação

1. Conferir a composição dos 435 registros excluídos na delimitação temporal.
2. Verificar a interpretação dos códigos `CLASSI_FIN` ainda não esclarecidos e dos 5.761 registros com `CRITERIO = 3` entre os 215.748 classificados nos arquivos de origem.
3. Revisar a sensibilidade do recorte de 62 atrasos extremos e a possibilidade de duplicidades não detectadas.
4. Confirmar o estado de atualização dos arquivos de 2025 e evitar atribuir a menor contagem a uma redução epidemiológica comprovada.
5. Conferir os cálculos regionais e os mapas com os CSVs e scripts que os geraram.
6. Verificar referências e fontes documentais antes de incorporar citações ao artigo.

## 25. Plano de finalização do artigo científico

### 25.1. Estrutura editorial proposta

1. Resumo e palavras-chave; Abstract e keywords.
2. Introdução, problema de pesquisa, objetivo geral e objetivos específicos.
3. Fundamentação teórica: dengue, vigilância epidemiológica, qualidade de dados secundários, séries temporais e análise espacial descritiva.
4. Metodologia: fontes, recortes, critérios de classificação, tratamento de datas, agregação temporal, validação municipal, populações e taxas, ferramentas computacionais e limitações.
5. Resultados e discussão: fluxo da base, série anual e mensal, sazonalidade, rankings e taxas municipais, comparações históricas, mapas municipais e regiões (somente após conferência).
6. Conclusão: principais achados descritivos, limitações e contribuições, sem inferências causais não testadas.
7. Referências verificadas e padronizadas para o modelo do IFCE.

### 25.2. Critérios de revisão antes do envio

- Cada número no resumo deve corresponder a uma tabela, figura ou resultado conferido no texto.
- Toda figura deve ter legenda, fonte, período e definição clara do indicador.
- Não confundir notificações brutas, registros classificados, casos únicos e casos confirmados.
- Evitar chamar mapas descritivos de prova de autocorrelação ou agrupamento espacial.
- Indicar que o recorte de 2025 pode estar incompleto.
- Validar a compilação do projeto LaTeX e a posição de resumo e abstract conforme o modelo institucional.
- Confirmar com o orientador eventuais ajustes de estrutura, extensão e bibliografia.

## 26. Registro de controle de versão desta atualização

**Data:** 18/11/2026.

**Documento de origem:** `diario_pesquisa(1).md`, com histórico das seções 1 a 22 preservado.

**Mudanças:** atualização da nota editorial; inclusão das seções 23 a 26, com andamento do artigo, resultados geográficos/regionais relatados, quadro de reconciliação dos totais, pendências e plano de finalização.

**Natureza:** atualização documental. Nenhum CSV, script ou mapa foi reexecutado ou auditado nesta edição. Os resultados regionais citados na seção 23.2 precisam ser validados nos artefatos atuais do projeto.

