# conformidade-regulatoria — Container

## Descrição
Evidência documental de conformidade de um componente ou sistema com requisitos regulatórios ou normativos. Organiza o que existe — certificados emitidos, declarações de conformidade, relatórios de ensaio para fins regulatórios. Não avalia se o produto deveria ser aprovado; registra o que já foi aprovado e documentado.

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Cabeçalho | S | Produto (fabricante + modelo + versão), data de coleta |
| Tabela de conformidades | S | Uma linha por certificação / declaração |
| Lacunas identificadas | S | Requisitos sem evidência documentada |
| Seção de fontes | S | Referências aos certificados e bases consultadas |

## Estrutura da tabela de conformidades

| Campo | Obrigatório | Notas |
|---|---|---|
| Requisito / norma | S | Número e ano da norma ou regulamento |
| Tipo de evidência | S | Certificado / Declaração de Conformidade / Relatório de ensaio |
| Número do documento | S | Número do certificado ou referência do documento |
| Organismo / emissor | S | Quem emitiu |
| Data de emissão | S | — |
| Validade | N | `NULL-MISSING` se não tiver prazo |
| Escopo da evidência | S | O que exatamente está coberto — pode excluir itens |
| Status | S | Válido / Expirado / Suspenso / Retirado |
| URL de verificação | N | Link público de verificação no organismo |

## Seção de lacunas

Para cada requisito identificado como aplicável mas sem evidência:

| Requisito | Status | Notas |
|---|---|---|
| ISO XXXX-1 | NULL-MISSING | Consultado: [1][2] — não encontrado |

## Regras de preenchimento
- Nunca inferir conformidade: ausência de evidência = `NULL-MISSING`
- Escopo pode ter exclusões: "certificado CE cobre módulo base, exclui módulo de força"
- Verificar status no organismo quando possível (certificados podem ser retirados)
- Requisitos identificados como aplicáveis mas sem evidência vão obrigatoriamente na seção de lacunas

## O que o Supervisor verifica
- Sem inferências de conformidade
- Lacunas listadas (não omitidas)
- Status com data de verificação
- Escopo declarado para cada certificação

## Tipos de dado compatíveis
`conformidade-certificados` | `normas-regulamentacoes`
