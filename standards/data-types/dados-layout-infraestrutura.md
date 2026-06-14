# dados-layout-infraestrutura — Tipo de Dado

## Descrição
Dados do ambiente físico onde um sistema robótico será ou está instalado: dimensões de área, capacidade estrutural, disponibilidade de serviços (energia, ar comprimido, rede) e restrições de acesso. Documenta o estado encontrado do ambiente — não o estado desejado ou projetado.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Identificação do espaço | S | Texto | Nome ou código do ambiente (ex: "Linha 3 — Célula B") |
| Área disponível | N | m² | Planta livre para a célula robótica |
| Dimensões do espaço | N | m × m × m | Largura × profundidade × altura útil |
| Capacidade de carga do piso | N | kg/m² | Carga distribuída suportada |
| Pontos de ancoragem disponíveis | N | Texto | Posição e capacidade de carga |
| Alimentação elétrica disponível | N | V / fases / A | Tensão, número de fases e corrente disponível no ponto |
| Distância ao quadro elétrico | N | m | — |
| Ar comprimido | N | bar / m³/min | Pressão e vazão disponíveis; sim/não se apenas presença |
| Rede de comunicação | N | Texto | Ethernet, Profinet, Wifi — se disponível no ponto |
| Iluminação | N | lux | Se relevante para visão computacional |
| Temperatura ambiente | N | °C | Faixa operacional medida |
| Restrições de acesso | N | Texto | Corredores, portas, rotas de emergência que limitam o layout |
| Fonte do levantamento | S | Texto | Planta, vistoria in loco, especificação de obra |
| Data do levantamento | S | Data | — |

## Fontes válidas (em ordem de prioridade)
1. Plantas e projetos arquitetônicos ou de instalações (datados e revisados)
2. Projetos elétricos e diagramas de instalação
3. Levantamento in loco documentado (com data e responsável)
4. Especificação de obra ou memorial descritivo

## Fontes inválidas
- Plantas sem data ou revisão
- Memória de responsável sem documento de suporte
- Dados de projetos anteriores sem confirmação de que o ambiente é o mesmo

## Regras de qualidade
- Dados "como construído" (as-built) têm prioridade sobre projeto original — verificar se a planta é do projeto ou do as-built
- Capacidade de carga do piso: registrar se é carga distribuída ou ponto — robôs transmitem carga concentrada
- Disponibilidade elétrica: registrar se o ponto já existe ou se requer instalação nova
- Dados ausentes: `NULL-MISSING` — não estimar capacidades não documentadas
- Se o ambiente foi vistoriado in loco, registrar data, quem vistoriou e quais instrumentos foram usados

## Armadilhas comuns
- Plantas de projeto e situação real frequentemente divergem — registrar se foi verificado in loco ou apenas em planta
- Capacidade de piso declarada em projeto pode não considerar cargas adicionadas posteriormente
- "Há rede ethernet" ≠ "há porta ethernet disponível no ponto" — verificar disponibilidade real
