# Tipo de Dado: `dados-layout-infraestrutura`

## Natureza

Dados do **ambiente físico** onde um sistema técnico será ou está instalado: dimensões de espaço, capacidades estruturais, disponibilidade de utilidades (energia, ar comprimido, rede) e restrições de acesso. Documenta o estado encontrado do ambiente — não o estado desejado ou projetado.

Todo dado deste tipo responde à pergunta: "o que este ambiente físico oferece e limita para uma instalação técnica?"

O tipo se aplica a qualquer ambiente de instalação de sistemas técnicos: fábricas, armazéns, laboratórios, data centers, áreas externas. Não se limita a robótica.

## Critérios de qualidade

- **Fonte identificada** — planta, vistoria in loco, especificação de obra — com data
- **Estado documentado** — "como construído" (as-built) tem prioridade sobre projeto original. Registrar qual dos dois é a fonte.
- **Capacidades declaradas, não estimadas** — capacidade de piso, corrente disponível, pressão de ar: registrar o que está documentado
- **Data do levantamento** — ambiente muda (reformas, novas instalações)

Dados não documentados recebem `NULL-MISSING` — capacidades não podem ser estimadas para fins de infraestrutura.

## Fontes válidas

- Plantas e projetos arquitetônicos ou de instalações datados e revisados
- Projetos elétricos e diagramas de instalação
- Levantamento in loco documentado com data e responsável
- Especificação de obra ou memorial descritivo

## Fontes inválidas

- Plantas sem data ou revisão
- Memória de responsável sem documento de suporte
- Dados de projetos anteriores sem confirmação de que o ambiente é o mesmo

## Limites com outros tipos

- **Não é `dados-geometricos`:** geometria dos componentes que serão instalados vão em `dados-geometricos`. Este tipo coleta o espaço onde eles serão instalados.
- **Não é `dados-seguranca-funcionais`:** parâmetros de segurança funcional (PL, SIL, zonas de segurança definidas por avaliação de risco) vão em `dados-seguranca-funcionais`. Dimensões físicas de corredores e rotas de emergência vão aqui.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos com base no ambiente e na tarefa. Exemplos:

- Para planta industrial: dimensões do espaço, capacidade de carga do piso (distribuída vs. ponto), alimentação elétrica disponível (V, fases, A), ar comprimido (bar, vazão), restrições de acesso, fonte + data
- Para célula robótica existente: layout atual, pontos de ancoragem, disponibilidade de rede, temperatura ambiente, iluminação se relevante para visão
- Para pré-projeto: o que o ambiente oferece vs. o que a instalação vai requerer — como dois conjuntos de dados separados
