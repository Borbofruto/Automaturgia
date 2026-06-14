# modelos-interoperabilidade — Tipo de Dado

## Descrição
Esquemas formais e estruturas de dados padronizadas que descrevem como informações técnicas de produto são representadas para intercâmbio entre sistemas: ISO 10303 (STEP), eCl@ss, IEC CDD, URDF como esquema lógico, ou modelos AML. Diferente de `dados-geometricos` (que coleta o arquivo CAD em si), este tipo coleta o esquema ou dicionário — a estrutura formal, não o arquivo de geometria.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Nome do esquema / dicionário | S | Texto | Ex: "eCl@ss 12.0", "ISO 10303-214", "AutomationML 2.10" |
| Padrão de referência | S | Texto | ISO 10303, IEC CDD, eCl@ss, AutomationML, etc. |
| Formato de representação | S | Texto | EXPRESS, XML, JSON-LD, RDF/OWL, etc. |
| Versão | S | Texto | Versão ou edição do esquema |
| Entidade / classe relevante | N | Texto | Ex: "eCl@ss 27-01-04-01 (Industrial Robot)" |
| Atributos / propriedades definidos | N | Lista | Atributos formais do esquema que se aplicam ao contexto |
| IDs de elemento de dados (eCl@ss/IEC) | N | Lista | IRDI ou ECLASS code dos atributos |
| AP (Application Protocol) — ISO 10303 | N | Texto | Ex: "AP214", "AP242" |
| URL do dicionário ou repositório | N | URL | Portal eCl@ss, IEC CDD portal, etc. |
| Aplicabilidade ao contexto | N | Texto | Como este esquema se aplica à tarefa — descritivo |

## Fontes válidas (em ordem de prioridade)
1. Portal oficial eCl@ss (eclass.eu)
2. IEC Common Data Dictionary (cdd.iec.ch)
3. ISO 10303 Application Protocols (documentos ISO oficiais)
4. AutomationML e.V. (automationml.org)
5. Repositórios de Application Modules de AP específicos

## Fontes inválidas
- Mapeamentos informais entre padrões criados por terceiros
- Tabelas de equivalência em papers sem referência ao padrão oficial

## Regras de qualidade
- Versão do esquema é obrigatória: eCl@ss 11 e eCl@ss 12 têm estruturas diferentes
- IDs de elementos (IRDI, ECLASS code) devem ser registrados exatamente como no dicionário — são identificadores formais
- Não mapear atributos sem verificar se o mapeamento está definido no padrão — mapeamento informal vai para `registro-conflitos`
- Dados ausentes: `NULL-MISSING`

## Armadilhas comuns
- eCl@ss e IEC CDD têm dicionários diferentes com IDs diferentes para conceitos similares — não consolidar
- ISO 10303 AP242 substituiu AP203 e AP214 em muitos contextos, mas não em todos — verificar qual AP é relevante
- URDF como esquema de descrição de robô é diferente de URDF como arquivo de geometria — registrar o contexto de uso
