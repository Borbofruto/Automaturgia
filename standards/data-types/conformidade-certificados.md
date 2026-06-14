# Tipo de Dado: `conformidade-certificados`

## Natureza

Registros de **certificados e declarações de conformidade** emitidos para um produto ou componente específico. Documenta o que existe: quem emitiu, quando, com base em quais normas e qual o escopo coberto.

Todo dado deste tipo responde à pergunta: "existe um certificado ou declaração de conformidade para este produto? O que ele cobre e está válido?"

O tipo se aplica a qualquer tipo de certificação técnica: segurança elétrica (CE, UL), qualidade (ISO 9001), segurança funcional (TÜV, SIL), homologação regulatória (INMETRO, FCC, ANATEL), declarações do fabricante (DoC). Não se limita a robótica.

## Critérios de qualidade

- **Produto identificado exatamente** — fabricante, modelo, versão. Um certificado para X.1 não cobre X.2 automaticamente.
- **Número do certificado** — exatamente como emitido, não parafrasado
- **Organismo emitente identificado** — quem emitiu importa (auto-declaração ≠ certificação por terceiro)
- **Escopo declarado** — o que o certificado cobre, incluindo exclusões explícitas
- **Status verificado** — válido, expirado, suspenso, retirado — verificado na base do organismo emitente

Conformidade não é inferida — se não há certificado documentado, o campo recebe `NULL-MISSING` com as bases consultadas.

## Fontes válidas

- Banco de dados público do organismo certificador (UL Product iQ, TÜV database, EU Declaration database)
- Declaração de Conformidade emitida pelo fabricante (DoC/EU Declaration of Conformity)
- Página oficial de compliance do fabricante com número de certificado verificável
- Cópia digital do certificado original fornecida pelo fabricante

## Fontes inválidas

- Afirmações de conformidade sem número de certificado verificável
- Sites de revendedores declarando conformidade por conta própria
- Documentos sem identificação de organismo emitente

## Limites com outros tipos

- **Não é `normas-regulamentacoes`:** normas técnicas em si (ISO, IEC, ABNT) vão em `normas-regulamentacoes`. Este tipo coleta a evidência de conformidade a uma norma por parte de um produto específico.
- **Não é `dados-seguranca-funcionais`:** parâmetros de segurança funcional (PL, SIL) declarados para um sistema vão em `dados-seguranca-funcionais`. O certificado que os atesta vai aqui.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos com base no tipo de certificação e no produto. Exemplos:

- Para certificação CE de cobot: número de certificado, normas cobertas (ISO 10218-1, ISO 13849), organismo (se terceiro), escopo, validade
- Para homologação ANATEL: número de homologação, data, URL na base ANATEL
- Para declaração de conformidade alimentar (FDA, EU 10/2011): documento do fabricante, escopo (quais materiais), data
