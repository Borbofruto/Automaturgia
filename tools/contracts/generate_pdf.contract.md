# Contrato de Ferramenta: `generate_pdf`

## Descrição

Converte conteúdo Markdown estruturado em arquivo PDF formatado e o armazena no destino especificado.

---

## Input

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `content` | string | sim | Conteúdo em Markdown (suporta tabelas, listas, cabeçalhos, código) |
| `filename` | string | sim | Nome do arquivo de saída (sem extensão — .pdf adicionado automaticamente) |
| `destination` | string | sim | Caminho de destino (Google Drive path ou pasta local mapeada) |
| `title` | string | não | Título do documento para metadados do PDF |
| `author` | string | não | Autor para metadados (padrão: "Automaturge") |

---

## Output

```json
{
  "status": "success | error",
  "file_path": "/caminho/completo/arquivo.pdf",
  "file_size_kb": 245,
  "pages": 4,
  "error_message": null
}
```

---

## Modos de falha

| Condição | Comportamento esperado |
|---|---|
| Markdown inválido / mal-formado | Erro com linha problemática — Executor corrige e retry |
| Destino inacessível | Erro de permissão — escalar para Gabriel |
| Tabela muito larga para a página | PDF gerado com aviso — Executor verifica output e ajusta formatação se necessário |
| Conteúdo vazio (`content: ""`) | Erro — Executor nunca deve chamar com conteúdo vazio |
| Timeout (>60s para documentos grandes) | Erro — retry uma vez; se persistir, escalar |

---

## Ambiente

- Disponível em: n8n via nó de geração de PDF
- Biblioteca: configurável (WeasyPrint, Pandoc+LaTeX, etc.) — ver configuração n8n
- Suporte a Markdown: tabelas GFM, blocos de código, cabeçalhos H1-H6, listas ordenadas e não-ordenadas
- **Não suporta:** equações LaTeX inline, imagens sem URL pública, HTML arbitrário

---

## Chamadores permitidos

| Agente | Uso permitido |
|---|---|
| Executor | Sim — geração dos containers e evidence-packs |
| Ordenador | Não |
| Supervisor | Não |

---

## Destino do output

Arquivo PDF gravado em:
- Google Drive: `/Automaturge/Execuções/[AAAA-MM]/[task-id]/`
- Nome padrão: `[container]_[task-id]_[AAAAMMDD].pdf`

O `file_path` retornado deve ser registrado no cabeçalho do evidence-pack.

---

## Notas de uso para o Executor

1. O Executor valida que `content` está completo antes de chamar esta ferramenta — nunca gerar PDF parcial.
2. Se o container alvo for `evidence-pack`, o PDF deve incluir todas as 7 seções obrigatórias.
3. Tabelas muito largas: preferir orientação paisagem ou quebrar em subtabelas — verificar o parâmetro de layout disponível no nó n8n.
4. Nomenclatura do arquivo deve seguir o padrão `[container]_[task-id]_[AAAAMMDD]` sem espaços ou caracteres especiais.
