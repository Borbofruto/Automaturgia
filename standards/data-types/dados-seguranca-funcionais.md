# dados-seguranca-funcionais — Tipo de Dado

## Descrição
Parâmetros de segurança funcional documentados de um sistema robótico ou componente: zonas de segurança, Performance Level (PL), Safety Integrity Level (SIL), funções de parada, monitoramentos de segurança. Coleta apenas o que está documentado em fontes formais — nunca deriva ou extrapola valores de segurança.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Componente / sistema | S | Texto | Fabricante + modelo + versão |
| Função de segurança | S | Texto | Ex: "Parada de emergência", "Monitoramento de velocidade segura" |
| Performance Level (PL) | N | Texto | PLa a PLe, conforme EN ISO 13849-1 |
| SIL | N | Texto | SIL 1-3, conforme IEC 62061 |
| Categoria (EN ISO 13849-1) | N | Texto | Cat. 1, 2, 3 ou 4 |
| Categoria de parada (IEC 60204-1) | N | Texto | Cat. 0, 1 ou 2 |
| Zona de segurança | N | Texto | Zona colaborativa, zona restrita, espaço protegido — conforme ISO/TS 15066 |
| Parâmetros de monitoramento | N | Tabela | Parâmetro, limite, unidade, norma de referência |
| Tempo de resposta / reação | N | ms | Tempo de reação do sistema de segurança |
| Norma de referência | S | Texto | ISO 10218-1/2, ISO/TS 15066, EN ISO 13849-1, IEC 62061 |
| Fonte | S | Texto + ref | Manual de segurança, relatório de avaliação de risco, certificado |
| Data do documento fonte | S | Data | — |

## Fontes válidas (em ordem de prioridade)
1. Manual de segurança oficial do fabricante (com número de revisão)
2. Relatório de avaliação de risco documentado (com metodologia)
3. Certificado de conformidade de organismo notificado para a função de segurança específica
4. Application note de segurança oficial do fabricante

## Fontes inválidas
- Inferências a partir de protocolos de comunicação ("usa Profisafe, então é SIL 2")
- Declarações de marketing ou comerciais ("robô colaborativo seguro")
- Valores calculados sem metodologia documentada

## Regras de qualidade
- NUNCA derivar PL ou SIL a partir de características técnicas do produto — apenas registrar o que está formalmente documentado
- PL e SIL são propriedades de funções de segurança específicas, não do produto como um todo — sempre especificar para qual função
- Zona colaborativa ISO/TS 15066 requer avaliação de risco para o uso específico — o que o fabricante documenta é capacidade, não autorização para uso colaborativo
- Parâmetros de monitoramento: sempre incluir a norma ou especificação que define o limite
- Dados ausentes: `NULL-MISSING` — nunca estimar valores de segurança

## Armadilhas comuns
- "Cobot" não implica ausência de risco ou dispensa de avaliação de risco — registrar apenas o que está documentado
- PL de componente ≠ PL do sistema — a integração pode reduzir o nível de desempenho
- ISO/TS 15066 foi substituída por ISO TS 15066:2016; verificar se há atualização posterior em andamento
