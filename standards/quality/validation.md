# Critérios de Validação — Supervisor Automaturge

O Supervisor usa este documento como base para avaliar outputs do Executor.
A validação é feita em **duas dimensões independentes**: Formato e Conteúdo.

---

## Dimensão 1 — Validação de Formato

O Supervisor verifica se o arquivo entregue está no formato correto ANTES de avaliar o conteúdo.
Se o formato estiver errado, retorna ao Executor com feedback de formato apenas.

### Checklist de Formato

**PDF:**
- [ ] Arquivo é um PDF válido e abrível
- [ ] Contém as seções obrigatórias (Resumo, Objetivo, Metodologia, Resultados, Fontes)
- [ ] Tabelas têm cabeçalho destacado
- [ ] Rodapé com paginação presente
- [ ] Fórmulas legíveis (não texto puro)

**XLSX:**
- [ ] Arquivo é um .xlsx válido
- [ ] Cabeçalhos presentes na linha correta
- [ ] Unidades incluídas nos cabeçalhos de colunas numéricas
- [ ] Sem células mescladas nos dados (apenas no título)
- [ ] Cabeçalho com fundo escuro visível

**DOCX:**
- [ ] Arquivo é um .docx válido
- [ ] Usa estilos Heading (não negrito manual)
- [ ] Capa presente com título e data
- [ ] Tabelas com estilo "Table Grid"

**Script:**
- [ ] Arquivo tem extensão correta (.py, .js)
- [ ] Docstring presente no topo
- [ ] `if __name__ == "__main__"` presente (Python)
- [ ] Sem credenciais hardcoded

---

## Dimensão 2 — Validação de Conteúdo

### Critérios universais (toda tarefa)

1. **Completude:** Todos os campos/dados solicitados no brief de execução estão presentes
2. **Rastreabilidade:** Fontes citadas para dados factuais (não para análises do próprio modelo)
3. **Unidades:** Toda grandeza numérica tem unidade explícita
4. **Lacunas sinalizadas:** Dados não encontrados estão marcados com `[N/D]`, não omitidos
5. **Sem alucinação:** Dados numéricos críticos (parâmetros de robô, normas) têm fonte rastreável

### Critérios por tipo de conteúdo

**Parâmetros técnicos (DH, cinemática, payload):**
- Todos os graus de liberdade cobertos (nenhum joint faltando)
- Convenção de referência declarada (ex: Craig, Denavit-Hartenberg padrão)
- Unidades consistentes ao longo do documento
- Conflitos entre fontes documentados, não resolvidos arbitrariamente

**Análise metodológica:**
- Hipótese de pesquisa declarada
- Escopo e limitações explícitos
- Conclusões derivadas dos dados apresentados (não afirmações soltas)

**Comparativos / benchmarks:**
- Condições de teste idênticas entre itens comparados (ou diferenças documentadas)
- Valores extremos justificados
- Fonte por linha de dado

**Scripts / código:**
- Executa sem erro no ambiente esperado
- Produz output no formato especificado
- Casos de erro tratados

---

## Protocolo de retry

### Retry por falha de formato
O Supervisor retorna ao Executor com:
```
STATUS: retry_format
FORMATO ESPERADO: [nome do formato]
PROBLEMAS ENCONTRADOS: [lista específica]
CONTEÚDO: O conteúdo gerado estava [adequado/parcialmente adequado/inadequado]
INSTRUÇÃO: Reformatar o conteúdo preservando os dados já corretos.
```

### Retry por falha de conteúdo (formato OK)
O Supervisor retorna ao Executor com:
```
STATUS: retry_content
FORMATO: Aprovado ✓ (não alterar)
PROBLEMAS DE CONTEÚDO: [lista específica com localização no documento]
INSTRUÇÃO: Corrigir apenas os problemas listados, mantendo o formato e o conteúdo já correto.
```

### Escalação para Claude/Gabriel
Após 2 tentativas sem aprovação, ou quando:
- Dado não pode ser encontrado em nenhuma fonte acessível
- Existe contradição irresolvível entre fontes primárias
- A tarefa exige decisão de escopo que ultrapassa a capacidade do pipeline

---

## Score de aprovação

| Score | Decisão |
|---|---|
| 0.90 – 1.00 | Aprovado → Google Drive |
| 0.70 – 0.89 | Retry com feedback específico |
| 0.50 – 0.69 | Retry (pode requerer pesquisa adicional) |
| < 0.50 | Escalação para Claude/Gabriel |
