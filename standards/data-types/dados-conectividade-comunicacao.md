# dados-conectividade-comunicacao — Tipo de Dado

## Descrição
Dados sobre redes, protocolos e endereçamento de um componente ou sistema: o que ele suporta, como está configurado, quais parâmetros de comunicação estão definidos. Documenta o estado configurado ou a capacidade declarada pelo fabricante — não infere configurações a partir de protocolos comuns.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Componente / sistema | S | Texto | Fabricante + modelo + versão |
| Interface física | S | Texto | Ethernet, RS-485, USB, EtherCAT, etc. |
| Protocolo de nível de aplicação | S | Texto | EtherNet/IP, Profinet, Modbus TCP, OPC UA, REST, ROS, etc. |
| Velocidade de comunicação | N | Mbps / bps / Hz | — |
| Endereçamento | N | Texto | Faixa de IP, node ID, endereço Modbus |
| Mapa de dados / data model | N | Texto ou tabela | O que é publicado/subscribido, quais registros, quais tags OPC UA |
| Namespace OPC UA | N | URI | Se OPC UA disponível |
| Mestre / escravo (fieldbus) | N | Texto | Qual papel o equipamento assume no barramento |
| Tempo de ciclo de comunicação | N | ms | — |
| Capacidade de conexões simultâneas | N | Inteiro | — |
| Fonte | S | Texto + ref | Manual de comunicação, datasheet de interface, application note |
| Versão do documento fonte | S | Texto | — |

## Fontes válidas (em ordem de prioridade)
1. Manual de comunicação ou manual de fieldbus oficial do fabricante
2. Datasheet da interface de comunicação
3. Application note de integração de rede oficial do fabricante
4. Diagrama de rede documentado (as-built, com data)

## Fontes inválidas
- Configurações inferidas a partir do protocolo ("usa EtherNet/IP, então deve ter registros de I/O em...")
- Fóruns sem referência a documento oficial
- Configurações de projetos anteriores sem confirmação que o modelo é o mesmo

## Regras de qualidade
- Suporte declarado ao protocolo ≠ compatibilidade de integração: dois equipamentos com EtherNet/IP podem não se comunicar sem configuração específica
- Mapa de dados: registrar o que o fabricante documenta — não inferir registros não documentados
- Endereçamento: registrar configuração como-está ou padrão de fábrica — sempre especificar qual dos dois
- Versão de firmware importa: suporte a protocolos pode ser adicionado ou removido em updates
- Dados ausentes: `NULL-MISSING`

## Armadilhas comuns
- OPC UA companion specification pode não estar implementada mesmo que o equipamento suporte OPC UA básico
- "Suporta Profinet" pode significar apenas IO Device, não IRT ou PROFIsafe — verificar perfil suportado
- Velocidade de comunicação declarada pode ser do hardware físico, não do protocolo configurado — especificar qual
