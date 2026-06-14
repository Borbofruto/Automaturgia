# Tipo de Dado: `desempenho-ensaio`

## Natureza

Resultados de medições de desempenho obtidos por **ensaio documentado**, com método, condições e fonte rastreáveis. Diferente de especificações declaradas pelo fabricante — este tipo coleta o que foi *medido*, não o que foi *prometido*.

Todo dado deste tipo responde à pergunta: "o que foi medido, como, em que condições, e quem mediu?"

O tipo se aplica a qualquer grandeza mensurável de qualquer componente ou sistema: repetibilidade, tempo de ciclo, força, vazão, temperatura, tensão, vibração. Não se limita a robótica nem a nenhuma norma específica.

## Critérios de qualidade

Todo resultado de ensaio deve ter:
- **Valor medido + unidade**
- **Método de medição** — norma de referência (ISO 9283, IEC 60068, etc.) ou descrição do procedimento
- **Condições do ensaio** — pelo menos: carga/payload, velocidade, temperatura ambiente, postura ou configuração
- **Executor** — fabricante, laboratório, pesquisador (quem mediu afeta o peso do dado)
- **Fonte** — relatório, paper, datasheet com seção de ensaio

Valor sem condição de ensaio = dado inválido. Campo recebe `NULL-MISSING`.

## Fontes válidas

- Relatório de ensaio de laboratório certificado
- Datasheet do fabricante com seção de desempenho explicitando condições
- Paper acadêmico com metodologia documentada
- Relatório técnico interno com setup documentado e rastreável

## Fontes inválidas

- Valores de desempenho sem condições de ensaio declaradas
- Comparativos de mercado que citam specs sem referência à fonte primária
- Estimativas ou valores simulados apresentados como medidos
- Reviews técnicos sem metodologia formal

## Limites com outros tipos

- **Não é `parametros-componente`:** valores declarados pelo fabricante como especificação (payload nominal, alcance) são `parametros-componente`. Aqui coleta-se o resultado de uma medição com método.
- **Não é `conformidade-certificados`:** o ensaio que gera um certificado de conformidade é `conformidade-certificados`. Ensaios de desempenho sem vínculo a processo de certificação são `desempenho-ensaio`.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos com base no parâmetro ensaiado e na tarefa. Exemplos:

- Para repetibilidade de robô (ISO 9283): valor ±mm, ciclo de teste, payload, velocidade, temperatura, quem executou
- Para força de sustentação de ventosa: valor N, pressão de vácuo aplicada, tipo de superfície, instrumento de medição
- Para tempo de ciclo: trajetória exata, carga transportada, velocidade programada, número de ciclos medidos
