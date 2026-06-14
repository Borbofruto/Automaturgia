# inventario-normas — Container

## Descrição
Lista estruturada de normas técnicas aplicáveis a um contexto específico: identificação, escopo e status. Não interpreta requisitos, não extrai obrigações, não conclui o que um produto deve atender. É um índice — a análise de conformidade é trabalho posterior ao dossier.

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Cabeçalho | S | Contexto de aplicação (ex: "Sistemas robóticos colaborativos industriais"), data de coleta |
| Tabela de normas | S | Uma linha por norma |
| Seção de fontes | S | URLs dos catálogos consultados com data de acesso |

## Estrutura da tabela de normas

| Campo | Obrigatório | Notas |
|---|---|---|
| Número da norma | S | Ex: "ISO 10218-1:2011" |
| Título oficial | S | Título exato no idioma original |
| Organismo | S | ISO / IEC / ABNT / EN / etc. |
| Ano de publicação | S | — |
| Status | S | Ativa / Supersedida / Retirada / Em revisão |
| Sucedida por | N | Número da norma mais recente, se supersedida |
| Escopo (resumo literal) | S | Primeiras linhas do campo Scope da norma |
| Aplicabilidade ao contexto | N | Descrição de como esta norma se aplica ao contexto da tarefa |
| Disponibilidade | N | Paga / Gratuita / Parcialmente pública |

## Regras de preenchimento
- Escopo deve ser transcrição literal do documento oficial — nunca paráfrase ou interpretação
- Aplicabilidade ao contexto é descritiva: "esta norma cobre X, que está presente no sistema Y" — não "o sistema Y deve cumprir os requisitos Z"
- Status deve ser verificado no catálogo oficial na data de coleta — normas são revisadas
- Normas que se aplicam em conjunto devem ser listadas individualmente — não consolidar
- Dados ausentes: `NULL-MISSING`

## O que o Supervisor verifica
- Escopo é transcrição literal, não síntese
- Status verificado com data
- Sem texto interpretativo de requisitos
- Toda norma tem referência ao catálogo oficial

## Tipos de dado compatíveis
`normas-regulamentacoes`
