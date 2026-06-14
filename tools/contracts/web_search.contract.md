# Contrato de Ferramenta: `web_search`

## Descrição

Executa buscas na web e retorna trechos de páginas indexadas. Ferramenta primária do Executor para localizar fontes válidas.

---

## Input

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `query` | string | sim | Query de busca em linguagem natural ou booleana |
| `num_results` | int | não | Número de resultados a retornar (padrão: 5, máx: 10) |
| `lang` | string | não | Idioma preferencial dos resultados (ex: "pt", "en") |

**Restrições:**
- Queries com operadores booleanos (`site:`, `filetype:`, `"..."`) são suportadas
- Queries não devem conter PII do usuário

---

## Output

```json
{
  "results": [
    {
      "title": "Título da página",
      "url": "https://...",
      "snippet": "Trecho relevante da página",
      "date": "YYYY-MM-DD ou null"
    }
  ],
  "total_results_estimate": 1200,
  "query_used": "query exata enviada ao motor"
}
```

**Atenção:** `snippet` é um extrato — não é o conteúdo completo da página. Para conteúdo completo, o Executor deve acessar a URL diretamente (via outra ferramenta se disponível) ou registrar como "verificado via snippet" no `repositorio_referencias`.

---

## Modos de falha

| Código / Condição | Comportamento esperado |
|---|---|
| Sem resultados | `results: []` com `total_results_estimate: 0` — Executor deve variar a query e registrar no `null_missing` |
| Timeout (>30s) | Erro com mensagem — Executor deve registrar a query como "não executada" e escalar se crítico |
| URL bloqueada por paywall | Snippet disponível, conteúdo completo inacessível — registrar como `nao-verificavel` |
| Conteúdo em idioma inesperado | Resultado válido — Executor deve registrar o idioma na referência |

---

## Ambiente

- Disponível em: n8n via nó de busca web (configurar API key no ambiente)
- Provedor: configurável (Serper, Brave Search, etc.) — ver configuração n8n
- Sem acesso a: páginas protegidas por login, conteúdo JavaScript-only sem renderização
- Latência típica: 1-5s por chamada

---

## Chamadores permitidos

| Agente | Uso permitido |
|---|---|
| Executor | Sim — uso primário |
| Ordenador | Não — Ordenador não executa buscas |
| Supervisor | Não — Supervisor não acessa fontes externas |

---

## Destino do output

O output não é armazenado diretamente — o Executor extrai dados dos resultados e os deposita no container alvo. Todas as URLs utilizadas como fonte devem ser registradas no `repositorio_referencias` do evidence-pack.

---

## Notas de uso para o Executor

1. Sempre registrar a query exata usada (campo `query_used`) no `repositorio_referencias`, não apenas a URL.
2. Se um snippet contém um dado técnico crítico mas a página completa está inacessível: registrar o dado com status `nao-verificavel` e fonte = URL + "(trecho de busca, não verificado na íntegra)".
3. Variar queries quando os resultados iniciais não atingem fontes válidas: tentativas com diferentes termos, idiomas e operadores devem ser documentadas.
4. Máximo de 3 queries por campo antes de declarar `NULL-MISSING` (exceto instrução contrária no `execution_brief`).
