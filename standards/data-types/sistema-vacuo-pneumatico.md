# Tipo de Dado: `sistema-vacuo-pneumatico`

## Descrição

Parâmetros do sistema pneumático que alimenta e controla o vácuo nas garras: geradores de vácuo (ejetores, bombas), válvulas, sensores e infraestrutura de linha. Não inclui a ventosa em si (ver `parametros-ventosa`) nem a arquitetura de montagem da garra (ver `arquitetura-garra-vacuo`).

---

## Campos a coletar

### Gerador de vácuo

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| tipo_gerador | Ejetor Venturi / bomba de vácuo dedicada / bomba centralizada | — | confirmado |
| fabricante_gerador | Nome do fabricante OEM do gerador | — | confirmado |
| modelo_gerador | Referência exata do modelo | — | confirmado |
| principio_operacao | Venturi / membrana / palheta / etc. | — | confirmado |
| pressao_entrada_ar | Pressão de entrada de ar comprimido necessária | bar / kPa | confirmado |
| consumo_ar_comprimido | Consumo de ar comprimido (Nl/min) | Nl/min | confirmado |
| vacuo_maximo_alcancavel | Nível máximo de vácuo alcançável | kPa / mbar | confirmado |
| caudal_succao | Caudal de sucção (fluxo de ar aspirado) | Nl/min | confirmado |
| tempo_evacuacao | Tempo de evacuação declarado (condição padrão) | ms | confirmado / nao-verificavel |
| tempo_liberacao | Tempo de liberação (quebra de vácuo) | ms | confirmado / nao-verificavel |
| funcao_soplador | Possui função de sopro para liberação ativa? | booleano | confirmado |

### Válvulas de controle

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| tipo_valvula | Solenoide / proporcional / mecânica | — | confirmado |
| fabricante_valvula | Nome do fabricante | — | confirmado |
| modelo_valvula | Referência exata | — | confirmado |
| tensao_atuacao | Tensão de atuação da solenoide | VDC | confirmado |
| corrente_atuacao | Corrente de atuação | mA | confirmado |
| tempo_comutacao | Tempo de comutação (abertura/fechamento) | ms | confirmado / nao-verificavel |
| funcao_fail_safe | Posição de falha segura (normalmente aberta / normalmente fechada) | — | confirmado |

### Sensores de vácuo

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| tipo_sensor | Pressostato / transmissor analógico / digital IO-Link | — | confirmado |
| fabricante_sensor | Nome do fabricante | — | confirmado |
| modelo_sensor | Referência exata | — | confirmado |
| faixa_medicao | Faixa de medição do sensor | kPa | confirmado |
| saida_sinal | Tipo de sinal de saída (0-10V, 4-20mA, IO-Link, PNP/NPN) | — | confirmado |
| ponto_comutacao_configuravel | Ponto de comutação é configurável? | booleano | confirmado |
| faixa_histerese | Faixa de histerese configurável | kPa | confirmado / nao-verificavel |

### Infraestrutura de linha

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| diametro_tubo_principal | Diâmetro interno do tubo de vácuo principal | mm | confirmado |
| material_tubo | Material do tubo (poliuretano, silicone, etc.) | — | confirmado |
| pressao_maxima_linha | Pressão máxima suportada pela linha | bar | confirmado |
| tipo_conexao_rapida | Tipo de conexão rápida pneumática (push-in, rosca) | — | confirmado |
| filtro_presente | Filtro de linha presente? Tipo e grau de filtração | — | confirmado / nao-aplicavel |

---

## Fontes válidas

- Datasheet oficial do fabricante de cada componente
- Catálogo técnico do fabricante (ejetor, válvula, sensor)
- Manual de instalação e operação do sistema
- Especificações de integração do fornecedor do sistema completo

---

## Fontes inválidas

- Valores calculados a partir de fórmulas sem ensaio documentado
- Manuais de componentes de gerações anteriores aplicados ao modelo atual
- Distribuidores sem documentação OEM

---

## Regras de qualidade

1. Cada componente (gerador, válvula, sensor) é coletado com fabricante + modelo separados — nunca agrupar "sistema de vácuo SMC" sem especificar modelos.
2. `consumo_ar_comprimido` e `vacuo_maximo_alcancavel` dependem da pressão de entrada — registrar a pressão de entrada utilizada para o valor declarado.
3. Tempo de evacuação: especificar volume evacuado nas condições do teste (tamanho de câmara / tubo).
4. `funcao_fail_safe` é crítica para análise de segurança — se não declarado pelo fabricante, marcar `nao-verificavel`, não inferir.
5. Para sistemas integrados (ejetor + válvula em bloco único), registrar tanto os dados do bloco quanto os dos componentes individuais se disponíveis.

---

## Armadilhas comuns

- **Vácuo em kPa vs mbar:** Ambas as unidades são usadas. Registrar a unidade exata do fabricante e NÃO converter sem declarar.
- **Consumo de ar em diferentes pressões:** O consumo de ar comprimido varia com a pressão de entrada. Valor "padrão" geralmente a 6 bar — verificar.
- **Ejetores multistágio vs estágio único:** Diferem significativamente em fluxo e nível de vácuo. Não interpolar entre modelos da mesma família.
- **IO-Link:** Sensores IO-Link podem reportar pressão absoluta ou relativa dependendo da configuração — declarar qual.
