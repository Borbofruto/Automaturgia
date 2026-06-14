# dossie-tecnico-tdp — Container

## Descrição
Meta-container para um pacote de dados técnicos de um sistema completo (Technical Data Package). Não duplica os dados de outros containers — aponta para eles. Organiza o sistema como um todo: lista de materiais, relações entre componentes e índice de todos os containers gerados para o projeto.

## Estrutura obrigatória

| Seção | Obrigatório | Notas |
|---|---|---|
| Cabeçalho do sistema | S | Nome do projeto, revisão, data, responsável |
| Lista de materiais (BOM) | S | Todos os componentes do sistema |
| Relações entre componentes | S | Quais componentes se conectam — referência aos dossier-interface |
| Índice de containers | S | Lista de todos os containers gerados para este sistema |
| Status geral de completude | S | Percentual de campos confirmados, em conflito, não encontrados |

## Estrutura da Lista de Materiais

| Item # | Tipo | Fabricante | Modelo | Versão | Papel no sistema | Container de referência |
|---|---|---|---|---|---|---|
| 001 | Robô | Universal Robots | UR10e | CB5 3.15 | Robô principal | ficha-tecnica/UR10e.md |
| 002 | End Effector | Robotiq | 2F-140 | 2.4 | Garra | ficha-tecnica/2F140.md |

## Estrutura do Índice de Containers

| Container | Arquivo | Status | Data |
|---|---|---|---|
| ficha-tecnica UR10e | ficha-tecnica/UR10e | Completo | DD/MM/AAAA |
| dossier-interface UR10e–2F140 | dossier-interface/UR10e-2F140 | Parcial | DD/MM/AAAA |
| registro-conflitos | registro-conflitos/sistema-X | 2 conflitos abertos | DD/MM/AAAA |

## Regras de preenchimento
- Este container não contém dados técnicos — apenas referências aos containers que os contêm
- Toda atualização em containers individuais deve ser refletida no índice (data e status)
- BOM deve identificar cada componente com versão — versões diferentes do mesmo modelo são itens distintos
- Status de completude é calculado a partir dos estados nos containers individuais

## O que o Supervisor verifica
- Índice completo — todo container gerado para o sistema está listado
- BOM com versões identificadas
- Status geral baseado nos containers individuais, não estimado

## Tipos de dado compatíveis
Todos — este é o container de nível de sistema que agrega todos os outros.
