# Tipo de Dado: `dados-conectividade-comunicacao`

## Natureza

Dados sobre **redes, protocolos e topologia de comunicação** de um componente, sistema ou infraestrutura de rede. Documenta capacidades declaradas e configurações existentes — não infere configurações a partir de protocolos conhecidos.

Todo dado deste tipo responde à pergunta: "o que este componente ou sistema suporta em termos de comunicação, e como está ou pode estar configurado?"

O tipo cobre infraestrutura de comunicação em qualquer nível: física (Ethernet, RS-485), fieldbus (Profinet, EtherNet/IP, Modbus), middleware (OPC UA, ROS), e redes de TI. Não se limita a robótica industrial.

## Critérios de qualidade

- **Componente ou sistema identificado** — fabricante, modelo, versão de firmware (protocolos suportados podem mudar com updates)
- **Capacidade declarada vs. configuração existente** — declarar qual dos dois está sendo documentado
- **Versão do protocolo especificada** — "suporta OPC UA" pode não incluir companion specifications; "suporta Profinet" pode não incluir PROFIsafe
- **Fonte** — manual de comunicação, datasheet de interface, diagrama de rede com data

Suporte declarado ao protocolo ≠ compatibilidade de integração. Compatibilidade entre dois componentes vai em `interfaces-compatibilidade`.

## Fontes válidas

- Manual de comunicação ou manual de fieldbus oficial do fabricante
- Datasheet da interface de comunicação
- Application note de integração de rede oficial do fabricante
- Diagrama de rede documentado (as-built, com data)

## Fontes inválidas

- Configurações inferidas a partir do protocolo
- Fóruns sem referência a documento oficial
- Configurações de projetos anteriores sem confirmação que o modelo é o mesmo

## Limites com outros tipos

- **Não é `interfaces-compatibilidade`:** compatibilidade de comunicação entre dois objetos específicos vai em `interfaces-compatibilidade`. Este tipo coleta a capacidade de comunicação de um componente individualmente, ou a topologia de uma rede.
- **Não é `modelos-interoperabilidade`:** esquemas de dados formais (OPC UA Information Model, eCl@ss) vão em `modelos-interoperabilidade`. Aqui coleta-se a infraestrutura de transporte, não o modelo de dados.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos com base no componente/rede e na tarefa. Exemplos:

- Para interface de comunicação de cobot: protocolos suportados, versões, interfaces físicas, parâmetros configuráveis (IP, node ID), fonte + versão de firmware
- Para topologia de rede de célula: diagrama as-built, equipamentos conectados, switches, endereçamento, VLANs se aplicável, data do levantamento
- Para OPC UA: namespace, information model implementado, companion specifications disponíveis, perfil de segurança suportado
