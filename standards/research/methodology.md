# Metodologia de Pesquisa Técnica — Automaturge

Este documento define o processo padrão para tarefas de pesquisa técnica em robótica industrial.
Todo Executor deve seguir este fluxo, adaptando a profundidade conforme o escopo da tarefa.

---

## 1. Princípio fundamental

**Dados de primeiros princípios, não de benchmarks genéricos.**

Parâmetros técnicos (DH, payload, inércia, ciclo, etc.) devem ser rastreados até:
- Datasheets e manuais do fabricante (primeira escolha)
- Literatura acadêmica com metodologia rastreável (segunda escolha)
- Análise derivada a partir de parâmetros conhecidos (terceira escolha, documentar explicitamente)

Nunca usar valores de integradores, revendedores ou comparativos de mercado sem rastrear a origem primária.

---

## 2. Fases da pesquisa

### Fase 1 — Definição do objeto
- Identificar claramente o que está sendo medido/levantado
- Especificar as condições de validade (ex: payload nominal, temperatura, configuração de montagem)
- Listar o que é necessário vs. o que é desejável

### Fase 2 — Levantamento de fontes
- Buscar fontes primárias: datasheets, manuais técnicos, papers IEEE/Robotics
- Registrar URL ou referência de cada fonte consultada
- Datar a consulta (dados de robôs podem ser atualizados por firmware)

### Fase 3 — Extração e estruturação
- Extrair apenas os dados relevantes para o escopo
- Estruturar em formato tabular quando possível
- Preservar unidades originais + conversão quando necessário
- Sinalizar lacunas: campos não encontrados devem aparecer como `N/D (não encontrado)` — nunca omitir

### Fase 4 — Validação cruzada
- Verificar consistência entre fontes diferentes
- Identificar contradições e documentá-las explicitamente
- Para parâmetros críticos (DH, payload, inércia), buscar mínimo 2 fontes independentes

### Fase 5 — Entrega
- Formato conforme definido pelo Ordenador (ver `/standards/documents/formats.md`)
- Incluir seção "Fontes e Rastreabilidade" em todo documento
- Incluir seção "Limitações e Incertezas" quando houver dados incompletos

---

## 3. Critérios de confiança por tipo de dado

| Tipo de dado | Fonte aceitável | Fonte não aceitável |
|---|---|---|
| Parâmetros DH | Datasheet fabricante, paper com derivação | Blog, fórum, vídeo |
| Payload / inércia | Manual técnico oficial | Comparativo de mercado |
| Ciclo de trabalho | Paper com setup documentado | Estimativa de integrador |
| Envelope de trabalho | CAD oficial, datasheet | Print de site comercial |
| Parâmetros de segurança | ISO 10218 / ISO/TS 15066 | Especificação de produto |

---

## 4. Template de referência bibliográfica

```
[N] Autor(es). "Título do trabalho". Publicação/Fabricante, Ano.
    Disponível em: <URL>. Acesso em: DD/MM/AAAA.
    Dado extraído: [descrição do dado específico utilizado]
    Confiança: Alta / Média / Baixa
    Motivo da confiança: [justificativa]
```

---

## 5. Flags de qualidade

O Executor deve sinalizar no output final quando:

- `[ESTIMADO]` — valor calculado ou estimado, não medido diretamente
- `[ÚNICO FONTE]` — apenas uma fonte encontrada, validação cruzada não foi possível
- `[DATA ANTIGA]` — fonte com mais de 3 anos, verificar versão atual
- `[CONFLITO]` — múltiplas fontes com valores diferentes, ambos documentados
