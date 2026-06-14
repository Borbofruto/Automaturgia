# Tipo de Dado: `casos-aplicacao`

## Natureza

Registros descritivos de **instalações reais ou implementações documentadas** de sistemas técnicos. Captura o que foi feito, com quais componentes, em que contexto — sem análise de desempenho, sem conclusões sobre o que funcionou ou não.

Todo dado deste tipo responde à pergunta: "este sistema foi usado desta forma, neste contexto, com estes componentes — conforme documentado na fonte."

O caso é um dado; a interpretação é trabalho humano posterior. O tipo se aplica a qualquer implementação documentada: robótica industrial, automação de processo, sistemas de controle, infraestrutura de TI. Não se limita a robótica.

## Critérios de qualidade

- **Componentes identificados com fabricante e modelo** — nunca apenas "robô colaborativo" ou "sensor de força"
- **Fonte identificada** — case study do fabricante, paper, publicação técnica — com data
- **Conteúdo transcrito conforme declarado** — o que a fonte diz, não o que se infere
- **Resultados como dado da fonte** — se a fonte declara "reduziu 30%", registrar isso com flag `nao-verificavel`, não como fato verificado

## Fontes válidas

- Case studies oficiais de fabricantes com dados verificáveis
- Papers acadêmicos ou de conferência com implementação real documentada
- Reportagens técnicas em publicações especializadas
- White papers de integradores com dados verificáveis

## Fontes inválidas

- Depoimentos de clientes sem dados técnicos
- Comunicados de imprensa sem informação de implementação
- Cases sem identificação dos componentes utilizados

## Limites com outros tipos

- **Não é `parametros-componente`:** especificações do componente usado no caso vão em `parametros-componente`. Este tipo coleta o contexto de uso real, não os parâmetros do componente.
- **Não é `fornecedores-integradores`:** quem integrou o sistema vai em `fornecedores-integradores`. Este tipo coleta o caso de aplicação que eles executaram.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos com base no caso e na tarefa. Exemplos:

- Para case study de paletização: setor, tipo de produto, componentes usados (robô + garra + software), configuração operacional, fonte, data
- Para implementação de cobot em montagem: empresa (se divulgada), contexto declarado pela fonte, especificações de uso (payload, velocidade), integrador (se mencionado)
- Para instalação industrial documentada em paper: todos os autores, DOI, componentes listados no paper, configuração experimental
