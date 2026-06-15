# Níveis de Maturidade — Automaturgia

Todo pacote de evidências produzido pela Automaturgia recebe um nível de maturidade declarado. O nível determina o que o Supervisor aceita como aprovado e como o pacote deve ser interpretado por quem o usa.

O nível não é uma nota — é uma declaração do estado real dos dados.

---

## Níveis

### `exploratory` — Exploratório
Coleta inicial em campo com fontes escassas, acesso limitado ou dados inconsistentes. Muitos campos `NULL-MISSING` são esperados. O valor é mapear o que existe e o que falta.

**Critério de aprovação:** fontes consultadas documentadas, campos ausentes declarados, nenhuma estimativa não sinalizada.  
**Score mínimo do Supervisor:** 0.50

---

### `documented` — Documentado
Dados coletados de fontes válidas com rastreabilidade completa. Maioria dos campos obrigatórios preenchida. Conflitos identificados e registrados. Ausências declaradas como `NULL-MISSING`.

**Critério de aprovação:** ≥ 70% dos campos obrigatórios com fonte + unidade + estado.  
**Score mínimo do Supervisor:** 0.70

---

### `verified` — Verificado
Dados confirmados por mínimo de duas fontes independentes para campos críticos. Conflitos resolvidos (por humano) ou escalados. Ausências são genuínas, não falta de busca.

**Critério de aprovação:** campos críticos com ≥ 2 fontes, sem `nao-verificavel` em dados de segurança.  
**Score mínimo do Supervisor:** 0.85

---

### `measured` — Medido
Dados obtidos por ensaio documentado com método, condições e instrumento declarados. Fonte primária é resultado de medição, não declaração de fabricante.

**Critério de aprovação:** todo valor numérico crítico com método + condições + instrumento. Nenhum valor de datasheet como substituto de medição.  
**Score mínimo do Supervisor:** 0.90

---

### `validated` — Validado
Dados verificados e medidos, revisados por especialista humano, com declaração explícita de adequação ao contexto de uso. Nível máximo — requer intervenção humana no processo.

**Critério de aprovação:** revisão humana registrada + aprovação explícita no dossier.  
**Score mínimo do Supervisor:** N/A (aprovação humana supera score automático)

---

## Como o Ordenador declara o nível

O Ordenador inclui `maturity_target` no `execution_brief`:

```json
"maturity_target": "documented"
```

O Executor produz o pacote com esse nível como alvo.  
O Supervisor avalia usando o score mínimo correspondente — não o limiar universal de 0.90.

---

## Como o Supervisor reporta o nível alcançado

O Supervisor inclui no JSON de resposta:

```json
"maturity_achieved": "documented",
"maturity_target": "verified",
"maturity_gap": "Campos X e Y têm fonte única; Z está NULL-MISSING após 2 fontes consultadas"
```

Se `maturity_achieved` ≥ `maturity_target`: `overall_approved = true`.  
Se `maturity_achieved` < `maturity_target`: `recommended_action = retry_content` com instruções específicas.
