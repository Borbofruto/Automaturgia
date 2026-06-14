# planilha-dados-brutos — Container

## Descrição
Tabela de medições ou logs no estado em que foram coletados — antes de qualquer processamento, cálculo derivado ou transformação. Cada linha é um registro de medição com identificação completa de quando, onde, como e em que condições foi obtido. Cálculos derivados, médias ou estatísticas, se necessários, vão em aba separada com identificação clara.

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Aba "Dados Brutos" | S | Medições originais sem transformação |
| Aba "Metadados" | S | Descrição das colunas, unidades, instrumentos, condições |
| Aba "Derivados" | Quando houver cálculos | Identificar claramente que são derivados — com fórmula usada |
| Aba "Fontes" | S | Referência às fontes dos dados |

## Estrutura da aba Dados Brutos

| Campo obrigatório | Notas |
|---|---|
| Timestamp | Data e hora, ou número sequencial de ciclo |
| Parâmetro medido | Nome exato do parâmetro |
| Valor | Numérico — sem texto nesta coluna |
| Unidade | Em coluna separada ou no cabeçalho da coluna de valor |
| Instrumento / método | Identificação do instrumento ou método que gerou o dado |
| Condições | Estado do sistema durante a medição (carga, velocidade, temperatura, etc.) |

## Regras de preenchimento
- Sem mesclagem de células nas linhas de dados
- Unidades no cabeçalho da coluna: ex. "Força (N)", não na célula de dado
- Valores ausentes: `NULL-MISSING` — nunca branco, nunca zero como substituto
- Não filtrar outliers dos dados brutos — eles ficam na aba de brutos; filtragem vai na aba de derivados com critério documentado
- Cabeçalho da aba "Dados Brutos" com fundo escuro e texto claro
- Aba "Metadados" deve descrever cada coluna, incluindo range esperado e instrumento usado

## O que o Supervisor verifica
- Aba "Dados Brutos" sem fórmulas nas células de dado
- Toda coluna numérica com unidade no cabeçalho
- Sem células em branco nos dados — `NULL-MISSING` ou valor
- Aba "Metadados" presente com descrição de todas as colunas

## Tipos de dado compatíveis
`desempenho-ensaio` | `dados-layout-infraestrutura` | `dados-seguranca-funcionais`
