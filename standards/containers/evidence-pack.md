# Container: `evidence-pack`

## Descrição

O **evidence-pack** é o pacote de saída natural de uma execução da Automaturgia. Ele agrega, em um único container auditável, tudo que foi produzido durante uma corrida: o dossier principal, o repositório de referências, os conflitos identificados, as lacunas declaradas e os metadados de execução.

**Não é um produto para o usuário final** — é o registro completo e rastreável do que aconteceu em uma execução, que pode ser revisado, arquivado ou usado como insumo para execuções subsequentes.

### Distinção crítica: evidence-pack ≠ dossie-tecnico-tdp

| | `evidence-pack` | `dossie-tecnico-tdp` |
|---|---|---|
| **Escopo** | Uma execução da pipeline | Um sistema de produto completo |
| **Origem** | Gerado automaticamente pelo Executor | Consolidado por humano a partir de múltiplas fichas |
| **Conteúdo** | Tudo que foi produzido + metadados de execução | BOM + ponteiros para outros containers |
| **Audiência** | Pipeline + revisão técnica | Equipe de produto |
| **Ciclo de vida** | Imutável após geração | Atualizado conforme o produto evolui |

---

## Estrutura obrigatória

### 1. Cabeçalho de execução

```
# Evidence Pack

**Tarefa:** [ID da tarefa no ClickUp]
**Tipo de dado:** [tipo-dado declarado]
**Container alvo:** [container declarado]
**Nível de maturidade alvo:** [maturity_target]
**Nível de maturidade alcançado:** [maturity_achieved]
**Data de execução:** DD/MM/AAAA HH:MM UTC
**Modelos usados:** Ordenador: [...] | Executor: [...] | Supervisor: [...]
**Score do Supervisor:** [0.0-1.0]
**Status:** approved | retry_content | retry_format | escalated
```

### 2. Dossier principal

O conteúdo do container alvo (ficha-tecnica, tabela-comparativa, etc.) embutido integralmente.

### 3. Repositório de referências

Tabela com todas as fontes consultadas:

| ID | Tipo | Título | URL | Data acesso | Status |
|---|---|---|---|---|---|
| [1] | Datasheet OEM | ... | ... | DD/MM/AAAA | Acessado |
| [2] | Manual | ... | ... | DD/MM/AAAA | Não encontrado |

Inclui fontes que não retornaram dados (com status = "Não encontrado").

### 4. Lacunas declaradas (NULL-MISSING)

Lista de campos não encontrados com evidência de busca:

```
- Campo X: NULL-MISSING — consultado em [1][3][5]
- Campo Y: NULL-MISSING — consultado em [2][4] — nota: fonte inválida excluída conforme template
```

### 5. Registro de conflitos

Se existirem conflitos, tabela completa:

| ID | Campo | Valor A | Fonte A | Valor B | Fonte B | Resolução |
|---|---|---|---|---|---|---|
| RC-001 | ... | ... | [1] | ... | [2] | *(vazio — não resolvido pela IA)* |

Se não houver conflitos: `Nenhum conflito identificado nesta execução.`

### 6. Relatório de validação do Supervisor

O JSON de resposta completo do Supervisor, integralmente preservado.

### 7. Metadados de rastreabilidade

```
**Prompt do Ordenador:** [hash SHA-256 do execution_brief]
**Versão do template tipo-dado:** [data de criação do arquivo em standards/data-types/]
**Versão do template container:** [data de criação do arquivo em standards/containers/]
**n8n Workflow ID:** [ID se disponível]
```

---

## Regras de preenchimento

1. O Executor gera o evidence-pack automaticamente ao final de cada execução — não é preenchido manualmente.
2. O dossier principal deve ser idêntico ao que seria entregue isoladamente — o evidence-pack o envolve, não o substitui.
3. O campo "Resolução" no registro de conflitos permanece vazio. Sem exceção.
4. O relatório do Supervisor é transcrito integralmente, sem edição.
5. Se o status final for `escalated`, incluir no cabeçalho a razão do escalonamento.

---

## O que o Supervisor verifica

O Supervisor não valida o evidence-pack — ele valida o dossier principal dentro dele. O evidence-pack em si é um envelope de rastreabilidade, não um objeto de validação de conteúdo.

**Exceção:** o Supervisor pode ser solicitado a verificar se o evidence-pack está estruturalmente completo (tem todas as 7 seções). Nesse caso, valida formato apenas.

---

## Tipos de dado compatíveis

Todos os tipos de dado (`tipo-dado/*`). O evidence-pack é agnóstico quanto ao conteúdo do dossier que engloba.

---

## Armazenamento

Evidence-packs são armazenados no Google Drive no diretório `/Automaturgia/Execuções/[AAAA-MM]/[task-id]/`.  
Nome padrão: `evidence-pack_[task-id]_[AAAAMMDD].md`
