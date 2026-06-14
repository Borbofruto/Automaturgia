# casos-aplicacao — Tipo de Dado

## Descrição
Registros descritivos de instalações reais ou implementações documentadas de sistemas robóticos. Captura o que foi feito, com quais componentes, em que contexto — sem análise de desempenho, sem conclusões sobre o que funcionou ou não. O caso é um dado; a interpretação é trabalho humano posterior.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Título do caso | S | Texto | Nome ou descrição curta da aplicação |
| Setor / indústria | S | Texto | Alimentos, automotivo, farmacêutico, logística, etc. |
| Tipo de aplicação | S | Texto | Paletização, solda, pick-and-place, inspeção, montagem, etc. |
| Empresa / cliente | N | Texto | Se divulgado pela fonte; omitir se não divulgado |
| País / região | N | Texto | — |
| Componentes utilizados | S | Lista | Robô (modelo), end effector, controlador, software — com fabricante e modelo |
| Configuração de uso | N | Texto | Payload utilizado, velocidade operacional, ciclo, montagem |
| Contexto da implementação | N | Texto | Por que foi adotado? Qual o problema que resolveu? (conforme declarado na fonte) |
| Fonte | S | Texto + URL | Case study do fabricante, paper, notícia técnica |
| Data de publicação / implementação | S | Data | — |

## Fontes válidas (em ordem de prioridade)
1. Case studies oficiais de fabricantes (com dados verificáveis)
2. Papers acadêmicos ou de conferência com implementação real documentada
3. Reportagens técnicas em publicações especializadas (Robotics Business Review, A3, etc.)
4. White papers de integradores com dados verificáveis

## Fontes inválidas
- Depoimentos de clientes sem dados técnicos
- Comunicados de imprensa sem informação de implementação
- Cases sem identificação dos componentes utilizados

## Regras de qualidade
- Componentes devem ser identificados com fabricante E modelo — nunca apenas "robô colaborativo"
- Contexto de implementação: transcrever o que a fonte declara, não interpretar intenções
- Não incluir avaliações de sucesso, ROI, produtividade — esses são dados de estudo, não dados de coleta
- Se a fonte declara resultados (ex: "reduziu tempo de ciclo em 30%"), registrar como dado da fonte, não como fato verificado, com flag `nao-verificavel`
- Dados ausentes: `NULL-MISSING`

## Armadilhas comuns
- Cases de fabricantes frequentemente omitem informações desfavoráveis — registrar o que está disponível sem inferir o que não está
- "Aplicação similar" não é o mesmo caso — não consolidar casos distintos
- Data de implementação e data de publicação podem ser muito diferentes — registrar ambas quando disponíveis
