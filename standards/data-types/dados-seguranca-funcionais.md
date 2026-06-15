# Tipo de Dado: `dados-seguranca-funcionais`

## Natureza

Parâmetros de **segurança funcional** documentados em fontes formais: Performance Level (PL), Safety Integrity Level (SIL), funções de parada, zonas de segurança, monitoramentos. Coleta apenas o que está explicitamente documentado — nunca deriva, extrapola ou estima valores de segurança.

Todo dado deste tipo responde à pergunta: "o que foi formalmente documentado sobre a segurança funcional deste sistema ou componente, e por qual fonte?"

Este é o tipo com maior restrição de fonte da Automaturgia. Qualquer valor de segurança sem fonte formal documentada recebe `NULL-MISSING` — não existe `nao-verificavel` como substituto para PL ou SIL não documentado.

## Critérios de qualidade

- **Função de segurança especificada** — PL e SIL são propriedades de funções específicas, não do produto como um todo. Campo inválido sem a função declarada.
- **Norma de referência** — qual norma define o parâmetro coletado (ISO 13849-1, IEC 62061, ISO/TS 15066, etc.)
- **Fonte formal identificada** — manual de segurança, relatório de avaliação de risco, certificado de organismo notificado
- **Versão do documento** — parâmetros de segurança podem mudar entre revisões

## Fontes válidas

- Manual de segurança oficial do fabricante com número de revisão
- Relatório de avaliação de risco documentado com metodologia
- Certificado de conformidade de organismo notificado para a função de segurança específica
- Application note de segurança oficial do fabricante

## Fontes inválidas

- Inferências a partir de protocolos de comunicação ("usa PROFIsafe, então é SIL 2")
- Declarações de marketing ou comerciais ("seguro para trabalho colaborativo")
- Valores calculados sem metodologia documentada
- Estimativas baseadas em produtos similares

## Limites com outros tipos

- **Não é `conformidade-certificados`:** o certificado que atesta a segurança funcional vai em `conformidade-certificados`. Os parâmetros de segurança declarados no manual vão aqui.
- **Não é `normas-regulamentacoes`:** as normas de segurança (ISO 13849-1, IEC 62061) vão em `normas-regulamentacoes`. Os valores de PL/SIL de um produto específico vão aqui.
- **Não é `processos-procedimentos`:** o procedimento de configuração de zona de segurança vai em `processos-procedimentos`. Os parâmetros resultantes documentados vão aqui.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos com base no sistema e na tarefa. Exemplos:

- Para função de parada de emergência de cobot: função de segurança, PL alcançado, norma de referência (ISO 13849-1), categoria de parada (IEC 60204-1), tempo de reação, fonte + revisão
- Para zona colaborativa: dimensões, velocidade máxima monitorada, força máxima monitorada, norma de referência (ISO/TS 15066), configuração declarada pelo fabricante
- Para monitoramento de velocidade segura: parâmetro, limite, unidade, norma que define o limite, fonte
