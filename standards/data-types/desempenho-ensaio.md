# desempenho-ensaio — Tipo de Dado

## Descrição
Resultados de medições de desempenho de um componente ou sistema, obtidos por ensaio documentado. Inclui o valor medido, a condição de ensaio, o método utilizado e a fonte. Não inclui interpretações sobre se o desempenho é adequado ou superior — apenas o que foi medido e como.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Componente / sistema ensaiado | S | Texto | Fabricante + modelo + versão |
| Parâmetro medido | S | Texto | Ex: "Repetibilidade", "Tempo de ciclo" |
| Valor medido | S | Numérico + unidade | Ex: "±0.02 mm" |
| Método de medição | S | Texto | Norma de referência (ISO 9283, etc.) ou descrição do método |
| Condições do ensaio | S | Texto | Payload, velocidade, temperatura, postura, ciclo de teste |
| Incerteza de medição | N | Numérico + unidade | Se declarada pela fonte |
| Executor do ensaio | N | Texto | Fabricante, laboratório terceiro, pesquisador |
| Instituição / laboratório | N | Texto | — |
| Data do ensaio | N | Data | — |
| Fonte do resultado | S | Texto + URL/ref | Datasheet, relatório de ensaio, paper |

## Fontes válidas (em ordem de prioridade)
1. Datasheet do fabricante com seção de desempenho (valores declarados pelo fabricante, com condições)
2. Relatório de ensaio de laboratório certificado
3. Paper acadêmico com metodologia e condições de ensaio explicitamente documentadas
4. Relatório técnico interno com setup documentado

## Fontes inválidas
- Valores de desempenho sem condições de ensaio declaradas
- Comparativos de mercado que citam specs sem referência à fonte primária
- Estimativas ou valores simulados apresentados como medidos
- Blogs ou reviews técnicos sem referência a ensaio formal

## Regras de qualidade
- Valor sem condição de ensaio = dado inválido — campo fica `NULL-MISSING`
- Condições mínimas obrigatórias: payload, velocidade, temperatura ambiente
- Método de medição obrigatório: citar norma (ISO 9283, etc.) ou descrever o procedimento usado
- Repetibilidade declarada pelo fabricante vs. medida por terceiro são dados distintos — coletar como registros separados
- Se duas fontes divergem no mesmo parâmetro sob as mesmas condições: preservar ambos com fonte; criar `registro-conflitos`
- Dados ausentes: `NULL-MISSING` com nota de quais fontes foram consultadas

## Armadilhas comuns
- Repetibilidade ISO 9283 mede apenas um ciclo específico — não equivale a precisão geral
- "Tempo de ciclo" pode ser definido de formas diferentes — verificar trajetória e distância do ciclo medido
- Dados de desempenho de datasheets são frequentemente condições ideais — registrar isso explicitamente
- Ensaios feitos pelo fabricante vs. ensaios independentes têm peso de confiança diferente — registrar quem ensaiou
