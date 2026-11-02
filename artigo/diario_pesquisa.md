# Diário de Pesquisa — TCC Dengue Ceará

**Projeto:** Análise temporal e espacial dos registros de dengue no Ceará entre 2016 e 2025 utilizando Python

**Curso:** Ciência da Computação — IFCE, Campus Maracanaú

**Situação:** Pesquisa em desenvolvimento

---

## 1. Objetivo da pesquisa

Investigar a distribuição temporal e espacial dos registros de dengue no estado do Ceará entre 2016 e 2025, considerando notificações e casos confirmados.

Ao final da pesquisa, pretende-se aplicar técnicas de análise de séries temporais para identificar tendências, variações anuais e padrões sazonais da dengue no estado.

## 2. Fonte dos dados

Foram obtidos dados públicos disponibilizados pelo Ministério da Saúde, por meio do Portal de Dados Abertos, no conjunto referente à dengue.

**Fonte:** https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue

Foram utilizados dez arquivos históricos, identificados de `DENGBR16.csv` a `DENGBR25.csv`.

As bases originais são preservadas localmente na pasta `dados/originais/`, sem inclusão no repositório GitHub.

## 3. Ambiente de desenvolvimento

O processamento dos dados está sendo desenvolvido em Python, com utilização da biblioteca pandas.

Ferramentas utilizadas:

- Python
- pandas
- Matplotlib
- Visual Studio Code
- Git e GitHub

O processamento de arquivos grandes utiliza leitura em blocos (`chunksize=100_000`), reduzindo a necessidade de carregar toda a base na memória.

## 4. Preparação dos dados

Foi desenvolvido o script `scripts/preparar_base_historica.py`, responsável por percorrer os dez arquivos históricos e selecionar os registros referentes ao Ceará.

O filtro utiliza a coluna `SG_UF`, considerando o código `23`.

Os arquivos resultantes são armazenados em `dados/processados/`, com nomes como `DENGBR16_CE.csv` e `DENGBR25_CE.csv`.

### Resultado preliminar do processamento

| Arquivo | Registros filtrados |
|---|---:|
| DENGBR16 | 100.523 |
| DENGBR17 | 81.382 |
| DENGBR18 | 15.202 |
| DENGBR19 | 33.396 |
| DENGBR20 | 40.976 |
| DENGBR21 | 69.284 |
| DENGBR22 | 42.787 |
| DENGBR23 | 14.463 |
| DENGBR24 | 12.552 |
| DENGBR25 | 5.530 |
| **Total** | **416.095** |

**Observação metodológica:** os valores representam linhas filtradas por arquivo de origem. Ainda não correspondem necessariamente a casos únicos, confirmados ou ocorridos no ano indicado pelo nome do arquivo.

## 5. Escolha da referência temporal

Foram identificadas duas variáveis de interesse:

- `DT_NOTIFIC`: data de notificação do registro.
- `DT_SIN_PRI`: data de início dos primeiros sintomas.

A análise temporal principal utilizará, inicialmente, `DT_SIN_PRI`, enquanto `DT_NOTIFIC` poderá ser utilizada em análises complementares.

Foi observado que alguns arquivos contêm registros cujas datas pertencem a anos diferentes daqueles indicados em seus nomes. Por isso, o ano do arquivo não será considerado automaticamente como o ano de ocorrência.

## 6. Avaliação da qualidade das datas

Foi desenvolvido o script `scripts/verificar_intervalos.py` para calcular o intervalo, em dias, entre a data de início dos sintomas e a data de notificação.

Os registros foram classificados nas seguintes categorias:

- Notificação anterior ao início dos sintomas.
- Intervalo de 0 a 30 dias.
- Intervalo de 31 a 365 dias.
- Intervalo superior a 365 dias.
- Datas ausentes ou inválidas.

### Resultados da verificação

| Indicador | Registros |
|---|---:|
| Intervalo de 0 a 30 dias | 407.102 |
| Intervalo de 31 a 365 dias | 8.048 |
| Intervalo superior a 365 dias | 938 |
| Notificação anterior aos sintomas | 2 |
| Datas ausentes ou inválidas | 5 |
| **Total** | **416.095** |

Aproximadamente 97,84% dos registros apresentaram intervalos de até 30 dias.

Foram encontrados registros com intervalos superiores a 365 dias, incluindo datas de sintomas de décadas anteriores à notificação.

Também foram identificados dois registros no arquivo de 2022 em que a data de início dos sintomas era posterior à notificação:

| Notificação | Início dos sintomas |
|---|---|
| 19/04/2022 | 22/04/2022 |
| 02/02/2022 | 01/08/2022 |

Esses dois registros foram sinalizados como temporalmente inconsistentes. Ainda não foi aplicada uma rotina definitiva de exclusão.

### Decisão metodológica provisória

Os dados originais serão preservados. Registros com inconsistências temporais serão identificados e contabilizados antes da aplicação de critérios de limpeza.

Os intervalos superiores a 365 dias permanecerão sob investigação, sem exclusão automática.

## 7. Análises exploratórias já realizadas

Foi realizada uma análise inicial dos registros de 2024, incluindo:

- Distribuição mensal dos registros.
- Contagem de registros por município.
- Geração de gráficos com Python e Matplotlib.

Esses resultados são exploratórios e deverão ser reavaliados após a definição dos critérios de qualidade e classificação dos casos.

## 8. Pendências metodológicas

Antes de consolidar a base histórica, será necessário:

- Investigar possíveis duplicidades entre os arquivos.
- Consultar a documentação oficial para interpretar `CLASSI_FIN`.
- Definir os critérios de identificação dos casos confirmados.
- Estabelecer regras de tratamento das datas inconsistentes.
- Verificar a consistência dos códigos municipais.
- Obter dados populacionais para calcular taxas por 100 mil habitantes.
- Avaliar a completude dos dados referentes aos anos mais recentes.

## 9. Próximas etapas

1. Concluir a validação dos registros.
2. Separar notificações e casos confirmados.
3. Consolidar a série histórica de 2016 a 2025.
4. Produzir análises anuais e mensais.
5. Investigar a distribuição espacial por município.
6. Realizar a análise de tendências e sazonalidade.
7. Interpretar os resultados e redigir o artigo científico.

## 10. Registro de decisões futuras

Este espaço será atualizado conforme o desenvolvimento da pesquisa.

Para cada decisão relevante, registrar:

**Data:**

**Etapa:**

**Problema ou questão investigada:**

**Procedimento realizado:**

**Resultado obtido:**

**Decisão e justificativa:**

**Pendências:**

---

*Documento de acompanhamento interno da pesquisa. Os resultados registrados são preliminares e estão sujeitos à validação metodológica.*