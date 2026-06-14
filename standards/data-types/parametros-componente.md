# Tipo de Dado: `parametros-componente`

## Natureza

Parâmetros que definem o comportamento e os limites operacionais de um **componente individual**, conforme declarado pelo fabricante para um modelo específico. São dados intrínsecos ao componente — independem da instalação, do contexto de uso ou da relação com outros componentes.

Todo dado deste tipo responde à pergunta: "o que este componente é capaz de fazer ou suportar, segundo quem o fabricou?"

O componente pode ser qualquer coisa: cobot, ventosa, sensor, garra, redutor, válvula, atuador, câmera. O tipo se aplica a qualquer componente técnico para o qual um fabricante declare especificações formais.

## Critérios de qualidade

Todo valor coletado deste tipo deve ter:
- **Valor + unidade** (grandezas numéricas)
- **Referência ao documento OEM** — datasheet, manual técnico ou especificação formal, com número de revisão ou data quando disponível
- **Estado** — `confirmado`, `nao-verificavel`, `conflito`, `nao-aplicavel` ou `NULL-MISSING`

Parâmetros que variam por condição de operação (temperatura, carga, velocidade) devem registrar as condições junto com o valor.

## Fontes válidas

- Datasheet oficial do fabricante (versão identificável por data ou revisão)
- Manual técnico do fabricante
- Especificações publicadas no site OEM com data de acesso registrada
- Documentos de certificação que incluam parâmetros técnicos

## Fontes inválidas

- Distribuidores (exceto quando reproduzem literalmente a documentação OEM com referência explícita)
- Fóruns, vídeos, artigos de blog
- Valores medidos externamente (→ usar `desempenho-ensaio`)
- Especificações de modelos similares ou de gerações anteriores
- Estimativas ou valores "típicos" sem fonte OEM

## Limites com outros tipos

- **Não é `interfaces-compatibilidade`:** parâmetros deste tipo descrevem um componente isolado. Dados sobre como dois componentes interagem vão em `interfaces-compatibilidade`.
- **Não é `desempenho-ensaio`:** parâmetros declarados pelo fabricante ≠ resultados medidos. Se o dado vem de um ensaio documentado com método e condições, é `desempenho-ensaio`.
- **Não é `dados-geometricos`:** dimensões e geometria de forma (CAD, envelope espacial) vão em `dados-geometricos`. Alcance nominal como parâmetro de especificação pode aparecer aqui se declarado pelo fabricante como capacidade.
- **Não é `dados-seguranca-funcionais`:** parâmetros de segurança com nível de performance (PL, SIL) têm tratamento específico em `dados-seguranca-funcionais`.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos relevantes com base no componente e na tarefa. Exemplos para orientar:

- Para um cobot: payload, alcance, repetibilidade, número de eixos, IP, massa, tensão de alimentação
- Para uma ventosa: diâmetro, material de lábio, força de sustentação nominal, pressão de operação, temperatura de uso
- Para um redutor: razão de transmissão, torque máximo, backlash, eficiência
- Para um sensor de força: faixa de medição, resolução, overload admissível, saída de sinal

Campos relevantes emergem do componente e da tarefa — não de uma lista pré-definida.
