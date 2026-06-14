# registro-ensaios — Container

## Descrição
Registro estruturado de uma sessão de ensaio ou medição: o que foi medido, com qual método, em que condições, com qual setup, produzindo quais resultados. Cada sessão de ensaio gera um registro independente. Os resultados são medições — não conclusões sobre desempenho.

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Cabeçalho do ensaio | S | Identificação do DUT, objetivo do ensaio, data, executor |
| Método de ensaio | S | Norma de referência ou descrição do procedimento |
| Condições do ensaio | S | Todas as variáveis controladas |
| Setup do ensaio | S | Instrumentos, configuração, diagrama se aplicável |
| Tabela de resultados | S | Medições brutas com unidades |
| Seção de fontes | S | Referência ao documento do método e ao DUT |

## Estrutura do cabeçalho

| Campo | Obrigatório | Notas |
|---|---|---|
| DUT (Device Under Test) | S | Fabricante + modelo + versão + número de série se disponível |
| Objetivo do ensaio | S | O que se quer medir |
| Data do ensaio | S | — |
| Executor | S | Nome ou instituição |
| Laboratório / local | N | — |

## Estrutura das condições do ensaio

| Campo | Obrigatório | Notas |
|---|---|---|
| Payload de teste | S se aplicável | Valor + unidade + posição do CG se relevante |
| Velocidade programada | S se aplicável | — |
| Temperatura ambiente | N | — |
| Postura / trajetória de teste | S para performance | Descrição ou referência ao ciclo ISO 9283 |
| Número de amostras | S | — |

## Estrutura da tabela de resultados

| Medição # | Parâmetro | Valor | Unidade | Instrumento | Observações |
|---|---|---|---|---|---|

## Regras de preenchimento
- Método obrigatório: citar norma (ISO 9283, etc.) ou descrever o procedimento usado
- Condições mínimas obrigatórias: payload, velocidade, temperatura (quando relevante)
- Resultados são dados brutos — sem média ou estatística calculada no registro (ficam em derivados)
- Incerteza de medição deve ser registrada se o instrumento a declara
- Não incluir interpretações sobre o que os resultados significam para o desempenho

## O que o Supervisor verifica
- Método declarado com referência ou descrição
- Condições completas para que o ensaio seja reproduzível
- Resultados com unidades e instrumento identificado
- Sem interpretações ou conclusões sobre adequação do DUT

## Tipos de dado compatíveis
`desempenho-ensaio` | `dados-seguranca-funcionais`
