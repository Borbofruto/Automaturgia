# Pipeline — Setup e Operação

Este diretório contém o workflow n8n que orquestra a execução da Automaturgia de ponta a ponta: da tarefa no ClickUp ao dossiê no Google Drive.

---

## Fluxo completo

```
ClickUp (status → Processando)
  ↓
Extrair tags (tipo_dado + container)
  ↓
Buscar templates e prompts no GitHub
  ↓
Ordenador → execution_brief + validation_brief
  ↓
Serper → resultados de busca
  ↓
Executor (tentativa 1) → output
  ↓
Supervisor (tentativa 1) → validação
  ├── Aprovado → Preparar Documento → Google Drive → ClickUp "Concluído"
  ├── Escalar  → ClickUp "Revisão Humana" + comentário
  └── Retry    → Executor (tentativa 2) → Supervisor (tentativa 2)
                   ├── Aprovado → Google Drive → ClickUp "Concluído"
                   └── Reprovado → ClickUp "Revisão Humana" + comentário
```

---

## 1. Variáveis de ambiente no n8n

Configure as seguintes variáveis em **Settings → Environment Variables** do n8n (ou no arquivo `.env` da instância):

| Variável | Valor |
|---|---|
| `OPENROUTER_API_KEY` | Sua chave da API do OpenRouter |
| `SERPER_API_KEY` | Sua chave da API do Serper.dev (opcional, mas recomendado) |

> **Sem `SERPER_API_KEY`:** o workflow funciona, mas os agentes recebem resultados de busca vazios. Use apenas para testes.

---

## 2. Credenciais no n8n

Crie as seguintes credenciais em **Credentials** do n8n antes de importar o workflow:

### ClickUp API
- Tipo: `ClickUp API`
- API Key: obtenha em ClickUp → Perfil → Apps → API Token
- Após criar, anote o **ID da credencial** e substitua `CREDENTIAL_CLICKUP_ID` no `workflow.json`

### Google Drive OAuth2
- Tipo: `Google Drive OAuth2 API`
- Configure via Google Cloud Console (OAuth 2.0, escopo Drive)
- Após criar, anote o **ID da credencial** e substitua `CREDENTIAL_GDRIVE_ID` no `workflow.json`

---

## 3. Google Drive — estrutura de pastas

Crie a seguinte estrutura no Google Drive:

```
Automaturgia/
  Dossiês/          ← outputs do pipeline (arquivos .md)
```

Após criar a pasta **Dossiês**:
1. Abra a pasta no Google Drive
2. Copie o ID da URL: `drive.google.com/drive/folders/`**`ESTE_É_O_ID`**
3. Substitua `GDRIVE_FOLDER_ID_DOSSIES` no `workflow.json`

> Os arquivos são enviados como `.md` (Markdown). O Google Drive abre `.md` como texto simples; converta manualmente para Google Doc se quiser editar com formatação. Para PDF/DOCX/XLSX, use os scripts em `/tools/` após o download.

---

## 4. ClickUp — configuração

### Status da lista de tarefas

Crie os seguintes status na lista onde ficam as tarefas de pesquisa:

| Status | Cor sugerida | Uso |
|---|---|---|
| `Pendente` | Cinza | Tarefa criada, aguardando processamento |
| `Processando` | Azul | **Dispara o pipeline** ao ser atribuído |
| `Concluído` | Verde | Pipeline aprovado e dossiê entregue |
| `Revisão Humana` | Laranja | Pipeline escalou — requer intervenção |
| `Reprocessando` | Roxo | Após revisão humana, reenviar para pipeline |

### Tags — dimensão 1: tipo_dado

Crie as seguintes tags na área de trabalho do ClickUp:

`parametros-componente` · `interfaces-compatibilidade` · `software-firmware` · `dados-geometricos` · `normas-regulamentacoes` · `desempenho-ensaio` · `conformidade-certificados` · `solucoes-mercado` · `fornecedores-integradores` · `casos-aplicacao` · `processos-procedimentos` · `literatura-tecnica` · `dados-layout-infraestrutura` · `dados-seguranca-funcionais` · `dados-conectividade-comunicacao` · `modelos-interoperabilidade`

### Tags — dimensão 2: container

`ficha-tecnica` · `tabela-comparativa` · `catalogo-solucoes` · `inventario-normas` · `repositorio-referencias` · `planilha-dados-brutos` · `mapa-fornecedores` · `dossier-interface` · `registro-ensaios` · `caderno-procedimentos` · `conformidade-regulatoria` · `dossie-tecnico-tdp` · `evidence-pack`

> **Importante:** cada tarefa de pesquisa deve ter exatamente **uma tag de cada dimensão**. O pipeline rejeita tarefas sem as duas tags.

### Como criar uma tarefa de pesquisa

1. Criar tarefa na lista de pesquisa
2. Escrever a descrição em linguagem natural: objetivo, componente ou sistema alvo, contexto do projeto
3. Adicionar a tag de `tipo_dado` correspondente
4. Adicionar a tag de `container` correspondente
5. Mudar o status para **Processando**

O pipeline dispara automaticamente.

---

## 5. Importar o workflow no n8n

1. No n8n, vá em **Workflows → Import**
2. Faça upload do arquivo `workflow.json` deste diretório
3. Após importar:
   - Abra o nó **ClickUp — Trigger** e selecione a credencial ClickUp criada
   - Abra o nó **Upload Google Drive** e selecione a credencial Google Drive criada
   - Repita para os demais nós ClickUp (`ClickUp Concluido`, `Comentario Aprovacao`, `ClickUp Revisao Humana`, `Comentario Escalada`)
4. Ative o workflow com o toggle no canto superior direito

---

## 6. Ajustes pós-importação recomendados

### Modelo do Supervisor com thinking
O prompt do Supervisor especifica `thinking: high`. Dependendo da versão do Gemini Flash disponível no OpenRouter, pode ser necessário ajustar o parâmetro no nó **Chamar Supervisor 1** e **Chamar Supervisor 2**:

```json
"thinking": { "type": "enabled", "budget_tokens": 2048 }
```

Adicione este campo ao body JSON dos nós de Supervisor se o modelo suportar.

### Repositório privado
Se o repositório do GitHub estiver privado, adicione um header de autenticação nos nós do tipo `Buscar Recursos`:

```
Authorization: token SEU_GITHUB_TOKEN
```

---

## 7. Testar o pipeline

Para o primeiro teste, recomenda-se uma tarefa simples e bem documentada:

- **Descrição:** "Coletar especificações técnicas do cobot UR10e: payload, alcance, peso, grau de proteção IP e temperatura de operação."
- **Tags:** `parametros-componente` + `ficha-tecnica`
- **Status:** Processando

Acompanhe a execução em n8n → **Executions**. Se o pipeline escalar ou falhar, o log de execução mostra em qual nó ocorreu o erro.
