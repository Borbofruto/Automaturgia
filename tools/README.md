# Catálogo de Ferramentas do Executor

O Executor consulta este arquivo para saber quais ferramentas estão disponíveis e quando usá-las. Cada ferramenta tem um script Python correspondente nesta pasta.

---

## `web_search` — Busca na internet

**Arquivo:** `web_search.py`  
**Quando usar:** Qualquer tarefa que exija dados técnicos atualizados: especificações de componentes, certificados, normas, distribuição no mercado.  
**Não usar para:** Dados que o modelo já sabe com alta confiança e que não mudam (ex: fórmulas matemáticas estabelecidas).

```
Entrada:  query (str), max_results (int, padrão: 5)
Saída:    lista de { title, url, snippet, content }
```

---

## `generate_pdf` — Geração de PDF

**Arquivo:** `pdf_generator.py`  
**Quando usar:** Containers que requerem documento formal: ficha-tecnica, dossier-interface, conformidade-regulatoria, caderno-procedimentos, casos-aplicacao.  
**Formato esperado:** Markdown estruturado com `# Título`, `## Seção`, tabelas.

```
Entrada:  content_markdown (str), filename (str), metadata (dict)
Saída:    caminho do arquivo PDF gerado
```

---

## `generate_docx` — Geração de Word (.docx)

**Arquivo:** `docx_generator.py`  
**Quando usar:** Containers que serão editados ou complementados manualmente após entrega: caderno-procedimentos, inventario-normas, repositorio-referencias.

```
Entrada:  content_markdown (str), filename (str), template (str, opcional)
Saída:    caminho do arquivo .docx gerado
```

---

## `generate_xlsx` — Geração de planilha Excel (.xlsx)

**Arquivo:** `xlsx_generator.py`  
**Quando usar:** Containers tabulares com múltiplas colunas e fontes: tabela-comparativa, planilha-dados-brutos, mapa-fornecedores, catalogo-solucoes.

```
Entrada:  data (list[dict] ou dict de sheets), filename (str)
Saída:    caminho do arquivo .xlsx gerado
```

---

## Decisão de ferramenta por container

| Container | Formato recomendado | Ferramenta |
|---|---|---|
| ficha-tecnica | PDF | generate_pdf |
| tabela-comparativa | XLSX | generate_xlsx |
| catalogo-solucoes | XLSX | generate_xlsx |
| inventario-normas | DOCX ou PDF | generate_docx / generate_pdf |
| repositorio-referencias | DOCX | generate_docx |
| planilha-dados-brutos | XLSX | generate_xlsx |
| mapa-fornecedores | XLSX | generate_xlsx |
| dossier-interface | PDF | generate_pdf |
| registro-ensaios | PDF ou XLSX | generate_pdf / generate_xlsx |
| caderno-procedimentos | PDF | generate_pdf |
| conformidade-regulatoria | PDF | generate_pdf |
| dossie-tecnico-tdp | PDF | generate_pdf |
| registro-conflitos | XLSX | generate_xlsx |
