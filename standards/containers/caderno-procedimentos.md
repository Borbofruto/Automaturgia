# caderno-procedimentos — Container

## Descrição
Coleção indexada de procedimentos técnicos relacionados a um componente ou sistema. Agrupa múltiplos procedimentos do mesmo escopo (ex: todos os procedimentos de manutenção de um robô específico) em um documento navegável por índice. Cada procedimento é transcrito da fonte — não adaptado, não otimizado.

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Cabeçalho | S | Componente/sistema de escopo, data de coleta, versão dos documentos fonte |
| Índice de procedimentos | S | Lista numerada com título e tipo de cada procedimento |
| Procedimentos individuais | S | Um por seção, estrutura padronizada |
| Seção de fontes | S | Referência a cada documento de origem |

## Estrutura de cada procedimento

| Seção | Obrigatório | Notas |
|---|---|---|
| ID do procedimento | S | Ex: PROC-001 |
| Nome | S | — |
| Tipo | S | Calibração / Montagem / Manutenção / Configuração / Comissionamento |
| Componente de escopo | S | Fabricante + modelo + versão |
| Pré-requisitos | N | O que deve estar feito antes de iniciar |
| Ferramentas necessárias | N | Com especificações declaradas na fonte |
| Passos | S | Lista numerada — transcrição literal da fonte |
| Avisos de segurança | S (quando presentes) | Transcrição literal dos avisos da fonte |
| Fonte | S | Documento + seção + página |
| Versão da fonte | S | Número de revisão ou data |

## Regras de preenchimento
- Procedimentos de fontes diferentes devem manter referência individual à fonte de cada um
- Não consolidar procedimentos similares de fontes diferentes — manter separados com suas fontes
- Não adaptar linguagem dos passos — transcrição literal
- Avisos de segurança intercalados nos passos devem ser preservados na posição original
- Índice usa IDs (PROC-001, PROC-002) para navegação

## O que o Supervisor verifica
- Índice presente e consistente com as seções
- Cada procedimento tem fonte com versão identificada
- Passos são transcrição, não paráfrase
- Avisos de segurança da fonte preservados

## Tipos de dado compatíveis
`processos-procedimentos`
