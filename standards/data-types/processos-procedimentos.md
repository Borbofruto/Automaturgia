# processos-procedimentos — Tipo de Dado

## Descrição
Sequências técnicas documentadas para executar uma operação em um componente ou sistema: calibração, montagem, parametrização, manutenção preventiva, configuração de segurança. Coleta os passos como estão na fonte — sem simplificação, sem adaptação, sem inferência de passos ausentes.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Nome do procedimento | S | Texto | — |
| Componente / sistema de escopo | S | Texto | Fabricante + modelo + versão |
| Tipo de procedimento | S | Texto | Calibração / Montagem / Parametrização / Manutenção / Configuração / Comissionamento |
| Pré-requisitos | N | Lista | O que deve estar feito antes de iniciar |
| Ferramentas / equipamentos necessários | N | Lista | Com especificações se declaradas |
| Sequência de passos | S | Lista numerada | Transcritos literalmente da fonte — sem paráfrase |
| Norma de referência | N | Texto | Se o procedimento referencia uma norma |
| Avisos de segurança | N | Lista | Conforme declarados na fonte |
| Fonte | S | Texto + ref | Manual, application note, boletim técnico — com seção/página |
| Versão da fonte | S | Texto | Número de revisão ou data do documento |

## Fontes válidas (em ordem de prioridade)
1. Manual técnico oficial do fabricante (com número de revisão)
2. Application note ou boletim técnico oficial
3. Procedimento validado de laboratório certificado (com registro)

## Fontes inválidas
- Tutoriais de YouTube ou blogs
- Fóruns técnicos (UR Forum, ROS Discourse) sem referência a documento oficial
- Procedimentos sem identificação de fonte ou versão

## Regras de qualidade
- Passos devem ser transcritos — não resumidos, não reordenados, não simplificados
- Se o manual tiver avisos de segurança entre os passos, eles devem ser preservados no registro
- Versão do documento fonte é obrigatória: procedimentos podem mudar entre revisões
- Não inferir passos ausentes: se o procedimento na fonte parece incompleto, registrar isso como `nao-verificavel` para os campos ausentes
- Dados ausentes: `NULL-MISSING`

## Armadilhas comuns
- Manuais em inglês podem ter procedimentos ligeiramente diferentes das versões em português — verificar se há versão oficial em PT-BR ou usar o original com nota
- Procedimentos de instalação vs. comissionamento são distintos — não consolidar
- Avisos de segurança omitidos são um problema de qualidade, não uma simplificação aceitável
