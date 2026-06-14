# registro-conflitos — Container

## Descrição
Ledger transversal de conflitos e lacunas de dados identificados durante uma coleta. Sempre criado quando há divergência entre fontes ou dado estruturalmente ausente após consulta exaustiva. A IA nunca resolve conflitos — preserva ambas as afirmações com proveniência completa e registra aqui para resolução humana posterior.

## Quando criar uma entrada
- Duas ou mais fontes retornam valores diferentes para o mesmo campo do mesmo objeto
- Uma fonte retorna um valor que contradiz outro campo do mesmo documento
- Um campo é obrigatório no template mas não foi encontrado em nenhuma das fontes consultadas (dado estruturalmente ausente, não apenas não prioritizado)

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Cabeçalho | S | Sistema / tarefa, data de geração |
| Tabela de entradas | S | Uma linha por conflito ou lacuna |

## Estrutura de cada entrada

| Campo | Obrigatório | Notas |
|---|---|---|
| ID | S | RC-001, RC-002, etc. |
| Tipo | S | Conflito / Lacuna |
| Componente / objeto | S | A qual componente ou relação se refere |
| Campo em conflito ou ausente | S | Nome exato do campo conforme o template |
| Container de origem | S | Qual container identificou este conflito |
| **Para conflitos:** Valor A | S | Valor + unidade + fonte A (ref + página) |
| **Para conflitos:** Valor B | S | Valor + unidade + fonte B (ref + página) |
| **Para lacunas:** Fontes consultadas | S | Lista de fontes verificadas sem resultado |
| Status | S | Aberto / Escalado / Resolvido por humano |
| Data de detecção | S | — |
| Resolução | N | Preenchido apenas por humano — nunca pela IA |

## Regras absolutas
- A IA NUNCA preenche o campo "Resolução" — este campo é exclusivo para humanos
- A IA NUNCA remove uma entrada do registro — apenas humanos podem marcar como Resolvido
- Conflito ≠ dado errado: ambos os valores são preservados sem julgamento de qual está correto
- Para lacunas: listar explicitamente quais fontes foram consultadas — é evidência de que a busca foi feita
- Toda entrada referenciada em outro container como `status: conflito` deve ter um RC correspondente aqui

## O que o Supervisor verifica
- Todo campo marcado como `conflito` em qualquer container tem entrada correspondente aqui
- Entradas de conflito têm os dois valores com fontes individuais
- Entradas de lacuna têm lista de fontes consultadas
- Campo "Resolução" está vazio — não foi preenchido pela IA
- Sem entradas RC sem ID

## Tipos de dado compatíveis
Todos — este container é transversal a toda coleta.
