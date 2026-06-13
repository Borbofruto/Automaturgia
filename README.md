# Automaturge · Research & Methods for Applied Robotics

Repositório de infraestrutura de conhecimento da iniciativa **Automaturge**.

Este repositório não é um produto nem uma biblioteca de código genérico. É a **base operacional** do pipeline de pesquisa automatizada — contém as ferramentas, padrões e instruções que os agentes de IA utilizam para executar, validar e entregar estudos técnicos em robótica industrial.

---

## Estrutura

```
/tools          → Scripts executáveis pelos agentes (busca, geração de documentos, etc.)
/standards      → Padrões de metodologia, formato de entrega e critérios de qualidade
/prompts        → System prompts dos agentes (Ordenador, Executor, Supervisor)
```

---

## Agentes e seus papéis

| Agente | Modelo | O que lê aqui |
|---|---|---|
| **Ordenador** | DeepSeek V3 | `/standards/` + `/tools/README.md` → decide formato de saída e ferramentas |
| **Executor** | Qwen 2.5 Coder 32B | `/tools/` → executa ferramentas conforme brief do Ordenador |
| **Supervisor** | Gemini Flash (thinking: high) | `/standards/quality/` → valida formato e conteúdo independentemente |

---

## Princípio de uso

O Ordenador lê uma tarefa do ClickUp (escrita em linguagem humana, descrevendo objetivo) e consulta este repositório para:
1. Identificar qual **padrão de formato** se aplica (`/standards/documents/`)
2. Identificar qual **metodologia de pesquisa** se aplica (`/standards/research/`)
3. Identificar quais **ferramentas** o Executor precisará (`/tools/README.md`)
4. Construir dois briefs distintos: um para o Executor, outro para o Supervisor

Isso elimina a necessidade de detalhar ferramentas e metodologias em cada tarefa do ClickUp.
