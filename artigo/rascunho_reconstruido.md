# Análise Temporal e Espacial da Dengue no Estado do Ceará entre 2016 e 2025 Utilizando Análise de Dados

**Autor:** Victor Iuri Costa Sousa — victor.iuri.costa60@aluno.ifce.edu.br  
**Orientador:** Prof. Fabio Jose Gomes de Sousa — fabio.jose@ifce.edu.br  
**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE), Campus Maracanaú  
**Curso:** Ciência da Computação  
**Situação:** versão reconstruída para revisão do orientador, 18 de novembro de 2026.

> **Nota editorial (remover da versão submetida):** Texto reconstruído com base no diário de pesquisa revisado e no rascunho revisado disponíveis na conversa. Não houve inspeção direta, nesta etapa, de todos os scripts, CSVs e gráficos da pasta local do projeto. As análises geográficas regionais mencionadas em conversas anteriores não foram incorporadas como resultados quantitativos porque não constam do diário examinado. Os pontos marcados **[VERIFICAR]** precisam de conferência antes da submissão definitiva. As referências abaixo são uma lista de fontes documentadas no projeto, não uma bibliografia ABNT concluída.

## Resumo

A dengue constitui um desafio para a vigilância em saúde, e a análise de bases públicas permite examinar a distribuição de seus registros ao longo do tempo e entre localidades. Este trabalho teve como objetivo caracterizar a evolução temporal e a distribuição municipal de registros classificados como dengue no Ceará entre 2016 e 2025. Realizou-se estudo quantitativo, retrospectivo e descritivo, com dez arquivos históricos do Ministério da Saúde e dados populacionais do Instituto Brasileiro de Geografia e Estatística. Os dados foram preparados e analisados em Python, com filtragem geográfica, avaliação de classificações e datas, agregações anuais e mensais e cálculo de taxas por 100 mil habitantes. A filtragem inicial reuniu 416.095 registros. Após seleção das classificações de dengue, delimitação temporal e aplicação do critério operacional para atrasos extremos, 215.251 registros integraram a série temporal; 215.243 possuíam município cearense válido para a análise municipal. Os maiores totais anuais ocorreram em 2016 (41.894) e 2022 (39.940). Aproximadamente 65,5% dos registros concentraram-se entre março e junho. Fortaleza apresentou o maior volume acumulado municipal, com 90.035 registros. Em 2024, Brejo Santo registrou taxa de 4.425,60 por 100 mil habitantes, superior à de Fortaleza, de 132,19, evidenciando diferenças entre rankings absolutos e indicadores padronizados pela população. Os resultados indicam marcada variabilidade temporal e heterogeneidade municipal, mas não permitem inferir causalidade nem devem ser equiparados automaticamente à incidência oficial ou a casos únicos. O estudo demonstra a utilidade da preparação e visualização de dados públicos para descrever padrões relevantes à vigilância epidemiológica.

**Palavras-chave:** Dengue; Análise de dados; Séries temporais; Distribuição espacial; Vigilância epidemiológica.

## 1. Introdução

A dengue é um problema relevante para a saúde pública brasileira. O acompanhamento de sua ocorrência exige informações sobre a evolução dos registros ao longo do tempo e sobre diferenças entre localidades. A disponibilidade de dados públicos de vigilância epidemiológica cria oportunidades para estudos computacionais de caráter descritivo, especialmente quando são aplicados procedimentos documentados de preparação, validação e visualização.

O uso direto de contagens extraídas de arquivos administrativos, entretanto, requer cautela. A quantidade de linhas de uma base não corresponde necessariamente ao número de pessoas acometidas, e diferentes campos podem representar notificações, classificações finais e critérios de investigação. Também é necessário distinguir o ano do arquivo de origem do ano efetivo de início dos sintomas e avaliar a compatibilidade entre códigos municipais e denominadores populacionais.

Este trabalho investiga os registros classificados como dengue no Ceará entre 2016 e 2025, utilizando arquivos públicos do Ministério da Saúde e informações populacionais do IBGE. O recorte de dez anos permite comparar oscilações anuais, concentração sazonal e diferenças entre os 184 municípios cearenses. A pesquisa se concentra em análises descritivas e exploratórias, sem pretender estabelecer relações causais entre os padrões observados e fatores ambientais, sociais ou assistenciais.

### 1.1. Objetivo geral

Analisar a evolução temporal e a distribuição espacial municipal dos registros classificados como dengue no estado do Ceará entre 2016 e 2025, utilizando técnicas computacionais de preparação, validação, agregação e visualização de dados.

### 1.2. Objetivos específicos

- Organizar e processar dez arquivos históricos de dengue disponibilizados pelo Ministério da Saúde.
- Examinar classificações, datas e possíveis coincidências de atributos, explicitando as limitações de qualidade.
- Construir séries anuais e mensais com base na data de início dos sintomas.
- Avaliar a sazonalidade e as oscilações interanuais dos registros selecionados.
- Validar os códigos de residência dos municípios cearenses e consolidar as populações municipais.
- Calcular e comparar taxas de registros classificados por 100 mil habitantes.
- Identificar municípios com maiores totais, maiores taxas e recorrência de taxas superiores à estadual.

## 2. Fundamentação teórica

### 2.1. Dengue e informação em saúde

A análise da dengue pode utilizar dados produzidos pela vigilância epidemiológica. Esses registros são valiosos para descrever a distribuição de notificações e classificações, mas sua interpretação depende do significado das variáveis e dos procedimentos de coleta e atualização. Nesta pesquisa, a variável `CLASSI_FIN` é central para a seleção dos registros classificados como dengue, enquanto `CRITERIO` é considerada na avaliação da consistência da classificação. A interpretação dos códigos foi apoiada no Dicionário de Dados do SINAN Online e na Nota Informativa nº 59/2016 do Ministério da Saúde. **[VERIFICAR referências completas e a correspondência dos códigos com as versões dos arquivos analisados.]**

### 2.2. Análise temporal e sazonalidade

Séries temporais permitem organizar observações segundo uma referência cronológica. Para a descrição da ocorrência de dengue, a data de início dos sintomas e a data de notificação podem conduzir a distribuições distintas, pois a notificação pode acontecer posteriormente. Neste estudo, a data de início dos sintomas foi escolhida como referência principal, e o intervalo até a notificação foi utilizado como indicador operacional de qualidade temporal. A comparação mensal permite examinar concentração sazonal sem, por si só, demonstrar as causas dessa concentração.

### 2.3. Distribuição municipal e padronização populacional

Contagens absolutas refletem tanto a quantidade de registros quanto o tamanho da população e outras características da cobertura dos dados. Para comparar municípios com populações diferentes, este estudo calcula taxas de registros classificados por 100 mil habitantes. Tais taxas são indicadores derivados da base analisada, não equivalentes automaticamente à incidência epidemiológica oficial. A comparação espacial apresentada é descritiva; rankings e mapas de calor temporais não constituem testes formais de autocorrelação espacial.

### 2.4. Análise de dados e reprodutibilidade

A pesquisa utiliza Python e bibliotecas de manipulação e visualização de dados para executar filtros, agregações e verificações reproduzíveis. A separação entre arquivos originais, dados processados, scripts e resultados favorece a rastreabilidade das transformações. As análises são exploratórias e devem ser interpretadas em conjunto com suas limitações de origem, classificação e completude.

> **Pendência bibliográfica:** esta fundamentação apresenta os conceitos empregados na pesquisa, mas ainda precisa de citações científicas verificadas e inseridas no formato exigido pelo IFCE. Não foram inventadas referências ou citações autor-data.

## 3. Metodologia

### 3.1. Delineamento

Trata-se de estudo quantitativo, observacional, retrospectivo e descritivo, baseado em dados secundários públicos. O processamento foi realizado em Python, com preservação dos arquivos originais e execução de scripts para preparação, verificação, agregação e visualização. Não foram aplicados testes de inferência causal nem testes formais de agrupamento espacial nesta versão.

### 3.2. Fontes, recorte e variáveis

Foram utilizados dez arquivos históricos do conjunto de arboviroses/dengue do Ministério da Saúde, de `DENGBR16.csv` a `DENGBR25.csv`. A filtragem inicial selecionou `SG_UF = 23`, correspondente ao Ceará, totalizando 416.095 linhas. O ano indicado no nome de cada arquivo não foi assumido como o ano de início dos sintomas.

O processamento preservou as variáveis `ID_AGRAVO`, `DT_NOTIFIC`, `NU_ANO`, `DT_SIN_PRI`, `SG_UF`, `ID_MN_RESI`, `CLASSI_FIN` e `CRITERIO`. Os arquivos extensos foram lidos em blocos de até 100.000 linhas com pandas.

Para o denominador populacional, foram utilizadas estimativas municipais do IBGE de 2016 a 2021 e de 2024 a 2025, o Censo Demográfico 2022 (SIDRA, tabela 4714) e, para 2023, valores derivados do Censo 2022 com referência territorial de 2023. O dado adotado para 2023 não representa uma estimativa populacional independente daquele ano.

### 3.3. Critérios de seleção e qualidade temporal

A seleção considerou `CLASSI_FIN` igual a 10 (dengue), 11 (dengue com sinais de alarme) ou 12 (dengue grave), resultando em 215.748 registros antes da delimitação temporal. O significado de outros códigos encontrados e a interpretação de alguns valores de `CRITERIO` permanecem limitações documentadas.

A delimitação por `DT_SIN_PRI` ao intervalo de 2016 a 2025 resultou em 215.313 registros, diferença de 435 em relação à seleção por classificação. **[VERIFICAR]** A composição exata desses 435 registros, inclusive quanto a datas ausentes ou inválidas, não foi completamente decomposta no diário.

Foi calculado o intervalo entre `DT_NOTIFIC` e `DT_SIN_PRI`. Entre os 215.313 registros, 211.881 apresentaram intervalo de 0 a 30 dias, 3.370 de 31 a 365 dias e 62 superior a 365 dias. Os 62 foram sinalizados e preservados na base, mas excluídos das agregações temporais aqui apresentadas, por critério operacional. A exclusão não significa comprovação de erro. A série temporal final contém 215.251 registros.

Na investigação de coincidências entre atributos, foram encontrados agrupamentos de registros com campos iguais; entretanto, não foi possível confirmar que correspondiam a uma mesma pessoa ou episódio. Não se realizou exclusão automática por suposta duplicidade.

### 3.4. Agregação temporal

Os 215.251 registros foram agrupados por ano e mês de início dos sintomas, compondo 120 observações mensais entre janeiro de 2016 e dezembro de 2025. Foram examinados totais anuais, médias por mês do calendário, concentração entre meses e picos da série. A completude dos dados de 2025 não foi demonstrada.

### 3.5. Validação municipal e integração populacional

A variável `ID_MN_RESI` foi validada contra os códigos dos 184 municípios cearenses. Dos 215.251 registros da série estadual, seis não apresentaram código municipal e dois continham códigos associados a outros estados. Assim, 215.243 registros foram utilizados nas agregações municipais. Os oito registros não foram removidos da série estadual, pois satisfaziam o filtro original `SG_UF = 23`.

Os dados populacionais foram integrados aos totais por município e ano, formando 1.840 pares município-ano (184 municípios em dez anos), sem populações ausentes após a junção. Os códigos municipais de seis dígitos foram compatibilizados com os códigos IBGE de sete dígitos.

A taxa anual de registros classificados foi calculada por:

\[
T_{m,a}=\frac{R_{m,a}}{P_{m,a}}\times100.000,
\]

em que \(R_{m,a}\) representa os registros selecionados do município \(m\) no ano \(a\), e \(P_{m,a}\), a população utilizada. A taxa estadual foi calculada dividindo-se a soma dos registros municipais pela soma das populações, e não pela média simples das taxas municipais.

### 3.6. Comparações exploratórias

Foram examinados os maiores totais municipais no período, as maiores taxas em 2024, a trajetória de Brejo Santo em comparação com a taxa estadual e a recorrência de municípios com taxas acima da taxa estadual anual. Um mapa de calor reuniu os 15 municípios selecionados por maior recorrência. A seleção é exploratória e não permite concluir a existência de agrupamentos espaciais estatisticamente significativos.

## 4. Resultados e discussão

### 4.1. Fluxo de seleção e consistência dos registros

A filtragem inicial dos dez arquivos históricos produziu 416.095 registros com `SG_UF = 23`. A seleção de `CLASSI_FIN` 10, 11 ou 12 produziu 215.748 registros. A delimitação por início dos sintomas reduziu esse total a 215.313; após exclusão operacional dos 62 intervalos extremos, 215.251 compuseram a análise temporal. A validação do município de residência resultou em 215.243 registros para a análise municipal. Esses totais descrevem etapas diferentes e não devem ser apresentados como quantidades intercambiáveis de casos confirmados.

### 4.2. Evolução anual e sazonalidade

A distribuição anual da série temporal estadual foi:

| Ano | Registros na série temporal |
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

Os maiores totais ocorreram em 2016 e 2022. O ano de 2018 apresentou o menor total entre 2016 e 2024, com 3.995 registros. O total de 2025 foi inferior, mas não deve ser interpretado como redução epidemiológica confirmada sem avaliação da completude do arquivo.

Aproximadamente 65,5% dos registros concentraram-se entre março e junho. Maio apresentou a maior média mensal (4.401,8), seguido por abril (3.933,0) e junho (3.362,9). Em todos os anos, o mês de maior contagem ocorreu entre abril e junho. O maior pico mensal da série foi observado em maio de 2022, com 10.601 registros.

**Figuras previstas para inserção:** `resultados/graficos/serie_mensal_2016_2025.png` e `resultados/graficos/mapa_calor_2016_2025.png`. Fonte: elaboração própria com dados do Ministério da Saúde.

### 4.3. Distribuição municipal dos totais acumulados

Os 215.243 registros com município de residência válido foram distribuídos entre os 184 municípios. Fortaleza apresentou o maior total acumulado, com 90.035 registros (41,83%), seguida por Brejo Santo, com 7.249 (3,37%), e Caucaia, com 6.155 (2,86%). As diferenças de população impedem comparar diretamente esses números como indicadores de ocorrência proporcional.

**Figura prevista:** `resultados/graficos/top10_municipios_2016_2025.png`. Fonte: elaboração própria com dados do Ministério da Saúde.

### 4.4. Taxas estaduais derivadas da agregação municipal

| Ano | Registros com município válido | População utilizada | Taxa por 100 mil habitantes |
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

*Fonte: elaboração própria com registros classificados do Ministério da Saúde e dados populacionais do IBGE.*

As diferenças entre os numeradores desta tabela e os totais da série temporal em 2021, 2022, 2024 e 2025 decorrem dos oito registros sem município cearense válido. A comparação entre 2022 e 2023 requer atenção adicional: o denominador de 2023 foi derivado de dados censitários de 2022. O diário registra diferenças de 227 habitantes entre Ereré e Pereiro nos arquivos de 2022 e 2023, com total estadual idêntico, sem confirmação da causa.

### 4.5. Comparação municipal em 2024

Em 2024, Brejo Santo apresentou a maior taxa municipal, de 4.425,60 registros classificados por 100 mil habitantes, seguido por Porteiras (2.688,08), Altaneira (2.568,15) e Penaforte (2.213,15). Dos 184 municípios, 37 tiveram taxas superiores à taxa estadual calculada de 131,33; cinco não apresentaram registros classificados no conjunto analisado para o ano.

Fortaleza reuniu 3.403 registros, com taxa de 132,19 por 100 mil habitantes, enquanto Brejo Santo apresentou 2.380 registros e taxa de 4.425,60. Assim, a taxa de Brejo Santo foi aproximadamente 33,5 vezes a de Fortaleza, apesar de seu número absoluto ser menor. A comparação demonstra a importância do denominador populacional, mas não identifica os fatores associados às diferenças.

**Figura prevista:** `resultados/graficos/top10_taxas_dengue_2024.png`. Fonte: elaboração própria com dados do Ministério da Saúde e do IBGE.

### 4.6. Evolução de Brejo Santo e recorrência municipal

Na comparação com a taxa estadual, Brejo Santo apresentou 2.877,33 registros por 100 mil habitantes em 2017 (9,59 vezes a taxa estadual), 3.491,88 em 2023 (21,60 vezes) e 4.425,60 em 2024 (33,70 vezes). Em oito dos dez anos, sua taxa foi superior à estadual; as exceções ocorreram em 2016 e 2021.

Quatro municípios apresentaram taxas superiores à estadual em oito dos dez anos: Brejo Santo, Quixeré, Tabuleiro do Norte e Fortaleza. Penaforte, Icapuí, Jaguaribara e Limoeiro do Norte apresentaram essa condição em sete anos. O mapa de calor dos 15 municípios selecionados evidenciou picos em períodos distintos, incluindo Brejo Santo em 2017, 2023 e 2024 e Quixeré em 2019 e 2021. A recorrência indica comparação relativa à taxa estadual de cada ano, não necessariamente taxas absolutas elevadas durante todo o período.

**Figuras previstas:** `resultados/graficos/comparativo_brejo_ceara_2016_2025.png` e `resultados/graficos/heatmap_taxas_municipais.png`. Fonte: elaboração própria com dados do Ministério da Saúde e do IBGE.

### 4.7. Discussão e limitações

Os resultados revelam oscilações interanuais, concentração de registros em determinados meses e heterogeneidade municipal. A interpretação desses padrões, entretanto, depende das características das bases utilizadas. Em primeiro lugar, os registros selecionados não foram identificados como episódios individuais únicos; a pesquisa encontrou coincidências de atributos sem condições de comprovar duplicidades. Em segundo lugar, os critérios de classificação e sua consistência ao longo do período requerem investigação complementar, sobretudo para códigos não esclarecidos e registros com `CRITERIO = 3`.

A exclusão dos 62 intervalos superiores a 365 dias foi operacional e pode influenciar as contagens; uma análise de sensibilidade ainda é recomendada. A referência populacional de 2023 não corresponde a uma estimativa independente, e a transição entre estimativas e censo exige cautela em comparações anuais. A completude de 2025 não foi confirmada. Finalmente, os rankings, comparações de taxas e mapa de calor constituem análises descritivas: não comprovam causas, risco individual ou agrupamentos espaciais estatisticamente significativos.

A discussão com literatura científica sobre vigilância epidemiológica, sazonalidade e distribuição territorial permanece pendente de inclusão de citações verificadas. **[VERIFICAR]** Antes da entrega final, conferir a versão dos scripts e os gráficos correspondentes aos valores apresentados.

## 5. Conclusão

A análise dos arquivos históricos de dengue do Ministério da Saúde permitiu descrever padrões temporais e diferenças municipais no Ceará entre 2016 e 2025. Após etapas de seleção e validação, foram utilizados 215.251 registros classificados na série temporal e 215.243 na análise municipal. Os resultados destacaram maiores totais em 2016 e 2022, concentração aproximada de 65,5% dos registros entre março e junho e diferenças expressivas entre municípios quando as contagens foram ajustadas pela população.

Fortaleza concentrou o maior volume absoluto de registros, enquanto Brejo Santo apresentou taxas municipais particularmente elevadas em anos específicos, inclusive em 2024. Esses achados reforçam a utilidade de combinar séries temporais, contagens municipais e indicadores populacionais para descrever a distribuição dos registros de dengue.

A principal contribuição computacional do estudo está na construção de um fluxo documentado de preparação, validação, integração e visualização de dados públicos. As conclusões são descritivas e condicionadas à qualidade e à completude dos arquivos, às decisões operacionais de seleção e à natureza dos denominadores populacionais. Trabalhos futuros podem avaliar a sensibilidade dos filtros temporais, aprofundar a verificação das classificações e duplicidades e aplicar métodos formais de análise espacial, desde que adequadamente justificados.

## Referências — fontes documentadas, a completar e normalizar

- BRASIL. Ministério da Saúde. **Portal de Dados Abertos: Arboviroses — Dengue**. Disponível em: https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue. **[Completar data de acesso.]**
- BRASIL. Ministério da Saúde. **Dicionário de Dados do SINAN Online**, versão 3.0, revisado em 2015. **[Verificar dados bibliográficos completos.]**
- BRASIL. Ministério da Saúde. **Nota Informativa nº 59/2016 — CGPNCD/DEVIT/SVS/MS**. **[Verificar dados bibliográficos completos.]**
- INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). **Censo Demográfico 2022, SIDRA, tabela 4714**. **[Completar referência e acesso.]**
- INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). **Estimativas municipais de população, 2016–2021 e 2024–2025; publicação com referência territorial de 2023**. **[Identificar e referenciar cada publicação.]**
- PANDAS. **Documentação oficial**. Disponível em: https://pandas.pydata.org/docs/. **[Completar acesso, caso citada no texto.]**
- MATPLOTLIB. **Documentação oficial**. Disponível em: https://matplotlib.org/stable/. **[Completar acesso, caso citada no texto.]**

## Lista de verificações antes do envio definitivo

- [ ] Confirmar os 435 registros excluídos na delimitação temporal, discriminando datas ausentes, inválidas ou fora do período.
- [ ] Conferir as tabelas e os gráficos diretamente nos arquivos gerados pelos scripts atuais.
- [ ] Revisar a completude de 2025 e o significado dos códigos de classificação ainda não esclarecidos.
- [ ] Verificar a adequação do critério de exclusão dos 62 atrasos extremos e explicitar a limitação.
- [ ] Completar e conferir referências bibliográficas e citações no corpo do artigo.
- [ ] Integrar resultados de mapas geográficos e análises regionais somente após conferência dos scripts, CSVs e figuras correspondentes.
- [ ] Ajustar a estrutura ao modelo LaTeX oficial do IFCE e gerar PDF para revisão do orientador.
