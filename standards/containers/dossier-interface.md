# dossier-interface — Container

## Descrição
Container relacional que documenta os dados de interface entre exatamente dois objetos nomeados. Não é sobre um objeto isolado — é sobre o espaço entre dois objetos: como eles se conectam, se comunicam e quais condições precisam ser atendidas para que a conexão funcione. Um dossier-interface distinto é necessário para cada par de objetos.

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Cabeçalho de identificação | S | Objeto A (fabricante + modelo + versão) + Objeto B (fabricante + modelo + versão) |
| Tipo(s) de interface | S | Mecânica / Elétrica / Comunicação / Software — pode ser mais de um |
| Tabela de parâmetros por tipo de interface | S | Ver estrutura abaixo |
| Status de compatibilidade geral | S | Compatível confirmado / Compatível não verificado / Incompatível / Não verificável |
| Seção de fontes | S | Referências numeradas |
| Registro de conflitos | Quando houver | Referência ao `registro-conflitos` |

## Estrutura da tabela de parâmetros

Para cada tipo de interface presente:

**Interface Mecânica:**
| Parâmetro | Valor | Unidade | Fonte | Estado |
| Padrão de flange | — | — | — | — |
| Diâmetro de acoplamento | — | mm | — | — |
| Pinos de localização | — | — | — | — |

**Interface Elétrica:**
| Pino | Sinal | Tensão | Direção | Fonte | Estado |
| — | — | V | I/O | — | — |

**Interface de Comunicação:**
| Parâmetro | Valor | Fonte | Estado |
| Protocolo | — | — | — |
| Velocidade | — bps | — | — |
| Endereçamento | — | — | — |

## Regras de preenchimento
- Objeto A e Objeto B devem ser identificados com fabricante + modelo + versão — nunca genérico
- Cada tipo de interface é documentado separadamente
- Status de compatibilidade: "Compatível confirmado" requer documentação de ambos os fabricantes ou ensaio documentado
- Se apenas um fabricante documenta a compatibilidade: `Compatível não verificado`
- Se há contradição entre fontes: `Não verificável` + `registro-conflitos`
- Dados ausentes: `NULL-MISSING`

## O que o Supervisor verifica
- Ambos os objetos identificados com versão
- Status de compatibilidade fundamentado na fonte (não inferido)
- Parâmetros de pinout especificam perspectiva do conector
- Sem inferências de compatibilidade a partir de protocolos comuns

## Tipos de dado compatíveis
`interfaces-compatibilidade` | `dados-conectividade-comunicacao` | `software-firmware`
