# ficha-tecnica — Container

## Descrição
Folha técnica de um único componente. Container profundo e rastreável: cada valor possui unidade, fonte e estado de qualidade. Não faz comparação com outros produtos. É o container padrão quando o objetivo é documentar um componente específico em profundidade.

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Cabeçalho de identificação | S | Fabricante, modelo, part number, revisão do datasheet, data de coleta |
| Tabela de especificações | S | Campo → valor → unidade → fonte → estado |
| Seção de fontes | S | Todas as fontes consultadas com URL e data de acesso |
| Registro de dados ausentes | S | Campos `NULL-MISSING` com lista de fontes consultadas |
| Registro de conflitos | Quando houver | Referência ao `registro-conflitos` correspondente |

## Estrutura da tabela de especificações

Cada linha da tabela deve ter:

| Campo | Valor | Unidade | Fonte (ref) | Estado |
|---|---|---|---|---|
| Payload nominal | 10 | kg | [1] p.3 | confirmado |
| Parâmetro DH d1 | NULL-MISSING | mm | Consultado: [1][2] | nao-encontrado |
| Repetibilidade | 0.02 | mm | [1] p.5 / [2] p.8 → CONFLITO | conflito → ver RC-001 |

Estados válidos: `confirmado` | `nao-encontrado` | `nao-verificavel` | `conflito` | `obsoleto` | `nao-aplicavel`

## Regras de preenchimento
- Um componente por ficha — nunca consolidar dois modelos em uma ficha
- Cada valor numérico deve ter unidade explícita
- Referências numeradas [1], [2], etc. mapeando para a seção de fontes
- Conflito entre fontes: não escolher — registrar ambos, colocar status `conflito`, criar `registro-conflitos`
- Campo não encontrado: `NULL-MISSING` — nunca branco, nunca "—", nunca estimado
- Identificar a convenção usada quando aplicável (ex: convenção DH de Craig)

## O que o Supervisor verifica
- Cabeçalho de identificação completo (fabricante + modelo + revisão + data)
- Toda grandeza numérica tem unidade
- Toda linha tem fonte referenciada
- Campos ausentes declarados como `NULL-MISSING`, não omitidos
- Conflitos não resolvidos — ambos os valores preservados com fontes
- Seção de fontes com URL e data de acesso

## Tipos de dado compatíveis
`parametros-componente` | `interfaces-compatibilidade` | `software-firmware` | `dados-geometricos` | `conformidade-certificados` | `dados-seguranca-funcionais` | `dados-conectividade-comunicacao`
