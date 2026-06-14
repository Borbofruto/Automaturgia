# tabela-comparativa — Container

## Descrição
Tabela que coloca múltiplos itens lado a lado para facilitar a leitura de diferenças. Não há coluna de ranking, recomendação ou melhor opção. Cada célula tem valor, unidade e referência de fonte. O container organiza dados — não conclui nada sobre eles.

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Cabeçalho da tabela | S | Parâmetro / Item A / Item B / Item C... |
| Identificação de cada item | S | Fabricante + Modelo + Revisão/Versão — na linha de cabeçalho de coluna |
| Linhas de parâmetros | S | Um parâmetro por linha |
| Rodapé de fontes | S | Referências numeradas mapeando cada célula |
| Registro de dados ausentes | S | Células `NULL-MISSING` explicadas |
| Registro de conflitos | Quando houver | Referência ao `registro-conflitos` correspondente |

## Estrutura de cada célula

Cada célula deve conter: valor + unidade + [ref]

Exemplos:
- `10 kg [1]`
- `NULL-MISSING [consultado: 1, 2]`
- `0.02 mm [1] / 0.05 mm [2] → CONFLITO RC-001`

## Regras de preenchimento
- Todos os itens comparados devem ser do mesmo tipo e função — não comparar robôs de categorias diferentes sem declarar isso
- Parâmetros nas linhas devem usar nomenclatura consistente entre colunas
- Condições de medição idênticas entre itens, ou diferenças explicitadas na linha: ex. "Payload @10% speed" vs. "Payload @100% speed"
- Sem coluna "Melhor", "Recomendado", "Vencedor" ou equivalente
- Sem notas de texto concluindo qual item é superior
- Células não encontradas: `NULL-MISSING` — nunca branco
- Conflito entre fontes para o mesmo item: registrar ambos na célula + criar `registro-conflitos`
- Ordenar itens alfabeticamente por fabricante — não por desempenho

## O que o Supervisor verifica
- Toda célula com valor numérico tem unidade e referência
- Nenhuma célula em branco — `NULL-MISSING` onde não houver dado
- Sem coluna ou nota de ranking
- Condições de medição declaradas quando há risco de comparação injusta
- Fontes acessíveis via referências no rodapé

## Tipos de dado compatíveis
`parametros-componente` | `solucoes-mercado` | `desempenho-ensaio` | `software-firmware` | `dados-conectividade-comunicacao`
