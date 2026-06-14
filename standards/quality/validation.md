# Critérios de Validação — Supervisor Automaturge

O Supervisor usa este documento como base para avaliar outputs do Executor.
A validação é feita em **duas dimensões independentes**: Formato e Conteúdo.

---

## Dimensão 1 — Validação de Formato

O Supervisor verifica se o container entregue corresponde ao especificado no `validation_brief` ANTES de avaliar o conteúdo.
Se o formato estiver errado, retorna ao Executor com feedback de formato apenas.

### Checklist de Formato por Container

**ficha-tecnica / dossier-interface / conformidade-regulatoria:**
- [ ] Cabeçalho de identificação completo (fabricante + modelo + revisão + data de coleta)
- [ ] Tabela com colunas: Campo, Valor, Unidade, Fonte (ref), Estado
- [ ] Seção de fontes presente com URL e data de acesso
- [ ] Nenhuma célula em branco — `NULL-MISSING` ou valor

**tabela-comparativa:**
- [ ] Cabeçalho de coluna com fabricante + modelo + versão de cada item
- [ ] Toda célula numérica com unidade e referência
- [ ] Sem coluna de ranking ou recomendação
- [ ] Rodapé de fontes numeradas presente

**catalogo-solucoes:**
- [ ] Critérios de inclusão declarados no cabeçalho
- [ ] Data de consulta em cada entrada
- [ ] Status comercial verificado com data

**inventario-normas:**
- [ ] Escopo de cada norma é transcrição literal (não paráfrase)
- [ ] Status verificado no catálogo oficial

**planilha-dados-brutos:**
- [ ] Aba "Dados Brutos" sem fórmulas nas células de dado
- [ ] Aba "Metadados" presente
- [ ] Unidades nos cabeçalhos de colunas numéricas

**registro-ensaios:**
- [ ] Método de ensaio declarado (norma ou procedimento)
- [ ] Condições do ensaio completas
- [ ] Resultados como medições, não como conclusões

**registro-conflitos:**
- [ ] Toda entrada tem ID (RC-XXX)
- [ ] Conflitos têm dois valores com fontes individuais
- [ ] Campo "Resolução" vazio (não preenchido pela IA)

**repositorio-referencias:**
- [ ] Data de acesso em toda entrada
- [ ] Fontes consultadas sem resultado listadas com status `Não encontrado`

---

## Dimensão 2 — Validação de Conteúdo

### Critérios universais (toda coleta)

1. **Rastreabilidade:** Todo valor numérico ou afirmação técnica tem referência de fonte
2. **Unidades:** Toda grandeza numérica tem unidade explícita
3. **Completude declarada:** Campos ausentes estão como `NULL-MISSING`, não omitidos
4. **Sem alucinação:** Parâmetros numéricos de componentes não devem existir sem fonte verificável
5. **Conflitos preservados:** Divergência entre fontes = ambos os valores registrados + entrada em `registro-conflitos`
6. **Sem resolução de conflitos:** A IA não escolhe entre valores conflitantes

### Critérios específicos por tipo de dado

**parametros-componente:**
- Convenção de referência declarada (ex: DH de Craig) quando parâmetros DH presentes
- Condições de payload especificadas (postura, distância do CG)
- Versão do datasheet registrada

**normas-regulamentacoes:**
- Escopo transcrito literalmente — sem interpretação de requisitos

**desempenho-ensaio / registro-ensaios:**
- Método de medição declarado
- Condições de ensaio suficientes para reprodutibilidade

**dados-seguranca-funcionais:**
- PL/SIL referenciados a funções específicas, não ao produto como um todo
- Nenhum valor de segurança inferido — apenas documentado

**conformidade-certificados / conformidade-regulatoria:**
- Nenhuma conformidade inferida sem certificado documentado
- Lacunas listadas explicitamente

---

## Protocolo de retry

### Retry por falha de formato
```
STATUS: retry_format
CONTAINER ESPERADO: [nome do container]
PROBLEMAS ENCONTRADOS: [lista específica]
CONTEÚDO: [adequado/parcialmente adequado/inadequado]
INSTRUÇÃO: Reformatar preservando os dados já corretos.
```

### Retry por falha de conteúdo (formato OK)
```
STATUS: retry_content
FORMATO: Aprovado ✓ (não alterar)
PROBLEMAS DE CONTEÚDO: [lista específica com localização no documento]
INSTRUÇÃO: Corrigir apenas os problemas listados, mantendo o formato e o conteúdo já correto.
```

### Escalação para Gabriel
Após 2 tentativas sem aprovação, ou quando:
- Dado não pode ser encontrado em nenhuma fonte acessível
- Existe contradição irresolvível entre fontes primárias (→ `registro-conflitos` + escalação)
- A tarefa exige decisão de escopo que ultrapassa a capacidade do pipeline

---

## Score de aprovação por nível de maturidade

O score mínimo de aprovação varia conforme o `maturity_target` declarado no `execution_brief`. Ver `standards/core/maturity-levels.md` para a definição completa de cada nível.

| Nível de maturidade | Score mínimo | Decisão abaixo do mínimo |
|---|---|---|
| `exploratory` | 0.50 | Retry ou escalação |
| `documented` | 0.70 | Retry com feedback específico |
| `verified` | 0.85 | Retry (busca adicional + 2ª fonte) |
| `measured` | 0.90 | Retry (método + condições incompletos) |
| `validated` | N/A | Revisão humana obrigatória |

**Regra padrão:** quando `maturity_target` não estiver declarado, usar limiar de `documented` (0.70).

### Tabela de decisão (independente do nível)

| Score | Decisão |
|---|---|
| ≥ limiar do nível | Aprovado → Google Drive |
| limiar − 0.15 até limiar | Retry com feedback específico |
| < limiar − 0.15 | Escalação para Gabriel |
