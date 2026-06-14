# mapa-fornecedores — Container

## Descrição
Tabela estruturada de empresas que fornecem, distribuem, integram ou suportam produtos e funções relevantes para o projeto. Organiza quem entrega o quê — sem avaliação de qualidade, capacidade ou preferência.

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Cabeçalho | S | Função ou produto buscado, data de coleta |
| Tabela de fornecedores | S | Uma linha por empresa |
| Seção de fontes | S | Como cada empresa foi identificada |

## Estrutura da tabela de fornecedores

| Campo | Obrigatório | Notas |
|---|---|---|
| Empresa | S | Nome comercial |
| Papel | S | Fabricante / Distribuidor / Integrador / Suporte técnico / OEM |
| Produtos / marcas | S | O que esta empresa fornece ou representa |
| Cobertura geográfica | S | Brasil / estado(s) / América do Sul / global |
| Site | S | URL oficial |
| Certificações relevantes | N | Ex: UR Certified Integrator, ISO 9001 |
| Status da informação | S | Confirmado / Não verificável |
| Data de consulta | S | — |

## Regras de preenchimento
- Papel declarado: quando possível, verificar na lista oficial do fabricante (ex: UR Certified Partners)
- "Integrador" sem certificação verificável: marcar como `Não verificável`
- Não incluir avaliações de qualidade, histórico de projetos ou reputação
- Ordenar por papel e depois por nome
- Dados ausentes: `NULL-MISSING`

## O que o Supervisor verifica
- Sem texto avaliativo sobre qualidade ou capacidade de fornecedor
- Status de verificação declarado
- Data de consulta presente em todas as entradas
- Certificações verificáveis têm referência à fonte

## Tipos de dado compatíveis
`fornecedores-integradores` | `solucoes-mercado`
