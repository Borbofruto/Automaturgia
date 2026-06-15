# Contrato de Ferramenta: `generate_docx`

## Descrição

Converte conteúdo Markdown estruturado em arquivo Word (.docx) e o armazena no destino especificado. Usado quando o container alvo requer formato editável para revisão humana.

---

## Input

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `content` | string | sim | Conteúdo em Markdown (suporta tabelas, listas, cabeçalhos, código) |
| `filename` | string | sim | Nome do arquivo de saída (sem extensão — .docx adicionado automaticamente) |
| `destination` | string | sim | Caminho de destino (Google Drive path ou pasta local mapeada) |
| `title` | string | não | Título para propriedades do documento |
| `author` | string | não | Autor para propriedades (padrão: "Automaturgia") |

---

## Output

```json
{
  "status": "success | error",
  "file_path": "/caminho/completo/arquivo.docx",
  "file_size_kb": 128,
  "error_message": null
}
```

---

## Modos de falha

| Condição | Comportamento esperado |
|---|---|
| Markdown inválido | Erro com linha problemática — Executor corrige e retry |
| Destino inacessível | Erro de permissão — escalar para Gabriel |
| Tabela com mais de 10 colunas | Gerado com aviso — verificar formatação no output |
| Timeout (>60s) | Retry uma vez; se persistir, escalar |

---

## Ambiente

- Disponível em: n8n via nó de geração de DOCX
- Biblioteca: configurável (Pandoc, python-docx, etc.) — ver configuração n8n
- Suporte a Markdown: tabelas GFM, cabeçalhos, listas, blocos de código (como texto monoespaçado)
- **Não suporta:** fórmulas, macros, controles de formulário, conteúdo vinculado

---

## Chamadores permitidos

| Agente | Uso permitido |
|---|---|
| Executor | Sim |
| Ordenador | Não |
| Supervisor | Não |

---

## Destino do output

Arquivo DOCX gravado em:
- Google Drive: `/Automaturgia/Execuções/[AAAA-MM]/[task-id]/`
- Nome padrão: `[container]_[task-id]_[AAAAMMDD].docx`

---

## Quando usar DOCX vs PDF

| Situação | Formato recomendado |
|---|---|
| Container para revisão e edição humana | DOCX |
| Container final/arquivado sem edição esperada | PDF |
| evidence-pack | PDF (registro imutável) |
| `caderno-procedimentos` ou `registro-ensaios` para revisão | DOCX |
| `ficha-tecnica` para entrega final | PDF |

O `output_format` no `execution_brief` é a fonte de verdade — o Executor não escolhe o formato por conta própria.
