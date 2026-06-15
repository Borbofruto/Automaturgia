# Contrato de Ferramenta: `generate_xlsx`

## Descrição

Gera arquivo Excel (.xlsx) a partir de dados estruturados. Usado principalmente para containers que envolvem comparações tabulares, dados brutos de ensaio ou inventários com múltiplas entradas.

---

## Input

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `sheets` | array | sim | Lista de abas a criar (ver estrutura abaixo) |
| `filename` | string | sim | Nome do arquivo (sem extensão — .xlsx adicionado automaticamente) |
| `destination` | string | sim | Caminho de destino |

**Estrutura de cada sheet:**

```json
{
  "name": "Nome da Aba",
  "headers": ["Coluna 1", "Coluna 2", "Coluna 3"],
  "rows": [
    ["valor1", "valor2", "valor3"],
    ["valor4", "valor5", "valor6"]
  ],
  "freeze_header": true
}
```

---

## Output

```json
{
  "status": "success | error",
  "file_path": "/caminho/completo/arquivo.xlsx",
  "file_size_kb": 85,
  "sheets_created": ["Dados", "Metadados", "Conflitos"],
  "error_message": null
}
```

---

## Modos de falha

| Condição | Comportamento esperado |
|---|---|
| `sheets` vazio | Erro — Executor nunca chama com sheets vazio |
| Nome de aba duplicado | Erro — nomes de aba devem ser únicos |
| Linha com número diferente de colunas dos headers | Erro — Executor valida antes de chamar |
| Destino inacessível | Erro de permissão — escalar para Gabriel |
| Timeout (>60s para planilhas grandes) | Retry uma vez; se persistir, escalar |

---

## Ambiente

- Disponível em: n8n via nó de geração de XLSX
- Biblioteca: configurável (openpyxl, ExcelJS, etc.) — ver configuração n8n
- **Não suporta:** fórmulas dinâmicas, macros, tabelas dinâmicas, gráficos embutidos
- Suporte a tipos: texto, números, datas (formato ISO), booleanos

---

## Chamadores permitidos

| Agente | Uso permitido |
|---|---|
| Executor | Sim |
| Ordenador | Não |
| Supervisor | Não |

---

## Containers que tipicamente usam XLSX

| Container | Estrutura de abas esperada |
|---|---|
| `planilha-dados-brutos` | Aba 1: Dados brutos; Aba 2: Metadados; Aba 3: Derivados (se houver) |
| `tabela-comparativa` | Aba 1: Comparação; Aba 2: Fontes |
| `inventario-normas` | Aba 1: Inventário; Aba 2: Escopo |
| `catalogo-solucoes` | Aba 1: Catálogo; Aba 2: Critérios de inclusão |

---

## Destino do output

Arquivo XLSX gravado em:
- Google Drive: `/Automaturgia/Execuções/[AAAA-MM]/[task-id]/`
- Nome padrão: `[container]_[task-id]_[AAAAMMDD].xlsx`

---

## Notas de uso para o Executor

1. Separar sempre dados de metadados em abas distintas — nunca misturar valores técnicos com rastreabilidade na mesma aba.
2. Linha de cabeçalho deve refletir exatamente os campos obrigatórios do template do container.
3. Valores `NULL-MISSING` devem aparecer como a string `"NULL-MISSING"` na célula — não como célula vazia.
4. Conflitos: se o container é `tabela-comparativa`, incluir aba separada "Conflitos" com as entradas do `registro-conflitos`.
5. Números: usar ponto como separador decimal nos valores (independente do locale) — o n8n converte conforme configuração regional do destino.
