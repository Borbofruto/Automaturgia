# interfaces-compatibilidade — Tipo de Dado

## Descrição
Dados relacionais que descrevem como dois componentes específicos se conectam ou comunicam. Este tipo de dado é sempre relacional — pertence ao espaço entre dois objetos, não a um objeto isolado. Coleta pinout, protocolos, mapeamento de I/O e requisitos de compatibilidade mecânica, elétrica ou de software.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Objeto A (nome exato + modelo) | S | Texto | Ex: "Controlador UR CB3.1" |
| Objeto B (nome exato + modelo) | S | Texto | Ex: "Gripper Robotiq 2F-85" |
| Tipo de interface | S | Texto | Mecânica / Elétrica / Comunicação / Software |
| Padrão de flange (se mecânica) | N | Texto | ISO 9283 flange size, custom |
| Protocolo de comunicação | N | Texto | EtherNet/IP, Profinet, Modbus TCP, RS-485, etc. |
| Velocidade de comunicação | N | bps / Hz | — |
| Pinout / mapeamento de conector | N | Tabela | Pino → sinal → tensão → direção |
| Mapeamento de I/O digital | N | Tabela | Canal → função → nível lógico |
| Mapeamento de I/O analógico | N | Tabela | Canal → sinal → faixa |
| Tensão de alimentação do conector | N | V | Se a interface fornece alimentação |
| Software / driver necessário | N | Texto | Nome + versão mínima |
| Restrições de compatibilidade | N | Texto | Versões incompatíveis, condições limitantes |
| Status de compatibilidade | S | confirmado / nao-verificavel / conflito | — |

## Fontes válidas (em ordem de prioridade)
1. Manual de integração oficial (do fabricante de A ou B, especificamente sobre a conexão entre eles)
2. URCap / plugin documentation (quando a interface é software)
3. Datasheet de conector ou interface elétrica do fabricante
4. Application note oficial do fabricante
5. Nota de integração validada por outro fabricante (ex: Robotiq documenta compatibilidade com UR)

## Fontes inválidas
- Fóruns (Universal Robots Forum, ROS Discourse) sem confirmação de fabricante
- Vídeos de tutorial
- Repositórios GitHub de terceiros (exceto como referência para driver, verificar sempre com docs oficiais)

## Regras de qualidade
- Sempre identificar os dois objetos com fabricante + modelo + revisão
- Pinout deve especificar a referência de qual conector/pino está sendo descrito (ex: "M8 4-pin male, visto da frente")
- Se a compatibilidade é declarada por apenas um fabricante, marcar como `nao-verificavel` até confirmação cruzada
- Nunca inferir compatibilidade a partir de protocolos comuns — requer documentação explícita
- Dados ausentes: `NULL-MISSING` com nota de quais fontes foram consultadas
- Conflitos (ex: documentos distintos com pinout divergente): preservar ambos com fonte; criar `registro-conflitos`

## Armadilhas comuns
- Compatibilidade de protocolo ≠ compatibilidade de integração (dois equipamentos com EtherNet/IP podem não se comunicar sem configuração ou driver específico)
- Versões de firmware podem quebrar compatibilidade — sempre registrar versão dos dois lados
- Connectors às vezes têm numeração de pinos diferente dependendo de qual lado você está olhando — sempre especificar perspectiva
