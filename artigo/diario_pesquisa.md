# Diário de Pesquisa — TCC Dengue Ceará

**Projeto:** Análise temporal e espacial dos registros de dengue no Ceará entre 2016 e 2025 utilizando Python

**Curso:** Ciência da Computação — Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE), Campus Maracanaú

**Situação:** Pesquisa em desenvolvimento

**Natureza do documento:** Registro interno de acompanhamento científico e metodológico

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
│   ├── diario_pesquisa.md
│   └── rascunho.md
├── dados/
│   ├── originais/
│   └── processados/
├── resultados/
│   └── graficos/
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

Esse código corresponde ao estado do Ceará.

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

**Observação de conferência:** a soma dos valores anuais é 215.748. Um total anterior de 215.471 havia sido registrado no diário, mas não corresponde à soma da tabela. O valor consolidado deverá ser confirmado novamente por execução do script antes de ser utilizado no artigo.

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

## 11. Pendências metodológicas

Antes da produção dos resultados definitivos, permanecem as seguintes pendências:

- Investigar possíveis duplicidades entre arquivos históricos.
- Esclarecer os códigos de `CLASSI_FIN` não documentados nas fontes consultadas.
- Investigar a diferença de distribuição das classificações entre 2016–2021 e 2022–2025.
- Avaliar a consistência da variável `CRITERIO` em todos os anos.
- Definir os critérios finais de identificação dos casos confirmados.
- Estabelecer regras de tratamento das datas inconsistentes.
- Verificar a consistência dos códigos municipais.
- Avaliar a completude dos dados referentes aos anos mais recentes.
- Definir o tratamento de registros com datas fora do período de 2016 a 2025.
- Investigar possíveis alterações de estrutura e cobertura das bases históricas.
- Obter dados populacionais oficiais para calcular taxas por 100 mil habitantes.
- Definir os métodos estatísticos para avaliação de tendências e sazonalidade.

## 12. Próximas etapas da pesquisa

1. Concluir a investigação das classificações e dos critérios de confirmação.
2. Verificar possíveis duplicidades e inconsistências entre os arquivos.
3. Definir e implementar as regras de limpeza.
4. Construir bases analíticas separadas para notificações e casos classificados como dengue.
5. Consolidar as séries temporais referentes ao período de 2016 a 2025.
6. Produzir análises anuais e mensais.
7. Investigar a distribuição espacial por município.
8. Calcular taxas por 100 mil habitantes, quando disponíveis os denominadores adequados.
9. Aplicar técnicas de análise de tendências e sazonalidade.
10. Interpretar os resultados à luz da documentação e das limitações dos dados.
11. Elaborar e revisar o artigo científico.

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

## 15. Referências documentais e técnicas

**BRASIL. Ministério da Saúde.** Portal de Dados Abertos. Conjunto de dados de arboviroses — dengue. Disponível em: https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue.

**BRASIL. Ministério da Saúde.** Dicionário de Dados do SINAN Online, versão 3.0, revisado em 2015. Documento técnico consultado durante a pesquisa.

**BRASIL. Ministério da Saúde.** Nota Informativa nº 59/2016 — CGPNCD/DEVIT/SVS/MS. Documento técnico consultado durante a pesquisa.

**Documentação do pandas:** https://pandas.pydata.org/docs/

**Documentação do Matplotlib:** https://matplotlib.org/stable/

As referências bibliográficas serão posteriormente revisadas e padronizadas conforme as exigências do artigo científico e do IFCE.

---

*Documento interno de acompanhamento da pesquisa. Os resultados apresentados são preliminares e estão sujeitos a verificações, revisões metodológicas e validação científica antes de sua utilização no artigo final.*