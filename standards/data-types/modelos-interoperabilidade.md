# Tipo de Dado: `modelos-interoperabilidade`

## Natureza

Esquemas formais e estruturas de dados padronizadas para **representação e intercâmbio de informações técnicas** entre sistemas: dicionários de dados, modelos de informação, application protocols. Coleta o esquema e seus elementos — não o arquivo de produto gerado a partir do esquema.

Todo dado deste tipo responde à pergunta: "como este padrão representa formalmente este conceito técnico, e quais são os identificadores formais dos elementos relevantes?"

O tipo cobre padrões como ISO 10303 (STEP), eCl@ss, IEC CDD, AutomationML, OPC UA Information Models, e outros formatos de intercâmbio padronizados. Aplica-se a qualquer domínio técnico onde interoperabilidade de dados seja relevante.

## Critérios de qualidade

- **Versão do esquema identificada** — versões diferentes têm estruturas e IDs diferentes
- **Identificadores formais registrados com precisão** — IRDI, ECLASS code, namespace URI: são identificadores formais, erro de digitação invalida o dado
- **Fonte** — portal oficial do padrão, não mapeamentos informais de terceiros
- **Escopo declarado** — qual parte do padrão se aplica ao contexto da tarefa

## Fontes válidas

- Portal oficial eCl@ss (eclass.eu)
- IEC Common Data Dictionary (cdd.iec.ch)
- ISO 10303 Application Protocols (documentos ISO oficiais)
- AutomationML e.V. (automationml.org)
- Portais oficiais de companion specifications OPC UA

## Fontes inválidas

- Mapeamentos informais entre padrões criados por terceiros
- Tabelas de equivalência em papers sem referência ao padrão oficial
- Versões "adaptadas" de padrões sem referência à versão original

## Limites com outros tipos

- **Não é `dados-geometricos`:** o arquivo CAD/STEP de um componente vai em `dados-geometricos`. Aqui coleta-se o esquema ISO 10303 que define como descrever geometria em STEP — o padrão, não o arquivo.
- **Não é `dados-conectividade-comunicacao`:** a infraestrutura de rede que transporta os dados vai em `dados-conectividade-comunicacao`. O modelo de informação OPC UA que define o que os dados significam vai aqui.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos com base no padrão e na tarefa. Exemplos:

- Para eCl@ss: versão (ex: 12.0), classe relevante com ECLASS code, atributos com IRDI, URL no portal oficial
- Para ISO 10303: Application Protocol (AP214, AP242), entidades relevantes, formato de representação (EXPRESS, P21)
- Para OPC UA Information Model: namespace URI, versão, nós relevantes (NodeId), companion specification associada
