# Análise Temporal e Espacial da Dengue no Estado do Ceará entre 2016 e 2025 Utilizando Análise de Dados

**Autor:** Victor Iuri Costa Sousa — victor.iuri.costa60@aluno.ifce.edu.br  
**Orientador:** Prof. Fabio Jose Gomes de Sousa — fabio.jose@ifce.edu.br  
**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE), Campus Maracanaú  
**Curso:** Ciência da Computação

> **Nota de revisão (não incluir na versão submetida):** Consolidação editorial dos três rascunhos fornecidos. Os valores e as referências foram preservados a partir desses documentos; não houve reexecução de scripts nem conferência dos CSVs ou das fontes bibliográficas externas. Verificar especialmente os códigos de classificação, os 435 registros fora do recorte, os 62 intervalos extremos, os resultados regionais e a completude de 2025. As imagens referenciadas dependem da pasta `resultados/graficos/` no projeto local.

## Resumo

A dengue representa um desafio para a vigilância em saúde, e a análise de bases públicas permite descrever sua distribuição temporal e territorial. O objetivo deste estudo foi analisar registros classificados como dengue no Ceará entre 2016 e 2025, considerando padrões temporais, municipais e regionais. Foi conduzido um estudo quantitativo, retrospectivo e descritivo com dez arquivos históricos do Ministério da Saúde e dados populacionais do IBGE. O processamento em Python incluiu filtragem, verificação de classificações e datas, agregações mensais, cálculo de taxas por 100 mil habitantes e elaboração de mapas municipais e análises das 18 Regiões Geográficas Imediatas. A filtragem inicial reuniu 416.095 registros; 215.251 integraram a série temporal e 215.243 possuíam município cearense válido para a análise territorial. Os maiores totais anuais da série ocorreram em 2016 (41.894) e 2022 (39.940). Entre março e junho concentraram-se aproximadamente 65,5% dos registros. Fortaleza apresentou o maior total municipal acumulado (90.035), enquanto Brejo Santo registrou taxa municipal de 4.425,60 por 100 mil habitantes em 2024. Na análise regional, 135 de 180 combinações região-ano apresentaram pico mensal entre março e junho; a região de Russas–Limoeiro do Norte superou a taxa estadual em todos os dez anos. Os resultados evidenciam heterogeneidade temporal e territorial, sem demonstrar causalidade ou agrupamentos espaciais estatisticamente significativos. As taxas calculadas não devem ser equiparadas automaticamente à incidência oficial, e a completude de 2025 ainda precisa ser avaliada.

**Palavras-chave:** Dengue. Análise de dados. Séries temporais. Distribuição espacial. Vigilância epidemiológica.

## 1. Introdução

A dengue constitui um desafio para a saúde pública brasileira e demanda acompanhamento de sua distribuição temporal e geográfica. Bases públicas de vigilância epidemiológica possibilitam análises computacionais que auxiliam na descrição de padrões de registros, na identificação de inconsistências e na comparação de municípios com diferentes populações.

Este estudo examina os registros classificados como dengue no Ceará entre 2016 e 2025, com base em arquivos históricos do Ministério da Saúde. Diferenciam-se as notificações disponíveis nos arquivos de origem dos registros selecionados por classificação final e qualidade temporal. Os resultados não são tratados automaticamente como contagens de casos únicos ou indicadores oficiais de incidência.

### 1.1. Objetivo geral
Analisar a evolução temporal e a distribuição municipal dos registros classificados como dengue no Ceará entre 2016 e 2025, utilizando técnicas computacionais de preparação, validação, agregação e visualização de dados.

### 1.2. Objetivos específicos
- Processar e organizar os arquivos históricos de dengue disponibilizados pelo Ministério da Saúde.

- Examinar a consistência de datas, classificações e possíveis coincidências entre registros.

- Construir séries anuais e mensais por data de início dos sintomas.

- Comparar os totais e as taxas municipais de registros por 100 mil habitantes.

- Investigar a sazonalidade e a heterogeneidade temporal entre municípios.

- Descrever a distribuição geográfica das taxas municipais e regionais e investigar a recorrência de valores acima da taxa estadual.

## 2. Fundamentação teórica

### 2.1. Dengue e vigilância epidemiológica

A dengue é uma doença infecciosa causada pelo vírus da dengue (DENV), transmitido aos seres humanos principalmente pela picada de mosquitos infectados da espécie *Aedes aegypti*. Sua ocorrência é especialmente relevante em regiões tropicais e subtropicais, constituindo um importante desafio para a saúde pública (ORGANIZAÇÃO MUNDIAL DA SAÚDE, 2025).

No Brasil, a dengue integra a lista de doenças de notificação compulsória. Os casos suspeitos e confirmados devem ser comunicados aos serviços de vigilância epidemiológica, sendo seus registros inseridos no Sistema de Informação de Agravos de Notificação (Sinan). Esse processo contribui para o acompanhamento da situação epidemiológica e para o planejamento das ações de prevenção e controle (BRASIL, 2022).

A utilização de dados secundários provenientes dos sistemas de vigilância permite examinar a distribuição temporal e geográfica dos registros de dengue. Entretanto, sua interpretação exige atenção aos critérios de classificação, à qualidade do preenchimento e às diferenças entre notificações, registros classificados e indicadores oficiais de incidência.

Nesse contexto, a análise computacional de dados públicos constitui uma abordagem relevante para descrever padrões epidemiológicos. No presente estudo, essa abordagem é aplicada aos registros classificados como dengue no Ceará entre 2016 e 2025, considerando sua evolução temporal e distribuição espacial.

### 2.2. Sazonalidade da dengue e fatores climáticos

A dengue apresenta variações temporais relacionadas a fatores ambientais, climáticos e epidemiológicos. A precipitação, a temperatura e a umidade podem influenciar as condições de desenvolvimento e sobrevivência do mosquito *Aedes aegypti*, contribuindo para alterações na dinâmica de transmissão da doença.

Soares, Araújo e Almeida (2021), ao investigarem a ocorrência de dengue em Fortaleza entre 2014 e 2019, identificaram relações entre os registros da doença e variáveis meteorológicas, incluindo precipitação, temperatura e velocidade do vento.

Costa e Araújo (2021) analisaram a relação entre precipitação e dengue em quatro municípios cearenses com características geográficas distintas: Aquiraz, Boa Viagem, Viçosa do Ceará e Brejo Santo. Os autores observaram diferenças entre os municípios, demonstrando que a distribuição temporal da doença não pode ser explicada exclusivamente pelo volume de chuvas.

Magalhães e Zanella (2013), em estudo sobre a Região Metropolitana de Fortaleza, identificaram que, em determinados anos, os maiores totais de dengue ocorreram após períodos de precipitação elevada, evidenciando a importância de considerar possíveis defasagens temporais entre as condições meteorológicas e os registros da doença.

Dessa forma, a análise da sazonalidade constitui uma ferramenta importante para compreender a distribuição temporal da dengue. Entretanto, a identificação de associações entre registros epidemiológicos e fatores climáticos exige a integração de dados meteorológicos e a aplicação de métodos estatísticos apropriados.

### 2.3. Análise espacial e geoprocessamento aplicados à dengue

A análise espacial constitui uma abordagem relevante para a investigação da distribuição geográfica de doenças, permitindo identificar diferenças territoriais e examinar padrões de ocorrência em unidades geográficas distintas. No contexto da dengue, técnicas de geoprocessamento possibilitam representar indicadores epidemiológicos por meio de mapas temáticos e investigar sua distribuição no território.

Araújo, Ferreira e Abreu (2008), em revisão sistemática sobre estudos de espacialização da dengue no Brasil, destacaram a utilização de técnicas de geoprocessamento na investigação da doença e de seu vetor. Essas ferramentas contribuem para a representação e interpretação da distribuição geográfica dos registros epidemiológicos.

Silva et al. (2020), ao analisarem a distribuição espacial da dengue nos 223 municípios da Paraíba entre 2007 e 2016, utilizaram técnicas de autocorrelação espacial, incluindo os índices de Moran global e local. Os autores identificaram dependência espacial significativa e destacaram a importância de considerar fatores socioambientais na interpretação da distribuição da doença.

A utilização de taxas populacionais permite comparar municípios com diferentes tamanhos populacionais, reduzindo as distorções decorrentes da análise exclusiva de números absolutos. A representação cartográfica desses indicadores facilita a identificação visual de diferenças territoriais, embora a presença de áreas com taxas elevadas não constitua, isoladamente, comprovação estatística de agrupamentos espaciais.

Para a análise regional, o Instituto Brasileiro de Geografia e Estatística (IBGE) disponibiliza a Divisão Regional do Brasil em Regiões Geográficas Imediatas e Intermediárias, publicada em 2017. Essa regionalização considera a organização territorial e as articulações entre centros urbanos, fornecendo unidades de referência para análises estatísticas e geográficas (IBGE, 2017).

No presente estudo, essas abordagens fundamentam a utilização de mapas temáticos, taxas municipais por 100 mil habitantes e agregações por Regiões Geográficas Imediatas do Ceará. A análise realizada possui caráter descritivo e exploratório, sem aplicação, nesta etapa, de testes formais de autocorrelação espacial.

### 2.4. Ciência de dados e Python aplicados à saúde pública

A crescente disponibilidade de bases públicas de informações em saúde amplia as possibilidades de utilização de métodos computacionais para investigar a distribuição temporal e espacial de doenças. Nesse contexto, a ciência de dados reúne técnicas de coleta, organização, processamento, análise e visualização de informações, permitindo transformar grandes volumes de registros em indicadores úteis à pesquisa científica.

A linguagem de programação Python apresenta recursos para o desenvolvimento de procedimentos de análise de dados, incluindo manipulação de tabelas, tratamento de valores ausentes, integração de diferentes fontes e elaboração de representações gráficas. Sua utilização em pesquisas quantitativas possibilita a automatização de tarefas e a documentação dos procedimentos empregados.

McKinney (2010) apresentou o pandas como uma biblioteca voltada à manipulação e à análise de dados estruturados em Python. Seus recursos permitem realizar operações de filtragem, agrupamento, integração e transformação de tabelas, fundamentais para o processamento de bases epidemiológicas.

Hunter (2007) descreveu o Matplotlib como uma biblioteca para a construção de visualizações científicas em Python. A ferramenta permite produzir gráficos que auxiliam na identificação de tendências, variações temporais e diferenças entre grupos de observações.

No campo da análise geográfica, o GeoPandas permite integrar tabelas a geometrias e elaborar representações cartográficas. Neste trabalho, foi empregado para associar as taxas aos limites municipais e às Regiões Geográficas Imediatas.

## 3. Metodologia

### 3.1. Caracterização da pesquisa
Estudo quantitativo, observacional, retrospectivo e descritivo, baseado em dados secundários públicos. A análise foi desenvolvida em Python, com processamento reprodutível e preservação dos arquivos originais. As comparações apresentadas não estabelecem relações causais.

### 3.2. Fontes e abrangência
Foram utilizados os dez arquivos históricos de dengue do Ministério da Saúde, identificados como `DENGBR16.csv` a `DENGBR25.csv`. A seleção inicial utilizou `SG_UF = 23`, correspondente ao Ceará, totalizando **416.095 linhas** nos arquivos de origem filtrados. O ano do nome do arquivo não foi utilizado como substituto da data de início dos sintomas.

Para as taxas populacionais, foram utilizadas publicações do Instituto Brasileiro de Geografia e Estatística (IBGE): estimativas municipais de 2016 a 2021 e de 2024 a 2025, dados do Censo Demográfico de 2022 (SIDRA, tabela 4714) e, para 2023, uma publicação baseada na população censitária de 2022 com referência à malha municipal de 2023. Portanto, o denominador adotado para 2023 **não constitui estimativa populacional independente daquele ano**.

### 3.3. Ferramentas e processamento
Foram utilizados Python, pandas, Matplotlib, Seaborn e GeoPandas para processamento, agregação e visualização de dados temporais e geográficos. Os arquivos extensos foram lidos em blocos de até 100.000 linhas. Scripts independentes foram empregados para preparar as bases, validar campos, agregar registros, calcular taxas e produzir figuras. Os dados originais foram mantidos separadamente dos processados.

### 3.4. Seleção dos registros e qualidade temporal
A classificação final foi examinada pela variável `CLASSI_FIN`, com apoio no Dicionário de Dados do SINAN Online e na Nota Informativa nº 59/2016 do Ministério da Saúde. Foram selecionados, para a análise descritiva, os códigos **10** (dengue), **11** (dengue com sinais de alarme) e **12** (dengue grave), totalizando **215.748 registros** antes da delimitação temporal. A variável `CRITERIO` também foi examinada; sua consistência e a interpretação de classificações não esclarecidas permanecem como limitações.

A referência temporal principal foi `DT_SIN_PRI` (início dos sintomas), enquanto `DT_NOTIFIC` foi utilizada para avaliar o intervalo entre sintomas e notificação. Após a delimitação ao período de 2016 a 2025, a base analítica continha **215.313 registros**, diferença de **435** em relação aos registros classificados inicialmente. A composição detalhada desses 435 registros, inclusive quanto a datas ausentes ou inválidas, **ainda deve ser confirmada diretamente nos scripts e arquivos processados**.

Entre os 215.313 registros, **62** apresentaram intervalo entre sintomas e notificação superior a 365 dias. Esses registros foram sinalizados e preservados na base analítica, mas excluídos das agregações temporais e municipais aqui apresentadas, restando **215.251 registros** para a série temporal. O limite de 365 dias é um critério operacional, não prova de erro; recomenda-se análise de sensibilidade futura.

A investigação exploratória de possíveis duplicidades encontrou combinações coincidentes de atributos, mas não permitiu identificar com segurança pessoas ou episódios repetidos. Por esse motivo, não houve exclusão automática de registros por coincidência de campos.

### 3.5. Construção das séries temporais
Os registros selecionados foram agregados por ano e mês de início dos sintomas, gerando uma série mensal de 120 observações entre janeiro de 2016 e dezembro de 2025. Foram examinados totais anuais, concentração por mês e picos mensais. A completude dos arquivos mais recentes, sobretudo de 2025, ainda requer avaliação.

### 3.6. Validação municipal e cálculo das taxas
A variável `ID_MN_RESI` foi confrontada com os códigos dos **184 municípios do Ceará**. Dos 215.251 registros temporais, **seis** não possuíam código municipal e **dois** continham códigos associados a outras unidades federativas (`353440` e `420910`). Os oito registros foram mantidos na série estadual definida pelo filtro inicial `SG_UF = 23`, mas excluídos das agregações por município de residência. Assim, **215.243 registros** compõem a análise municipal.

A base populacional histórica reúne **1.840 pares município-ano** (184 municípios × 10 anos), sem populações ausentes após a integração. Os códigos IBGE de sete dígitos foram compatibilizados com os códigos municipais de seis dígitos presentes na base de dengue, juntamente com o ano de início dos sintomas.

A taxa municipal de registros classificados por 100 mil habitantes foi calculada como:

\[

T_{m,a}=\frac{R_{m,a}}{P_{m,a}}\times 100.000

\]

Em que \(R_{m,a}\) é o número de registros classificados no município \(m\) e ano \(a\), e \(P_{m,a}\) é a população utilizada como denominador. Para a taxa estadual derivada da base municipal, foram somados os registros municipais e as populações dos 184 municípios em cada ano; **não** foi utilizada a média simples das taxas municipais.

A publicação populacional de 2023 manteve o total estadual de 2022 (8.794.957 habitantes), mas apresentou diferenças de −227 habitantes em Ereré e +227 em Pereiro. As fontes foram preservadas sem ajustes manuais. A causa dessa redistribuição permanece não confirmada.

Essas taxas são indicadores calculados a partir dos registros classificados disponíveis na base do estudo; não devem ser apresentadas automaticamente como taxas oficiais de incidência ou como medidas diretas de risco individual.

### 3.7. Comparações exploratórias entre municípios
Foram comparados rankings de números absolutos e taxas em 2024. Também foram calculadas, para cada município, as quantidades de anos em que sua taxa superou a taxa estadual correspondente. Os **15 municípios com maior recorrência** foram selecionados para um mapa de calor com anos nas colunas e municípios nas linhas. A seleção é exploratória e não representa, por si só, a distribuição de todos os municípios do Ceará nem comprova agrupamentos espaciais.

### 3.8. Análise espacial e regional

A distribuição espacial foi examinada com a malha municipal do IBGE de 2024, composta pelos 184 municípios do Ceará, em SIRGAS 2000 (EPSG:4674). Para comparabilidade visual, essa mesma malha foi utilizada nos mapas dos dez anos, sem pressupor estabilidade histórica de todos os limites territoriais. As taxas municipais foram representadas por mapas coropléticos contínuos e por seis classes descritivas definidas para o estudo: ausência de registros; maior que zero até 100; maior que 100 até 300; maior que 300 até 700; maior que 700 até 1.500; e maior que 1.500 registros por 100 mil habitantes. Essas classes não são limiares oficiais de risco epidemiológico.

Os municípios foram associados às 18 Regiões Geográficas Imediatas do IBGE, identificadas na malha pelos campos `CD_RGI` e `NM_RGI`. A associação foi validada para os 184 municípios, sem duplicações ou correspondências ausentes. Para cada região e ano, somaram-se os registros e as populações dos municípios componentes, calculando-se a taxa regional pela razão entre as duas somas multiplicada por 100.000; não se utilizou média aritmética das taxas municipais. Obtiveram-se 180 observações região-ano. A recorrência regional corresponde ao número de anos em que a taxa regional não arredondada superou a taxa estadual do mesmo ano, também calculada a partir dos registros com município de residência válido.

### 3.9. Sazonalidade mensal e investigação de concentrações atípicas

Os 215.251 registros temporais foram agrupados em 120 meses por data de início dos sintomas. Para a análise regional mensal, oito registros sem município cearense válido foram excluídos, restando 215.243 registros distribuídos em 2.160 combinações de 18 regiões, dez anos e 12 meses. Para comparar a forma da sazonalidade entre regiões de diferentes tamanhos, calculou-se a participação percentual de cada mês no total decenal de registros de sua respectiva região. Também foram identificados os meses de maior contagem em cada combinação região-ano; nos empates, o procedimento computacional seleciona o primeiro mês, o que exige cautela interpretativa.

Uma concentração atípica observada na região de Itapagé em novembro motivou investigação descritiva por ano, município e data de início dos sintomas. Essa exploração não constitui teste estatístico de surto nem comprova causalidade.

### 3.10. Análises ainda previstas

Permanecem previstas a avaliação da completude de 2025, a análise de sensibilidade aos 62 registros com atraso extremo, o aprofundamento da qualidade das classificações e das possíveis duplicidades, a verificação das mudanças históricas de referência populacional e a definição de métodos estatísticos para tendências ou associação espacial. Não foram realizados testes formais de autocorrelação espacial ou identificação de conglomerados.

## 4. Resultados e discussão

### 4.1. Distribuição temporal
A série temporal reuniu **215.251 registros classificados**. Os maiores totais anuais ocorreram em **2016 (41.894)** e **2022 (39.940 na série temporal; 39.938 na agregação municipal)**. Em **2018**, foram observados **3.995 registros**, o menor total entre 2016 e 2024. O total de 2025 foi inferior, mas não deve ser interpretado como queda epidemiológica confirmada sem avaliar a completude dos dados.

A concentração de registros entre **março e junho** correspondeu a aproximadamente **65,5%** da série. Maio apresentou a maior média mensal, de **4.401,8 registros**. Em todos os anos analisados, o mês de maior contagem situou-se entre abril e junho; o maior pico mensal ocorreu em **maio de 2022, com 10.601 registros**.

### 4.2. Distribuição municipal por número absoluto
Os **215.243 registros com município cearense válido** foram distribuídos entre os 184 municípios. Fortaleza apresentou **90.035 registros (41,83%)**, seguida por Brejo Santo (**7.249; 3,37%**) e Caucaia (**6.155; 2,86%**).

![Dez municípios com maiores totais de registros classificados de dengue, 2016–2025](../resultados/graficos/top10_municipios_2016_2025.png)

**Figura — Dez municípios com maiores totais acumulados de registros classificados de dengue no Ceará, 2016–2025. Fonte: elaboração própria a partir de dados do Ministério da Saúde.**

Os números absolutos não permitem comparações proporcionais diretas entre municípios com populações distintas.

### 4.3. Taxas anuais agregadas do Ceará
As taxas estaduais derivadas das agregações municipais foram:

\| Ano | Registros municipais | População utilizada | Taxa por 100 mil |

\|---|---:|---:|---:|

\| 2016 | 41.894 | 8.963.663 | 467,38 |

\| 2017 | 27.055 | 9.020.460 | 299,93 |

\| 2018 | 3.995 | 9.075.649 | 44,02 |

\| 2019 | 15.674 | 9.132.078 | 171,64 |

\| 2020 | 21.451 | 9.187.103 | 233,49 |

\| 2021 | 33.841 | 9.240.580 | 366,22 |

\| 2022 | 39.938 | 8.794.957 | 454,10 |

\| 2023 | 14.220 | 8.794.957 | 161,68 |

\| 2024 | 12.127 | 9.233.656 | 131,33 |

\| 2025 | 5.048 | 9.268.836 | 54,46 |

**Fonte: elaboração própria a partir de registros classificados do Ministério da Saúde e denominadores populacionais do IBGE. Os totais diferem da série temporal em oito registros sem município cearense válido.**

### 4.4. Comparação municipal em 2024
Em 2024, **Brejo Santo** apresentou a maior taxa municipal (**4.425,60 por 100 mil habitantes**), seguido por **Porteiras (2.688,08)**, **Altaneira (2.568,15)** e **Penaforte (2.213,15)**. Dos 184 municípios, **37** tiveram taxas superiores à taxa estadual derivada (**131,33**), e **cinco** não apresentaram registros classificados na base municipal daquele ano.

Fortaleza registrou o maior número absoluto (**3.403**), com taxa de **132,19 por 100 mil habitantes**; Brejo Santo registrou **2.380**, mas sua taxa foi aproximadamente **33,5 vezes** a de Fortaleza. A diferença evidencia a importância de considerar os denominadores populacionais.

![Dez maiores taxas municipais em 2024](../resultados/graficos/top10_taxas_dengue_2024.png)

**Figura — Dez maiores taxas municipais de registros classificados de dengue em 2024. Fonte: elaboração própria a partir de dados do Ministério da Saúde e do IBGE.**

### 4.5. Evolução de Brejo Santo em comparação com o Ceará
Brejo Santo apresentou taxas de **2.877,33** em 2017, **3.491,88** em 2023 e **4.425,60** em 2024, equivalentes, respectivamente, a **9,59**, **21,60** e **33,70 vezes** as taxas estaduais derivadas dos registros municipais. Em oito dos dez anos, sua taxa superou a estadual; as exceções foram 2016 e 2021.

![Comparação das taxas de Brejo Santo e Ceará, 2016–2025](../resultados/graficos/comparativo_brejo_ceara_2016_2025.png)

**Figura — Evolução das taxas anuais de registros classificados de dengue em Brejo Santo e no Ceará, 2016–2025. Fonte: elaboração própria a partir de dados do Ministério da Saúde e do IBGE.**

O contraste é descritivo e não identifica, isoladamente, os fatores responsáveis pelas diferenças. A taxa estadual inclui os registros de Brejo Santo, embora a contribuição desse município ao denominador populacional estadual seja pequena.

### 4.6. Recorrência de taxas acima da estadual
Quatro municípios apresentaram taxas superiores à estadual em **oito dos dez anos**: **Brejo Santo, Quixeré, Tabuleiro do Norte e Fortaleza**. Penaforte, Icapuí, Jaguaribara e Limoeiro do Norte apresentaram essa condição em sete anos.

O mapa de calor dos 15 municípios com maior recorrência revelou picos em anos diferentes: Brejo Santo em 2017, 2023 e 2024; Quixeré em 2019 e 2021; e Aratuba com taxa próxima de 4.196 por 100 mil habitantes em 2022.

![Mapa de calor das taxas de 15 municípios, 2016–2025](../resultados/graficos/heatmap_taxas_municipais.png)

**Figura — Taxas anuais de registros classificados de dengue nos 15 municípios selecionados por maior recorrência acima da taxa estadual, 2016–2025. Fonte: elaboração própria a partir de dados do Ministério da Saúde e do IBGE.**

A recorrência é definida **relativamente à taxa estadual de cada ano**, não significando necessariamente taxas altas em termos absolutos durante todo o período. Os resultados indicam heterogeneidade temporal entre os municípios selecionados, mas não demonstram, sem análise geográfica adicional, a existência de agrupamentos espaciais.

### 4.7. Distribuição espacial das taxas municipais

Os mapas históricos dos 184 municípios, construídos com classes fixas de taxas, mostraram diferenças relevantes entre os anos. Em 2022, 27 municípios apresentaram taxas superiores a 700 registros por 100 mil habitantes, contra apenas dois em 2018. Em 2016 e 2021, foram 22 municípios em cada ano. Em 2024, nove municípios superaram esse patamar, enquanto cinco não apresentaram registros classificados na base. Em 2016, 11 municípios ultrapassaram 1.500 registros por 100 mil habitantes, maior número observado nessa classe durante o período.

![Mapas históricos das taxas municipais, 2016–2025](../resultados/graficos/mapas_historicos_dengue_2016_2025.png)

*Figura — Distribuição municipal das taxas de registros classificados de dengue no Ceará, 2016–2025, em classes descritivas constantes. Malha municipal do IBGE de 2024. Fonte: elaboração própria com dados do Ministério da Saúde e do IBGE.*

### 4.8. Sazonalidade mensal e diferenças regionais

Na série estadual, março a junho concentraram 141.020 dos 215.251 registros (aproximadamente 65,5%); maio apresentou o maior total acumulado (44.018 registros). Os picos anuais estaduais ocorreram entre abril e junho, com máximo de 10.601 registros em maio de 2022.

A análise das 18 Regiões Geográficas Imediatas mostrou diferenças no mês de maior contagem acumulada: uma região teve pico em março, seis em abril, sete em maio e quatro em junho. Icó destacou-se em março; Brejo Santo e Juazeiro do Norte, em abril; Fortaleza, em maio; e Acaraú, Aracati, Russas–Limoeiro do Norte e Sobral, em junho. Ao considerar separadamente as 180 combinações região-ano, 135 (75%) tiveram seu pico entre março e junho. Esses resultados indicam heterogeneidade na distribuição temporal dos registros, sem estabelecer associação causal com fatores climáticos.

![Mapa de calor da sazonalidade regional, 2016–2025](../resultados/graficos/heatmap_sazonalidade_regional.png)

*Figura — Participação percentual dos registros de cada mês no total decenal de cada Região Geográfica Imediata. Fonte: elaboração própria a partir dos registros classificados do Ministério da Saúde e da regionalização do IBGE.*

### 4.9. Investigação de concentração atípica em Pentecoste

O mapa de calor regional apontou participação relativamente elevada de novembro na região de Itapagé (24,6% do total decenal regional). Dos 423 registros de novembro acumulados entre 2016 e 2025 nessa região, 418 ocorreram em 2016 (98,8%). Destes, 417 (99,76%) corresponderam a residentes de Pentecoste e um a General Sampaio. Em Pentecoste, foram identificados 489 registros classificados em 2016, dos quais 417 (85,3%) tiveram início dos sintomas em novembro e 476 (97,3%) entre outubro e dezembro. Os 417 registros de novembro distribuíram-se por 29 datas distintas, sem datas inválidas, e a maior contagem diária foi de 38 registros em 19 de novembro. A variável `CRITERIO` apresentou os códigos 2 (341 registros), 3 (70) e 1 (seis), cuja interpretação deve ser conferida no dicionário da fonte. A concentração é descritiva e, isoladamente, não comprova a ocorrência de surto.

### 4.10. Taxas regionais anuais e recorrência

Em 2024, Brejo Santo apresentou a maior taxa entre as 18 regiões (1.704,39 registros por 100 mil habitantes; 3.292 registros), seguida por Tauá (343,87), Aracati (221,85), Icó (194,39) e Juazeiro do Norte (150,32). Fortaleza apresentou o maior total absoluto regional (4.202 registros), mas taxa de 101,45 por 100 mil habitantes. A menor taxa regional de 2024 foi a de Itapagé (7,27).

No período de 2016 a 2025, a região de Russas–Limoeiro do Norte permaneceu acima da taxa estadual em todos os dez anos (22.933 registros acumulados), seguida por Brejo Santo em oito anos (13.592), Aracati em sete (5.277) e Icó em seis (4.755). Itapipoca, Sobral e Camocim não superaram a taxa estadual em nenhum ano. Brejo Santo liderou o ranking de taxas regionais em 2017, 2022, 2023 e 2024; Russas–Limoeiro do Norte, em 2019 e 2021; Icó, em 2020 e 2025. A maior taxa regional entre os líderes anuais foi registrada em Tauá em 2016 (2.476,75 por 100 mil habitantes). A recorrência indica posição relativa à taxa estadual anual e não deve ser interpretada como medida direta de risco individual.

![Mapa de calor das taxas regionais, 2016–2025](../resultados/graficos/heatmap_taxas_regionais_2016_2025.png)

*Figura — Taxas anuais de registros classificados de dengue por 100 mil habitantes nas 18 Regiões Geográficas Imediatas do Ceará. Fonte: elaboração própria a partir de dados do Ministério da Saúde e do IBGE.*

### 4.11. Limitações dos resultados

Os registros selecionados não equivalem necessariamente a casos únicos ou à incidência oficial; possíveis duplicidades e a interpretação de alguns códigos de classificação ainda requerem investigação. A exclusão operacional dos 62 atrasos extremos pode influenciar os resultados e deve ser avaliada por análise de sensibilidade. A combinação de estimativas populacionais e dados censitários, especialmente o denominador de 2023, exige cautela nas comparações interanuais. A completude de 2025 não foi confirmada. A utilização da malha municipal de 2024 em toda a série requer documentação quanto a eventuais mudanças territoriais. As faixas dos mapas são descritivas e os achados de sazonalidade, recorrência e concentração municipal não demonstram causalidade nem agrupamento espacial estatisticamente significativo.

## 5. Conclusão

A análise dos arquivos históricos de dengue do Ministério da Saúde permitiu descrever padrões temporais e diferenças municipais no Ceará entre 2016 e 2025. Após etapas de seleção e validação, foram utilizados 215.251 registros classificados na série temporal e 215.243 na análise municipal. Os resultados destacaram maiores totais em 2016 e 2022, concentração aproximada de 65,5% dos registros entre março e junho e diferenças expressivas entre municípios quando as contagens foram ajustadas pela população.

Fortaleza concentrou o maior volume absoluto de registros, enquanto Brejo Santo apresentou taxas municipais particularmente elevadas em anos específicos, inclusive em 2024. Esses achados reforçam a utilidade de combinar séries temporais, contagens municipais e indicadores populacionais para descrever a distribuição dos registros de dengue.

A principal contribuição computacional do estudo está na construção de um fluxo documentado de preparação, validação, integração e visualização de dados públicos. As conclusões são descritivas e condicionadas à qualidade e à completude dos arquivos, às decisões operacionais de seleção e à natureza dos denominadores populacionais. Trabalhos futuros podem avaliar a sensibilidade dos filtros temporais, aprofundar a verificação das classificações e duplicidades e aplicar métodos formais de análise espacial, desde que adequadamente justificados.

A incorporação de mapas coropléticos e de agregações pelas 18 Regiões Geográficas Imediatas ampliou a descrição das diferenças territoriais. Na análise regional, 75% das combinações região-ano apresentaram maior contagem mensal entre março e junho, enquanto Russas–Limoeiro do Norte permaneceu acima da taxa estadual em todos os anos estudados. Esses achados são exploratórios e não constituem evidência de causalidade, surtos específicos ou dependência espacial estatisticamente demonstrada. A investigação descritiva da concentração de registros em Pentecoste em novembro de 2016 requer cautela adicional quanto à interpretação dos critérios de classificação.

## Referências (revisar e padronizar antes da submissão)

ARAÚJO, José Raimundo de; FERREIRA, Efigênia Ferreira e; ABREU, Mauro Henrique Nogueira Guimarães de. Revisão sistemática sobre estudos de espacialização da dengue no Brasil. **Revista Brasileira de Epidemiologia**, v. 11, n. 4, p. 696–708, 2008. Disponível em: https://doi.org/10.1590/S1415-790X2008000400016. Acesso em: 12 nov. 2026.

BRASIL. Ministério da Saúde. **Dengue: diagnóstico e manejo clínico: adulto e criança**. 6. ed. Brasília, DF: Ministério da Saúde, 2024. Disponível em: https://bvsms.saude.gov.br/bvs/publicacoes/dengue_diagnostico_manejo_clinico_6ed.pdf. Acesso em: 12 nov. 2026.

BRASIL. Ministério da Saúde. **Guia de vigilância em saúde: volume 2**. 6. ed. rev. Brasília, DF: Ministério da Saúde, [s. d.]. Disponível em: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/vigilancia/guia-de-vigilancia-em-saude-volume-2-6a-edicao/view. Acesso em: 12 nov. 2026.

BRASIL. Ministério da Saúde. **Portal de Dados Abertos: arboviroses — dengue**. Brasília, DF: Ministério da Saúde, [s. d.]. Disponível em: https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue. Acesso em: 12 nov. 2026.

HUNTER, John D. Matplotlib: a 2D graphics environment. **Computing in Science & Engineering**, v. 9, n. 3, p. 90–95, 2007. Disponível em: https://doi.org/10.1109/MCSE.2007.55. Acesso em: 12 nov. 2026.

INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). **Censo Demográfico 2022: tabela 4714 — população residente, área territorial e densidade demográfica**. Rio de Janeiro: IBGE, [s. d.]. Disponível em: https://sidra.ibge.gov.br/tabela/4714. Acesso em: 12 nov. 2026.

INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). **Divisão regional do Brasil em regiões geográficas imediatas e regiões geográficas intermediárias: 2017**. Rio de Janeiro: IBGE, 2017. Disponível em: https://biblioteca.ibge.gov.br/visualizacao/livros/liv100600.pdf. Acesso em: 12 nov. 2026.

JORDAHL, Kelsey et al. **geopandas/geopandas: v0.8.1**. Zenodo, 2020. Software. Disponível em: https://doi.org/10.5281/zenodo.3946761. Acesso em: 12 nov. 2026.

MAGALHÃES, Gledson Bezerra; ZANELLA, Maria Elisa. Comportamento espacial da dengue e sua relação com o clima na Região Metropolitana de Fortaleza. **Revista Brasileira de Climatologia**, v. 12, n. 1, 2013. Disponível em: https://doi.org/10.5380/abclima.v12i1.32180. Acesso em: 12 nov. 2026.

MCKINNEY, Wes. Data structures for statistical computing in Python. In: **PROCEEDINGS OF THE 9TH PYTHON IN SCIENCE CONFERENCE**, 2010. Anais [...]. 2010. Disponível em: https://doi.org/10.25080/Majora-92bf1922-00a. Acesso em: 12 nov. 2026.

ORGANIZAÇÃO MUNDIAL DA SAÚDE (OMS). **Dengue**. Genebra: OMS, 2025. Disponível em: https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue. Acesso em: 12 nov. 2026.

SILVA, Ellen Tayanne Carla da et al. Análise espacial da distribuição dos casos de dengue e sua relação com fatores socioambientais no estado da Paraíba, Brasil, 2007–2016. **Saúde em Debate**, v. 44, n. 125, 2020. Disponível em: https://doi.org/10.1590/0103-1104202012514. Acesso em: 12 nov. 2026.
