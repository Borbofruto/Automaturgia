# DEPRECIADO: `materiais-produto-embalagem`

> Este arquivo foi depreciado. Arquivos de tipo de dado domain-specific não pertencem em `standards/data-types/`.
>
> **Use no lugar:** `parametros-componente` para as características físicas e de superfície do produto/embalagem como objeto a ser manipulado. O Ordenador determina os campos relevantes para o contexto (dimensões, massa, material de superfície, permeabilidade ao ar, etc.) com base na tarefa.
>
> Execute `git rm standards/data-types/materiais-produto-embalagem.md` para remover este arquivo do repositório.

## Descrição

Características físicas e de superfície dos produtos e embalagens que serão manipulados pela garra de vácuo. Determina as restrições de aplicação da ventosa e do sistema de vácuo. Não inclui dados de layout (ver `dados-layout-infraestrutura`) nem parâmetros da ventosa em si (ver `parametros-ventosa`).

---

## Campos a coletar

### Identificação do item

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| descricao_item | Descrição do produto ou embalagem (ex: "caixa de papelão ondulado B-flute 20L") | — | confirmado |
| tipo_embalagem | Caixa de papelão / saco / bandeja / fardo / produto sem embalagem / etc. | — | confirmado |
| fabricante_embalagem | Fabricante da embalagem (se aplicável) | — | confirmado / nao-aplicavel |
| referencia_comercial | Referência ou SKU do produto/embalagem | — | confirmado / nao-verificavel |

### Geometria

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| comprimento | Comprimento nominal | mm | confirmado |
| largura | Largura nominal | mm | confirmado |
| altura | Altura nominal | mm | confirmado |
| variacao_dimensional | Variação dimensional esperada em produção (tolerância) | ±mm | confirmado / nao-verificavel |
| forma | Regular (paralelepípedo) / irregular / deformável | — | confirmado |

### Massa

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| massa_nominal | Massa nominal do item (cheio ou no estado de manipulação) | kg | confirmado |
| variacao_massa | Variação de massa esperada | ±kg / % | confirmado / nao-verificavel |
| centro_massa | Posição do centro de massa (distância do fundo) | mm | confirmado / nao-verificavel |

### Superfície de contato

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| material_superficie | Material da superfície de contato com a ventosa | — | confirmado |
| acabamento_superficie | Liso / texturizado / ondulado / microporoso / impresso / envernizado | — | confirmado |
| rugosidade | Rugosidade superficial (Ra) se disponível | μm | confirmado / nao-verificavel |
| permeabilidade_ar | Superfície porosa ao ar? (papel kraft não envernizado, saco de ráfia, etc.) | booleano | confirmado |
| area_disponivel_contato | Área de superfície disponível para posicionamento de ventosas | mm² | confirmado / nao-verificavel |
| obstrucoes_superficie | Costuras, relevos, impressões ou abas que limitam posicionamento | — | confirmado / nao-aplicavel |

### Integridade estrutural

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| rigidez | Rígido / semi-rígido / flexível / mole | — | confirmado |
| deformacao_admissivel | Deformação máxima admissível sob carga da ventosa | mm | confirmado / nao-verificavel |
| resistencia_compressao | Resistência à compressão (BCT se papelão) | N | confirmado / nao-verificavel |
| sensibilidade_umidade | A embalagem perde resistência com umidade? | booleano | confirmado |
| temperatura_produto | Temperatura do produto no momento da manipulação | °C | confirmado |

### Restrições e certificações

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| contato_alimentar | Produto está em contato com alimentos? | booleano | confirmado |
| material_contaminante | Há óleos, resíduos, pós ou umidade na superfície? | — | confirmado / nao-aplicavel |
| restricao_marcas | Ventosa não pode deixar marcas visíveis? | booleano | confirmado |

---

## Fontes válidas

- Especificação técnica do produto (fornecida pelo cliente ou fabricante do produto)
- Ficha técnica da embalagem (fornecida pelo fabricante da embalagem)
- Medição direta com instrumentos calibrados (paquímetro, balança) — registrar instrumento e data
- Normas de embalagem aplicáveis (ex: ABNT NBR 6737 para caixas de papelão)

---

## Fontes inválidas

- Estimativas visuais sem medição
- Valores de produto similar sem confirmação para o SKU específico
- Informações de catálogo de vendas (dimensões de marketing podem diferir das dimensões reais)

---

## Regras de qualidade

1. `massa_nominal` deve ser a massa no estado real de manipulação — produto cheio, embalagem fechada, na temperatura de processo.
2. `permeabilidade_ar` é crítica para seleção de ventosa — deve ser confirmada, não estimada pelo material.
3. Se o produto tem variações de SKU com dimensões diferentes, cada SKU é um registro separado.
4. `restricao_marcas` = `true` implica restrição de material de lábio da ventosa — registrar esta implicação na seção de notas.
5. Resistência a compressão de papelão (BCT): declarar condições de temperatura e umidade relativa do ensaio.

---

## Armadilhas comuns

- **Dimensões de catálogo ≠ dimensões reais:** Caixas de papelão têm tolerâncias dimensionais significativas (±2-5mm). Medir amostra real.
- **Papelão reciclado vs virgem:** BCT e permeabilidade diferem. Especificar se o fornecedor usa material reciclado.
- **Superfícies envernizadas:** Verniz UV pode parecer liso e impermeável, mas ventosas de NBR podem ter aderência diferente de ventosas de silicone. Não assumir.
- **Temperatura:** Produto congelado tem comportamento de superfície diferente do produto à temperatura ambiente. Campo temperatura_produto é crítico.
