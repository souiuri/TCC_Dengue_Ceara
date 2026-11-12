# Análise Temporal e Espacial da Dengue no Ceará entre 2016 e 2025 com Técnicas de Aprendizado de Máquina

**Trabalho de Conclusão de Curso (TCC) — Ciência da Computação**  
**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE), Campus Maracanaú  
**Orientador:** Prof. Fabio Jose Gomes de Sousa  
**Status:** pesquisa em desenvolvimento; etapa de aprendizado de máquina ainda não implementada.

## Sobre o projeto

Este repositório reúne scripts, procedimentos e resultados de uma investigação **quantitativa, retrospectiva, observacional e descritiva** da distribuição temporal e espacial dos registros classificados como dengue no Ceará, entre 2016 e 2025.

O estudo utiliza dados públicos do Ministério da Saúde, informações populacionais e malhas geográficas do Instituto Brasileiro de Geografia e Estatística (IBGE). A análise computacional é realizada em Python. Como próxima etapa, está prevista a aplicação de técnicas de **aprendizado de máquina não supervisionado** para investigar semelhanças entre os padrões históricos dos municípios.

> **Nota metodológica:** as taxas apresentadas neste projeto representam **registros classificados como dengue por 100 mil habitantes, calculados a partir da base selecionada**. Elas não devem ser interpretadas automaticamente como taxas oficiais de incidência ou como contagens de episódios únicos.

## Objetivos

**Objetivo geral:** analisar a evolução temporal e a distribuição espacial dos registros classificados como dengue no Ceará de 2016 a 2025 e explorar técnicas de aprendizado de máquina para identificar padrões entre municípios.

**Objetivos específicos:**

- Preparar, filtrar e validar registros históricos públicos de dengue.
- Construir séries anuais e mensais por data de início dos sintomas.
- Integrar registros municipais, populações históricas e limites geográficos do IBGE.
- Calcular e comparar taxas por 100 mil habitantes nos 184 municípios e nas 18 Regiões Geográficas Imediatas.
- Examinar sazonalidade, heterogeneidade espacial e recorrência de taxas superiores à referência estadual.
- **Etapa planejada:** aplicar e avaliar agrupamento não supervisionado de municípios (K-Means), sem pressupor antecipadamente a quantidade ou o significado dos grupos.

## Fontes de dados

| Fonte | Utilização |
|---|---|
| Ministério da Saúde — arquivos `DENGBR16.csv` a `DENGBR25.csv` | Registros históricos de dengue |
| IBGE — estimativas municipais de 2016–2021 e 2024–2025 | Denominadores populacionais |
| IBGE — Censo Demográfico 2022, SIDRA tabela 4714 | População municipal em 2022 |
| IBGE — publicação populacional baseada no Censo 2022, malha 2023 | Denominadores utilizados para 2023 |
| IBGE — malhas municipais e divisão em Regiões Geográficas Imediatas | Mapas e agregações regionais |

O denominador populacional utilizado para 2023 é baseado no Censo 2022 e **não constitui uma estimativa independente de 2023**.

## Metodologia e tratamento dos dados

1. Seleção inicial de registros dos arquivos nacionais com `SG_UF = 23` (Ceará): **416.095 linhas**.
2. Seleção das classificações finais `CLASSI_FIN` **10, 11 e 12**, com delimitação pela data de início dos sintomas (`DT_SIN_PRI`) ao período de 2016 a 2025.
3. Formação de base analítica com **215.313 registros**.
4. Sinalização e exclusão **das agregações** de 62 registros com intervalo entre sintomas e notificação superior a 365 dias: **215.251 registros** para análise temporal estadual.
5. Exclusão de oito registros sem município de residência válido no Ceará **somente das agregações municipais e regionais**: **215.243 registros** nessas análises.
6. Integração com as populações dos **184 municípios** nos dez anos, totalizando **1.840 pares município–ano**.
7. Cálculo de taxas anuais, agregações regionais, mapas temáticos e análises mensais.

A taxa é calculada por:

\[
\text{Taxa por 100 mil} = \frac{\text{Registros classificados}}{\text{População utilizada}} \times 100.000
\]

As taxas estaduais e regionais são calculadas pela **razão entre a soma dos registros e a soma das populações**, não pela média simples das taxas municipais.

## Principais resultados obtidos

- **215.251** registros na série temporal estadual; **215.243** nas análises municipais e regionais.
- Aproximadamente **65,5%** dos registros da série temporal concentraram-se entre **março e junho**; **maio** teve o maior total acumulado (**44.018 registros**).
- Em **2024**, Brejo Santo apresentou taxa municipal de **4.425,60 registros por 100 mil habitantes**, enquanto Fortaleza concentrou o maior número absoluto municipal (**3.403 registros**).
- Em **2024**, a Região Geográfica Imediata de Brejo Santo apresentou taxa de **1.704,39 por 100 mil habitantes**.
- A região de **Russas–Limoeiro do Norte** apresentou taxa superior à estadual em **10 dos 10 anos**; Brejo Santo, em **8 anos**; Aracati, em **7 anos**.
- A análise mensal regional abrangeu **18 regiões × 10 anos × 12 meses = 2.160 combinações**.
- Os mapas históricos utilizam classes descritivas fixas para permitir comparação entre anos; **não** são faixas oficiais de risco epidemiológico.

Esses resultados são **descritivos** e não demonstram, por si só, causalidade, surtos confirmados ou agrupamentos espaciais estatisticamente significativos.

## Estrutura do repositório

```text
TCC_Dengue_Ceara/
├── artigo/
│   ├── rascunho.md
│   └── diario_pesquisa.md
├── dados/
│   ├── originais/             # Arquivos brutos, quando disponíveis localmente
│   ├── processados/           # Bases derivadas e população histórica
│   └── geograficos/           # Malhas do IBGE
├── resultados/
│   ├── graficos/              # Figuras, mapas e mapas de calor
│   └── *.csv                  # Agregações e indicadores
├── scripts/                  # Scripts de preparação, análise e visualização
├── .gitignore
└── README.md
```

A presença dos arquivos de dados brutos no GitHub depende das regras de versionamento e do `.gitignore`; os arquivos volumosos podem precisar ser obtidos diretamente nas fontes oficiais.

## Scripts e produtos principais

| Script | Produto / finalidade |
|---|---|
| `calcular_taxas_municipais_historicas.py` | `resultados/taxas_dengue_municipios_2016_2025.csv` |
| `analisar_dengue_mensal.py` | `resultados/dengue_mensal_2016_2025.csv` |
| `analisar_dengue_mensal_regional.py` | `resultados/dengue_mensal_regional_2016_2025.csv` |
| `calcular_taxas_regionais.py` | `resultados/taxas_dengue_regionais_2016_2025.csv` |
| `analisar_recorrencia_regional.py` | `resultados/recorrencia_regional_2016_2025.csv` |
| `mapa_taxas_dengue_2024_classes.py` | Mapa municipal de 2024 em classes descritivas |
| `mapas_historicos_dengue.py` | Painel cartográfico de 2016 a 2025 |
| `heatmap_taxas_regionais.py` | Mapa de calor das taxas regionais |
| `heatmap_sazonalidade_regional.py` | Mapa de calor da sazonalidade regional |

Os scripts devem ser executados **a partir da raiz do projeto** e na ordem correspondente às dependências dos dados. A tabela documenta os scripts já desenvolvidos; não é uma rotina única de execução automatizada.

## Ambiente e ferramentas

- Python 3 e bibliotecas `pandas`, `matplotlib`, `seaborn` e `geopandas`.
- VS Code para desenvolvimento e Git/GitHub para controle de versões.
- **Previsto para a próxima etapa:** `scikit-learn` para aprendizado de máquina.

As versões exatas das dependências e um ambiente reproduzível (`requirements.txt`) ainda precisam ser consolidados.

## Próxima etapa: aprendizado de máquina

Está planejado um experimento com **K-Means** sobre os perfis históricos de taxas municipais. Antes da interpretação dos grupos, serão definidos o tratamento de escalas e valores extremos, o conjunto de variáveis e os critérios de escolha do número de agrupamentos. A avaliação deverá incluir medidas como o **coeficiente de silhueta**, análise de estabilidade e interpretação dos perfis encontrados.

**Nenhum resultado de agrupamento ou desempenho de IA é apresentado como concluído nesta versão.** A inclusão de aprendizado de máquina no título reflete uma etapa prevista do TCC.

## Limitações

- A seleção de registros classificados não garante equivalência a casos únicos nem à incidência oficial.
- O limite de 365 dias para atraso de notificação é operacional; recomenda-se análise de sensibilidade.
- A completude dos dados de **2025** ainda precisa ser verificada.
- Os denominadores populacionais combinam estimativas e dados censitários; a referência de 2023 exige cautela especial.
- A malha municipal de 2024 foi utilizada como referência cartográfica para a série histórica.
- A análise espacial realizada até o momento é descritiva; não foram aplicados testes formais de autocorrelação espacial.
- Não foram incorporadas variáveis meteorológicas, portanto não se atribuem os padrões mensais observados diretamente à chuva ou à temperatura.

## Referências e documentação

- [Ministério da Saúde — Portal de Dados Abertos](https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue)
- [IBGE — SIDRA, tabela 4714](https://sidra.ibge.gov.br/tabela/4714)
- [IBGE — Divisão Regional do Brasil (2017)](https://biblioteca.ibge.gov.br/visualizacao/livros/liv100600.pdf)

A metodologia detalhada, os resultados científicos e as referências bibliográficas estão sendo consolidados em `artigo/rascunho.md`. O histórico das decisões e validações da pesquisa está em `artigo/diario_pesquisa.md`.

---

**Projeto acadêmico em desenvolvimento.** Os resultados podem ser atualizados após novas verificações, análises de sensibilidade e a implementação do experimento de aprendizado de máquina.
