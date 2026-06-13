# Catálogo de Ferramentas do Executor

O Executor consulta este arquivo para saber quais ferramentas estão disponíveis e quando usá-las. Cada ferramenta tem um script Python correspondente nesta pasta.

---

## `web_search` — Busca na internet

**Arquivo:** `web_search.py`  
**Quando usar:** Qualquer tarefa que exija dados atualizados, especificações técnicas, literatura, parâmetros de fabricantes.  
**Não usar para:** Dados que o modelo já sabe com alta confiança e que não mudam (ex: fórmulas matemáticas estabelecidas).

```
Entrada:  query (str), max_results (int, padrão: 5)
Saída:    lista de { title, url, snippet, content }
```

---

## `generate_pdf` — Geração de PDF

**Arquivo:** `pdf_generator.py`  
**Quando usar:** Relatórios técnicos, estudos com múltiplas seções, entregas formais de pesquisa.  
**Formato esperado:** Markdown estruturado com `# Título`, `## Seção`, tabelas, fórmulas LaTeX entre `$$`.

```
Entrada:  content_markdown (str), filename (str), metadata (dict)
Saída:    caminho do arquivo PDF gerado
```

---

## `generate_docx` — Geração de Word (.docx)

**Arquivo:** `docx_generator.py`  
**Quando usar:** Documentos que o usuário editará posteriormente, relatórios colaborativos, entregas em formato Word.

```
Entrada:  content_markdown (str), filename (str), template (str, opcional)
Saída:    caminho do arquivo .docx gerado
```

---

## `generate_xlsx` — Geração de planilha Excel (.xlsx)

**Arquivo:** `xlsx_generator.py`  
**Quando usar:** Dados tabulares com múltiplas colunas, comparações numéricas, datasets de parâmetros, benchmarks.  
**Não usar para:** Uma única tabela simples que cabe melhor num PDF.

```
Entrada:  data (list[dict] ou dict de sheets), filename (str)
Saída:    caminho do arquivo .xlsx gerado
```

---

## Decisão de ferramenta (regra do Ordenador)

| Tipo de tarefa | Ferramenta de busca | Formato de saída |
|---|---|---|
| Levantamento de parâmetros técnicos | web_search | xlsx ou pdf |
| Análise metodológica | web_search | pdf |
| Geração de script/código | — (modelo gera direto) | .py / .js no GitHub |
| Comparação de equipamentos | web_search | xlsx |
| Estudo de caso documentado | web_search | docx ou pdf |
| Definição de envelope/workspace | web_search | pdf com figuras |
