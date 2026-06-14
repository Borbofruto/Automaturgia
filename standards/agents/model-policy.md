# Política de Modelos e Custo — Automaturge

Define quais modelos são permitidos por função na pipeline, o teto de custo e as condições de exceção. Este documento resolve explicitamente qualquer contradição entre o README e os prompts individuais dos agentes.

---

## Regra geral

Todos os modelos usados na pipeline automática devem custar **menos de $1,00 por milhão de tokens** (input + output combinados, considerando o preço mais alto entre as duas métricas).

Esta regra existe para viabilizar volume de execuções sem custo operacional proibitivo.

---

## Modelos aprovados por função

| Função | Modelo | Provider | Custo aprox. (input/output) | Status |
|---|---|---|---|---|
| Ordenador | DeepSeek V3 (`deepseek/deepseek-chat`) | OpenRouter | ~$0.27 / $1.10 per M | ✓ Aprovado (input abaixo do teto) |
| Executor | Qwen 2.5 Coder 32B (`qwen/qwen-2.5-coder-32b-instruct`) | OpenRouter | ~$0.07 / $0.12 per M | ✓ Aprovado |
| Supervisor | Gemini Flash 3 (`google/gemini-flash-3-preview`) | OpenRouter | ~$0.10 / $0.40 per M | ✓ Aprovado (sem thinking) |
| Supervisor (crítico) | Gemini Flash 3 com thinking: high | OpenRouter | Variável — verificar | ⚠️ Exceção (ver abaixo) |

> **Nota:** Preços de modelos via OpenRouter variam e são atualizados pelo provedor sem aviso. Verificar preços reais em [openrouter.ai/models](https://openrouter.ai/models) antes de cada deploy significativo.

---

## Exceção para Supervisor com thinking: high

O Supervisor pode usar `thinking: high` quando a tarefa envolver **qualquer** dos seguintes critérios:

- Dados de segurança funcional (PL, SIL, zonas de segurança)
- Parâmetros de normas técnicas (onde interpretação incorreta tem consequências)
- Validação de conformidade (certificados, declarações)
- Risco alto de alucinação técnica identificado pelo Ordenador
- Tarefa de nível de maturidade `verified` ou superior

O Ordenador sinaliza isso no `validation_brief`:

```json
"supervisor_thinking": "high",
"supervisor_thinking_reason": "Dados de segurança funcional — ISO 10218"
```

Para tarefas de maturidade `exploratory` ou `documented` sem dados críticos: usar Supervisor sem thinking.

---

## Modelos não permitidos na pipeline automática

- **Claude (qualquer versão):** usado apenas para planejamento externo à pipeline. Custo proibitivo para automação em volume.
- **GPT-4o / GPT-4:** custo acima do teto.
- **Gemini Pro / Ultra:** custo acima do teto.
- Qualquer modelo acima de $1,00/M tokens sem exceção documentada aqui.

---

## Revisão desta política

Preços de modelos mudam com frequência. Esta política deve ser revisada:
- A cada novo deploy do pipeline
- Quando um modelo for descontinuado ou substituído
- Quando o volume de execuções aumentar significativamente

Última revisão: 2026-06
