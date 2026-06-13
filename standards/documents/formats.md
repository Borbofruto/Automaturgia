# Padrões de Formato de Entrega — Automaturge

O Ordenador usa este documento para decidir qual formato de arquivo gerar para cada tarefa.
O Supervisor usa para verificar se o formato entregue está em conformidade.

---

## Regra de decisão de formato

```
Tarefa contém dados numéricos comparativos ou paramétricos?
  └─ SIM → XLSX (tabela estruturada)

Tarefa requer análise narrativa longa (>3 seções) + dados?
  └─ SIM → PDF (relatório técnico)

Tarefa é documentação que o usuário vai editar depois?
  └─ SIM → DOCX (Word editável)

Tarefa gera script, algoritmo, código?
  └─ SIM → .py / .js / .m no GitHub (não no Drive)

Tarefa é comparação simples, checklist, ou resultado de benchmark?
  └─ SIM → XLSX

Padrão quando não se encaixa em nenhum acima → PDF
```

---

## Formatos aprovados

### PDF — Relatório Técnico

**Quando usar:** Estudos, análises metodológicas, relatórios de pesquisa com múltiplas seções.

**Estrutura obrigatória:**
```
1. Título e metadados (autor, data, versão)
2. Resumo executivo (máx. 200 palavras)
3. Objetivo e escopo
4. Metodologia (referência a /standards/research/methodology.md)
5. Resultados
6. Análise e discussão
7. Limitações e incertezas
8. Fontes e rastreabilidade
```

**Requisitos técnicos:**
- Fonte mínima: 11pt
- Margens: 2.5cm todos os lados
- Tabelas com cabeçalho destacado
- Fórmulas em notação LaTeX quando relevante
- Numeração de páginas
- Rodapé: "Automaturge · [Título] · Página X de Y"

---

### XLSX — Planilha de Dados

**Quando usar:** Parâmetros técnicos, benchmarks, comparativos numéricos, datasets.

**Estrutura obrigatória:**
- Linha 1: Título do dataset
- Linha 2: Data de geração e origem
- Linha 4+: Cabeçalhos + dados (cabeçalho fundo escuro, texto branco)
- Aba separada para metadados/fontes quando há múltiplas origens

**Requisitos técnicos:**
- Unidades sempre no cabeçalho da coluna: ex. `d (mm)`, `alpha (rad)`
- Valores ausentes: célula vazia com nota na aba "Metadados"
- Sem abreviações nos cabeçalhos sem legenda
- Colunas auto-dimensionadas

---

### DOCX — Documento Editável

**Quando usar:** Documentação que será revisada/complementada pelo usuário, templates de procedimento.

**Estrutura obrigatória:**
- Capa com título, data, versão
- Sumário automático (via estilos de heading)
- Seções com Heading 1/2/3 (não negrito manual)
- Tabelas com estilo "Table Grid"

---

### Script (.py / .js) → GitHub

**Quando usar:** Quando a tarefa é gerar código, algoritmo, ferramenta reutilizável.

**Destino:** `/tools/` no repositório GitHub (não vai para o Drive)

**Requisitos:**
- Docstring obrigatória no topo do arquivo
- Seção de uso (`if __name__ == "__main__"`)
- Comentários em pontos não-óbvios
- requirements.txt atualizado se necessário

---

## Destino final por formato

| Formato | Destino |
|---|---|
| PDF | Google Drive → pasta correspondente ao bloco de estudo (B1–B10) |
| DOCX | Google Drive → pasta correspondente ao bloco de estudo |
| XLSX | Google Drive → pasta correspondente ao bloco de estudo |
| Script (.py/.js) | GitHub → `/tools/` |
| Metodologia validada | GitHub → `/standards/` |
