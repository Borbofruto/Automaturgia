# Tipo de Dado: `arquitetura-garra-vacuo`

## Descrição

Configuração estrutural e funcional de uma garra de vácuo como sistema integrado: arranjo das ventosas, estrutura de suporte, distribuição de vácuo e interfaces mecânicas e elétricas. Dado relacional — sempre descreve uma garra específica como composição de componentes. Não coleta parâmetros individuais de ventosa (ver `parametros-ventosa`) nem do sistema pneumático upstream (ver `sistema-vacuo-pneumatico`).

---

## Campos a coletar

### Identificação da garra

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| identificacao_garra | Designação interna da garra (ex: "GV-PAL-01") | — | confirmado |
| aplicacao_alvo | Produto/embalagem alvo (referência ao item em `materiais-produto-embalagem`) | — | confirmado |
| robo_hospedeiro | Robô ao qual a garra se acopla (fabricante + modelo) | — | confirmado |
| fornecedor_garra | Quem fornece ou integra a garra (fabricante ou integrador) | — | confirmado |
| referencia_projeto | Número de projeto ou referência do desenho | — | confirmado / nao-verificavel |

### Arranjo de ventosas

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| numero_ventosas | Quantidade total de ventosas na garra | un | confirmado |
| modelo_ventosa | Referência ao registro em `parametros-ventosa` | — | confirmado |
| layout_ventosas | Descrição do arranjo (ex: "2×4 matriz regular", "adaptativo por zonas") | — | confirmado |
| espacamento_ventosas | Espaçamento entre centros das ventosas | mm | confirmado |
| zonas_independentes | Número de zonas de vácuo independentemente controladas | — | confirmado |
| mapa_zonas | Descrição de quais ventosas pertencem a cada zona | — | confirmado / nao-verificavel |

### Estrutura mecânica

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| material_estrutura | Material do corpo principal da garra | — | confirmado |
| processo_fabricacao | CNC / impressão 3D / soldagem / perfil extrudado / etc. | — | confirmado |
| massa_garra | Massa total da garra (sem produto) | kg | confirmado |
| dimensao_maxima_x | Dimensão máxima no eixo X | mm | confirmado |
| dimensao_maxima_y | Dimensão máxima no eixo Y | mm | confirmado |
| dimensao_maxima_z | Dimensão máxima no eixo Z (altura total) | mm | confirmado |
| cog_x | Centro de gravidade relativo ao flange — eixo X | mm | confirmado / nao-verificavel |
| cog_y | Centro de gravidade relativo ao flange — eixo Y | mm | confirmado / nao-verificavel |
| cog_z | Centro de gravidade relativo ao flange — eixo Z | mm | confirmado / nao-verificavel |
| ip_grau | Grau de proteção IP da garra como sistema | — | confirmado / nao-verificavel |

### Interface mecânica com o robô

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| tipo_flange | Tipo de flange (ISO 9409-1, diâmetro e padrão de furos) | — | confirmado |
| diametro_flange | Diâmetro do flange de acoplamento | mm | confirmado |
| padrao_furos | Padrão de furos (ex: "4× M6 em BC 50mm") | — | confirmado |
| massa_total_com_produto | Massa da garra + produto máximo (para cálculo de payload) | kg | confirmado |
| momentos_inercia | Ix, Iy, Iz declarados (se disponível) | kg·m² | confirmado / nao-verificavel |

### Interface pneumática

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| numero_entradas_vacuo | Número de entradas de vácuo na garra | un | confirmado |
| tipo_conexao_pneumatica | Tipo de conexão da entrada de vácuo | — | confirmado |
| diametro_linha_entrada | Diâmetro da linha de vácuo de entrada | mm | confirmado |
| distribuicao_interna | Manifold integrado / tubos externos / canais usinados | — | confirmado |

### Interface elétrica

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| numero_solenoides | Número de solenoides integradas à garra | un | confirmado / nao-aplicavel |
| tensao_alimentacao | Tensão de alimentação das solenoides | VDC | confirmado / nao-aplicavel |
| numero_sensores | Número de sensores integrados (presença, vácuo) | un | confirmado / nao-aplicavel |
| conector_eletrico | Tipo de conector elétrico (M8, M12, etc.) | — | confirmado / nao-aplicavel |
| numero_pinos | Número de pinos do conector | un | confirmado / nao-aplicavel |

### Desempenho declarado

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| forca_sustentacao_total | Força de sustentação total da garra (condição declarada) | N | confirmado |
| condicao_forca | Condição da força declarada (pressão de vácuo, tipo de superfície) | — | confirmado |
| fator_seguranca_declarado | Fator de segurança declarado pelo fornecedor | — | confirmado / nao-verificavel |
| velocidade_maxima | Velocidade máxima de translação com produto | m/s | confirmado / nao-verificavel |
| aceleracao_maxima | Aceleração máxima com produto | m/s² | confirmado / nao-verificavel |

---

## Fontes válidas

- Desenho de conjunto da garra (DWG, PDF, STEP)
- Especificação técnica do fornecedor da garra
- BOM (Bill of Materials) fornecida pelo integrador
- Datasheet de cada subcomponente (referenciado individualmente)

---

## Fontes inválidas

- Estimativas de desempenho baseadas em fórmulas sem validação empírica
- Valores de garras similares de outros projetos extrapolados para este
- Dados de catálogo de ventosas aplicados à garra sem confirmação do integrador

---

## Regras de qualidade

1. `massa_total_com_produto` deve somar massa da garra + massa máxima do produto — não é a massa apenas da garra.
2. `forca_sustentacao_total` ≠ soma aritmética da força de todas as ventosas — ventosas não atingem a mesma pressão simultaneamente. Registrar o valor declarado pelo fornecedor com as condições explicitadas.
3. Se a garra for adaptativa (ventosas reconfiguráveis por zonas), documentar cada configuração como registro separado.
4. `cog_x/y/z` são críticos para o cálculo de payload — se não fornecidos, marcar `NULL-MISSING` e escalar.
5. Momentos de inércia: se o fornecedor não declara, registrar `NULL-MISSING` — não calcular a partir da geometria sem validação.

---

## Armadilhas comuns

- **Payload do robô ≠ capacidade da garra:** O robô pode suportar 20 kg de payload, mas a garra pode ser o fator limitante pela configuração de ventosas ou pela integridade estrutural da embalagem.
- **Fator de segurança implícito:** Fabricantes de garras frequentemente aplicam fatores de segurança internamente ao declarar capacidade. Verificar se o valor declarado já inclui o fator.
- **Zonas de vácuo independentes:** Garras com zonas independentes podem operar com subconjuntos de ventosas para diferentes formatos de produto — cada configuração de zona tem uma capacidade de sustentação diferente.
