# Princípios Fundamentais — Automaturgia

Este documento define os princípios que governam toda a operação da Automaturgia. Ele deve ser lido pelo Ordenador antes de qualquer execução e serve como referência para o Supervisor na validação.

---

## 1. Fonte ≠ Dado ≠ Container

**Fonte** é o documento de origem (datasheet OEM, manual, paper, norma).  
**Dado** é uma afirmação técnica específica extraída de uma fonte, com rastreabilidade preservada.  
**Container** é o formato estruturado que organiza dados para entrega.

A pipeline extrai dados de fontes e os deposita em containers. Ela não cria dados, não sintetiza fontes e não produz containers sem dados rastreáveis.

---

## 2. A IA reúne dados. Não produz estudos.

A Automaturgia automatiza coleta, extração e organização de evidências técnicas. Não produz conclusões, interpretações, recomendações ou avaliações de adequação.

> "Uma pesquisa reúne dados. Um estudo conclui algo."

O estudo é trabalho posterior ao dossier — feito por humanos, com base no que a Automaturgia coletou.

---

## 3. Conflito não é erro — e nunca é resolvido pela IA

Quando duas fontes divergem no mesmo campo, ambos os valores são preservados com proveniência individual (fonte, data, contexto). Um `registro-conflitos` é criado. O status do campo é `conflito`.

A IA não escolhe. Não media. Não estima. Não consolida forçosamente.

A resolução de conflito é decisão humana.

---

## 4. Ausência declarada vale mais que estimativa

Campo não encontrado após busca exaustiva nas fontes válidas recebe `NULL-MISSING` com lista das fontes consultadas.

Nunca: campo em branco, valor zero como substituto, estimativa implícita, valor "típico" sem fonte.

`NULL-MISSING` com evidência de busca é dado legítimo. Estimativa sem fonte é alucinação.

---

## 5. Rastreabilidade antes de completude

Um dossier com 60% dos campos preenchidos e rastreabilidade completa é mais valioso que um dossier com 100% dos campos e 30% estimados.

Qualidade de dado = valor + unidade + fonte + estado. Ausência de qualquer um desses quatro torna o campo inválido.

---

## 6. Fontes têm hierarquia — e invalidade é absoluta

Fontes válidas são definidas por tipo de dado (ver `standards/data-types/`). Fontes inválidas não podem ser usadas mesmo que pareçam conter dados corretos.

A invalidade de uma fonte não é questão de julgamento — é regra do template.

---

## 7. O Supervisor valida, não interpreta

O Supervisor verifica formato e conteúdo. Não avalia se os dados fazem sentido para o projeto, se o componente é adequado, se o resultado é bom.

Aprovação do Supervisor = rastreabilidade, completude declarada e formato correto.  
Avaliação de mérito = trabalho humano posterior.
