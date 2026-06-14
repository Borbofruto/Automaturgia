# catalogo-solucoes — Container

## Descrição
Índice estruturado de produtos e soluções disponíveis no mercado para uma função técnica específica. Organiza o que existe — sem ranking, sem recomendação, sem análise comparativa. É o ponto de partida para quem precisa saber quais opções existem antes de aprofundar o estudo de casos específicos.

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Cabeçalho | S | Função técnica buscada, data de coleta, critérios de inclusão |
| Tabela de soluções | S | Uma entrada por produto/solução |
| Critérios de inclusão | S | O que define que um produto entrou nesta lista |
| Seção de fontes | S | URLs consultadas com data de acesso |

## Estrutura da tabela de soluções

| Campo | Obrigatório | Notas |
|---|---|---|
| Fabricante | S | — |
| Produto / Modelo | S | — |
| Categoria / subcategoria | S | Para organização interna |
| Especificações-chave | S | 3-5 specs relevantes para a função |
| Disponibilidade (Brasil) | S | Disponível / Sob consulta / Não distribuído no BR |
| Status comercial | S | Disponível / Descontinuado / Anunciado |
| URL | S | Página oficial do produto |
| Data de consulta | S | — |

## Regras de preenchimento
- Critérios de inclusão devem ser declarados no cabeçalho: o que define o escopo do catálogo (ex: "cobots de payload 3-15 kg com distribuição no Brasil")
- Produtos fora do critério não entram — se o critério for ajustado, declarar isso
- Ordenar por fabricante alfabeticamente — não por desempenho ou preferência
- Não incluir preços
- "Disponibilidade no Brasil" deve ser verificada — não assumir que produto global está disponível localmente
- Descontinuados podem aparecer se relevantes para contexto histórico — marcar claramente
- Dados ausentes em campos de um produto: `NULL-MISSING`

## O que o Supervisor verifica
- Critérios de inclusão declarados
- Ordenação não implica ranking
- Status comercial verificado e com data
- Toda entrada tem URL e data de consulta
- Sem texto avaliativo ou comparativo

## Tipos de dado compatíveis
`solucoes-mercado` | `fornecedores-integradores`
