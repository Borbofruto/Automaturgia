# repositorio-referencias — Container

## Descrição
Biblioteca de metadados de fontes consultadas em uma tarefa de coleta. Registra onde os dados foram buscados, o que cada fonte contém e o status de acesso — independentemente de a fonte ter retornado dados ou não. Serve como log de rastreabilidade das fontes, não como índice de conteúdo.

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Cabeçalho | S | Contexto da coleta, data de geração |
| Tabela de referências | S | Uma linha por fonte |

## Estrutura da tabela de referências

| Campo | Obrigatório | Notas |
|---|---|---|
| ID | S | [1], [2], etc. — usado para referenciar nos outros containers |
| Tipo | S | Datasheet / Manual / Paper / Application note / Website / Norma / Relatório |
| Título | S | Nome exato do documento ou página |
| Autor / Fabricante / Organismo | S | — |
| Ano / Data de publicação | N | — |
| URL | S | Link direto; `NULL-MISSING` se apenas documento físico |
| Data de acesso | S | DD/MM/AAAA |
| Versão / Revisão | N | Número de revisão do documento |
| Dados extraídos | N | Quais campos foram obtidos desta fonte |
| Status de acesso | S | Acessado / Restrito (paywall) / Inacessível / Não encontrado |
| Estado da fonte | N | Ativa / Obsoleta / Removida |

## Regras de preenchimento
- Listar todas as fontes consultadas — inclusive as que não retornaram dados (status: `Não encontrado`)
- Fontes consultadas e não encontradas são evidência de `NULL-MISSING` nos campos correspondentes
- ID deve ser sequencial e consistente com as referências nos outros containers da mesma tarefa
- URL deve ser o link direto ao documento, não à página inicial do site
- Dados extraídos: lista dos campos que foram coletados desta fonte — serve para auditoria

## O que o Supervisor verifica
- Toda fonte referenciada nos outros containers aparece aqui
- Data de acesso presente em todas as entradas
- Fontes consultadas sem resultado estão listadas com status `Não encontrado`

## Tipos de dado compatíveis
Todos os tipos de dado — este container é transversal e acompanha qualquer coleta.
