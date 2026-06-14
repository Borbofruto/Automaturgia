# parametros-componente — Tipo de Dado

## Descrição
Especificações técnicas intrínsecas de um único componente (robô, atuador, sensor, controlador, end effector). Dados que descrevem o que o componente é e pode fazer por si só, sem depender de outros objetos do sistema.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Fabricante | S | Texto | Nome oficial |
| Modelo / Part Number | S | Texto | Exatamente como no datasheet |
| Revisão / Versão | S | Texto | Data ou número de revisão do documento fonte |
| Payload nominal | S | kg | Condição de montagem e postura devem estar na fonte |
| Alcance máximo | S | mm | Distância flange–base, postura estendida |
| Número de graus de liberdade | S | Inteiro | — |
| Limite de posição por joint | S | graus ou mm | Min/max por eixo |
| Velocidade máxima por joint | S | graus/s ou mm/s | Por eixo |
| Torque nominal por joint | N | N·m | Por eixo, se disponível |
| Parâmetros DH (a, d, α, θ_offset) | N | mm / rad | Por eixo; declarar convenção usada (Craig, MDH, etc.) |
| Peso do robô | S | kg | Sem cabo |
| Proteção (IP) | S | Código IP | Ex: IP54 |
| Temperatura de operação | S | °C | Min/max |
| Tensão de alimentação | S | V / Hz | — |
| Consumo de potência | N | W | Nominal e pico, se disponível |
| Opções de montagem | N | Texto | Piso, teto, parede, inclinado |
| Repetibilidade | N | mm | ±; método de medição (ISO 9283 se declarado) |

## Fontes válidas (em ordem de prioridade)
1. Datasheet oficial do fabricante (PDF do site do fabricante, com versão e data)
2. Manual técnico / manual de instalação oficial
3. Especificação técnica em portal de download autenticado do fabricante
4. Paper acadêmico com derivação metodológica explícita (segunda escolha para parâmetros DH)

## Fontes inválidas
- Sites de revendedores ou integradores (podem conter dados desatualizados ou incorretos)
- Comparativos de mercado (Robotics-Tomorrow, Automate, etc.)
- Vídeos, blogs, fóruns
- Datasheets sem identificação de versão ou data

## Regras de qualidade
- Cada valor numérico deve ter unidade explícita e referência de fonte (documento + página ou seção)
- Valores ausentes: `NULL-MISSING` — nunca omitir, nunca estimar
- Se duas fontes divergem: preservar ambos os valores com fonte individual; criar entrada em `registro-conflitos`; não resolver
- Parâmetros DH exigem declaração explícita da convenção (Craig, DH padrão, MDH)
- Dados de payload devem especificar condições (postura, distância do CG ao flange)
- Verificar data do datasheet: robôs podem ter especificações atualizadas por firmware ou revisão mecânica

## Armadilhas comuns
- Payload "máximo" vs. payload "nominal" são valores diferentes — coletar ambos se disponíveis
- Alcance pode variar por definição (ponta da ferramenta vs. flange) — registrar qual definição foi usada
- Parâmetros DH de fabricantes asiáticos frequentemente usam convenção diferente da Craig — verificar
