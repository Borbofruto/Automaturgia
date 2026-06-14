# Automaturge · Research & Methods for Applied Robotics

A **Automaturge** é uma iniciativa de pesquisa e desenvolvimento de métodos para robótica aplicada — produz métodos práticos de automação robótica e os estudos técnicos que os fundamentam.

Este repositório contém a infraestrutura do **pipeline de geração de dossiês técnicos** que a Automaturge usa como etapa de pesquisa. O pipeline automatiza a compilação e estruturação de material técnico existente — normas, datasheets, literatura, especificações — em dossiês rastreáveis que servem de embasamento teórico para os estudos e métodos que a Automaturge produz. Os agentes de IA não criam conhecimento, não interpretam, não concluem: reúnem e organizam o que já existe.

É uma ferramenta da Automaturge — não o produto dela.

> **O pipeline reúne dados técnicos. A Automaturge conclui algo com eles.**
> "Uma pesquisa reúne dados. Um método ensina como usá-los."

---

## Estrutura

```
/standards
  /data-types     → Templates de coleta por tipo de dado (o que coletar)
  /containers     → Templates de entrega por formato de container (como estruturar)
/prompts          → System prompts dos agentes (Ordenador, Executor, Supervisor)
/tools            → Scripts executáveis pelos agentes (busca, geração de documentos)
/pipeline         → Código do workflow n8n
```

---

## Agentes e seus papéis

| Agente | Modelo | O que lê aqui |
|---|---|---|
| **Ordenador** | DeepSeek V3 | `/standards/` → lê templates do tipo de dado e container configurados na tarefa, constrói brief para o Executor |
| **Executor** | Qwen 2.5 Coder 32B | `/tools/` → coleta e estrutura os dados conforme brief do Ordenador |
| **Supervisor** | Gemini Flash 3 | `/standards/containers/` → valida rastreabilidade, completude e formato; sinaliza conflitos sem resolvê-los |

Custo e política de modelos: ver `standards/agents/model-policy.md`. A regra geral é <$1/M tokens; existe exceção documentada para o Supervisor em tarefas críticas.

---

## Como uma tarefa é configurada

No ClickUp, cada tarefa de pesquisa define duas dimensões de tag:

- **Dimensão 1 — tipo de dado** (`/standards/data-types/`): o que coletar
- **Dimensão 2 — container** (`/standards/containers/`): como entregar

O Ordenador lê os dois templates correspondentes antes de construir o brief. As dimensões nunca se fundem em uma tag só.

**Exemplo:** coletar especificações do cobot UR10e
→ tags `parametros-componente` + `ficha-tecnica`

**Exemplo:** mapear cobots de payload médio disponíveis no Brasil
→ tags `solucoes-mercado` + `tabela-comparativa`

---

## Vocabulário de tags

### Dimensão 1 — Tipos de dado

| Tag | O que é coletado |
|---|---|
| `parametros-componente` | Especificações técnicas de qualquer componente (geometria, faixa operacional, interfaces, desempenho declarado) |
| `interfaces-compatibilidade` | Protocolos, pinout, I/O entre componentes |
| `software-firmware` | Versões, SDKs, URCaps, changelogs de API |
| `dados-geometricos` | CAD/STEP/URDF, envelope de trabalho |
| `normas-regulamentacoes` | ISO, IEC, ABNT — identificação e escopo, sem interpretação |
| `desempenho-ensaio` | Resultados de medição com método e condições (base ISO 9283) |
| `conformidade-certificados` | Certificados e declarações de conformidade emitidos |
| `solucoes-mercado` | Produtos disponíveis no mercado por função (COTS) |
| `fornecedores-integradores` | Quem projeta, revende, integra ou suporta |
| `casos-aplicacao` | Registros descritivos de instalações reais — sem análise |
| `processos-procedimentos` | Sequências técnicas: calibração, montagem, parametrização |
| `literatura-tecnica` | Índice de existência de publicações — sem síntese |
| `dados-layout-infraestrutura` | Área, pontos de fixação, cargas de piso, infraestrutura |
| `dados-seguranca-funcionais` | Zonas de segurança, PL, SIL, parâmetros de parada |
| `dados-conectividade-comunicacao` | Redes, protocolos, endereçamento, OPC UA, fieldbus |
| `modelos-interoperabilidade` | Esquemas ISO 10303/EXPRESS, estruturas de dados eCl@ss |

### Dimensão 2 — Containers

| Tag | Descrição |
|---|---|
| `ficha-tecnica` | Folha de um único componente — profunda e rastreável |
| `tabela-comparativa` | Múltiplos itens lado a lado — sem ranking ou conclusão |
| `catalogo-solucoes` | Índice da oferta de mercado agrupado por função |
| `inventario-normas` | Lista estruturada de normas com status e escopo |
| `repositorio-referencias` | Biblioteca de metadados de fontes consultadas |
| `planilha-dados-brutos` | Medições ou logs antes de qualquer processamento |
| `mapa-fornecedores` | Quem entrega/suporta cada item ou função |
| `dossier-interface` | Container relacional para dados entre dois objetos |
| `registro-ensaios` | Medições com método, setup e condições documentadas |
| `caderno-procedimentos` | Coleção indexada de procedimentos reutilizáveis |
| `conformidade-regulatoria` | Evidência documental de conformidade legal |
| `dossie-tecnico-tdp` | Meta-container para pacote de dados de sistema completo |
| `registro-conflitos` | **Transversal** — sempre criado quando há conflito ou lacuna |
| `evidence-pack` | Pacote completo de uma execução (dossier + referências + lacunas + conflitos + metadados) |

---

## Princípios de qualidade

**Fonte ≠ Container.**
O datasheet OEM é fonte. A ficha técnica interna é container derivado. A pipeline extrai o tipo de dado correto para o container correto, preservando ponteiros de proveniência (documento, revisão, página, data).

**A IA nunca resolve conflitos.**
Quando duas fontes divergem, ambos os valores são preservados com fonte, data e contexto individuais. Um `registro-conflitos` é criado. Status do campo: `conflito`. A IA não escolhe, não media, não estima.

**Dados ausentes recebem `NULL-MISSING`.**
Nunca campo em branco. O log registra quais fontes foram consultadas e não retornaram o dado.

**Estados de qualidade dos campos:**
`confirmado` | `nao-encontrado` | `nao-verificavel` | `conflito` | `obsoleto` | `nao-aplicavel`

**Completude em três níveis (ISO 8000):**
1. *Atributo* — campos críticos preenchidos
2. *Metadado* — cada valor tem unidade e fonte (per IEC 62720)
3. *Identificação* — part number em formato padronizado (per ISO 8000-115)
