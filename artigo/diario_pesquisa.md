# Diário de Pesquisa — TCC Dengue Ceará

**Projeto:** Análise temporal e espacial dos registros de dengue no Ceará entre 2016 e 2025 utilizando Python

**Curso:** Ciência da Computação — Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE), Campus Maracanaú

**Orientador:** Prof. Fabio Jose Gomes de Sousa

**Situação:** Pesquisa em desenvolvimento

**Natureza do documento:** Registro interno de acompanhamento científico e metodológico

**Nota editorial:** este diário preserva registros históricos de etapas preliminares. As seções posteriores atualizam resultados e decisões anteriores; para o estado atual das pendências, consultar a seção 11.

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

### 3.1. Ferramentas

- Python — linguagem de programação.

- pandas — leitura, filtragem e manipulação dos dados.

- Matplotlib — geração de gráficos.

- Visual Studio Code — edição e execução dos scripts.

- Git — controle de versões.

- GitHub — armazenamento e acompanhamento do código-fonte.

### 3.2. Estratégia de processamento

Devido ao tamanho dos arquivos originais, foi adotada a leitura em blocos com pandas, utilizando:

`chunksize=100_000`

Essa estratégia permite processar os arquivos sem carregar todas as linhas simultaneamente na memória.

O projeto utiliza scripts independentes para preparação, exploração e validação dos dados, favorecendo a organização e a reprodutibilidade das análises.

## 4. Organização do projeto

A estrutura principal do projeto é composta por:

```text

TCC_Dengue_Ceara/

├── artigo/

│   ├── diario_pesquisa.md

│   └── rascunho.md

├── dados/

│   ├── originais/

│   └── processados/

├── resultados/

│   └── graficos/

├── scripts/

├── .gitignore

└── README.md

```

### 4.1. Finalidade dos diretórios

**`artigo/`:** documentação da pesquisa e elaboração do artigo científico.

**`dados/originais/`:** armazenamento das bases públicas sem alterações.

**`dados/processados/`:** armazenamento dos arquivos filtrados para o Ceará.

**`scripts/`:** códigos utilizados na preparação, verificação e análise dos dados.

**`resultados/`:** tabelas, relatórios e gráficos produzidos durante a pesquisa.

A pasta `dados/` e os arquivos CSV de resultados definidos no `.gitignore` não são enviados ao repositório.

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

Esta seção registra o estado atual da pesquisa. As decisões e os resultados preliminares das etapas anteriores permanecem documentados nas seções correspondentes.

### 11.1. Etapas já realizadas

- Preparação dos dez arquivos históricos, com filtragem inicial por `SG_UF = 23`.
- Investigação exploratória da variável `CLASSI_FIN` e da distribuição de `CRITERIO`.
- Investigação exploratória de combinações repetidas dentro dos arquivos e entre anos, **sem confirmação de duplicidade individual e sem exclusão automática**.
- Construção da base analítica com referência ao início dos sintomas e delimitação do período de 2016 a 2025.
- Identificação de 62 registros com intervalo entre sintomas e notificação superior a 365 dias; exclusão apenas das análises que aplicam esse filtro, com preservação da base.
- Consolidação da série temporal mensal e exploração da sazonalidade.
- Validação dos códigos municipais e identificação dos oito registros sem município cearense válido para a análise espacial.
- Consolidação das populações municipais de 2016 a 2025 e cálculo das taxas anuais por 100 mil habitantes.
- Produção dos rankings municipais de 2024, da comparação Brejo Santo × Ceará e do mapa de calor exploratório de 15 municípios.

### 11.2. Pendências que permanecem abertas

- Esclarecer os códigos de `CLASSI_FIN` ainda não interpretados e as diferenças de classificação entre períodos.
- Investigar a interpretação de `CRITERIO = 3` nos registros classificados como dengue e consolidar a definição operacional de casos para o artigo.
- Avaliar a sensibilidade dos resultados à inclusão dos 62 registros com atrasos extremos e à eventual existência de duplicidades não detectáveis pelos atributos examinados.
- Confirmar, nos dados processados, a composição exata dos 435 registros classificados não incluídos no intervalo analítico de 2016 a 2025, incluindo a eventual presença de datas ausentes ou inválidas.
- Verificar a completude, a cobertura e a comparabilidade das bases históricas, especialmente em 2025.
- Confirmar documentalmente a razão das diferenças populacionais de Ereré e Pereiro entre as fontes de 2022 e 2023.
- Obter e validar a malha territorial dos 184 municípios para os mapas geográficos; definir, se pertinente, métodos de análise de agrupamentos espaciais.
- Definir e executar métodos estatísticos de tendência e sazonalidade, com avaliação das limitações dos dados.
- Revisar a terminologia, as fontes e as referências segundo as exigências do IFCE e do orientador.

## 12. Próximas etapas da pesquisa

1. Concluir as verificações metodológicas ainda abertas e registrar as decisões definitivas de inclusão e exclusão.
2. Avaliar a sensibilidade das séries aos atrasos extremos e a qualidade/completude dos anos recentes.
3. Obter e validar os limites geográficos municipais do IBGE.
4. Produzir mapas temáticos para os 184 municípios, distinguindo descrição espacial de testes formais de agrupamento.
5. Aplicar, quando justificado, métodos estatísticos de tendências e sazonalidade.
6. Consolidar resultados, limitações e referências no artigo científico.

## 13. Registro das decisões metodológicas

### 13.1. Filtragem geográfica

**Problema:** selecionar os registros referentes ao Ceará em bases nacionais de grande volume.

**Procedimento:** leitura em blocos e filtragem por `SG_UF = 23`.

**Resultado:** 416.095 linhas selecionadas nos dez arquivos históricos.

**Decisão:** preservar os arquivos originais e manter os registros filtrados em arquivos separados.

**Justificativa:** possibilitar rastreabilidade e reprocessamento dos dados.

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
