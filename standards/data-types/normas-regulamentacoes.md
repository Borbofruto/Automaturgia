# Tipo de Dado: `normas-regulamentacoes`

## Natureza

Identificação e escopo de normas e regulamentos técnicos. Este tipo registra **o que a norma é e o que ela cobre** — nunca interpreta requisitos, nunca extrai obrigações, nunca conclui o que um produto deve fazer para estar em conformidade.

Todo dado deste tipo responde à pergunta: "esta norma existe, o que ela cobre, e qual é o seu status atual?"

O tipo se aplica a qualquer normativo: ISO, IEC, ABNT, EN, ANSI, OSHA, regulamentos de agência, diretivas EU, normas de associações de indústria. Não se limita a robótica — vale para qualquer domínio técnico.

## Critérios de qualidade

- **Identificação completa** — número, organismo emitente, ano de publicação
- **Status verificado** — ativa, supersedida, retirada, em revisão — verificado no catálogo oficial, não em terceiros
- **Escopo transcrito literalmente** — o campo "Scope" da norma copiado como está, sem paráfrase
- **Fonte** — link para a página oficial da norma no catálogo do organismo emitente

A data de verificação do status deve ser registrada — normas são revisadas e substituídas sem aviso.

## Fontes válidas

- ISO.org — catálogo oficial ISO
- IEC Webstore — catálogo oficial IEC
- ABNT Catálogo — abntcatalogo.abnt.org.br
- Portais nacionais oficiais (DIN, BSI, ANSI, etc.)
- Texto da própria norma (quando disponível e autenticado) para transcrição de escopo

## Fontes inválidas

- Resumos de normas em blogs, consultoras ou sites de treinamento
- Wikipedia ou Wikiwand
- PDFs de origem desconhecida
- Textos que parafraseiam ou interpretam a norma

## Limites com outros tipos

- **Não é `conformidade-certificados`:** certificados e declarações de conformidade de um produto específico vão em `conformidade-certificados`. Este tipo coleta a norma em si, não a conformidade a ela.
- **Não é `dados-seguranca-funcionais`:** parâmetros de segurança funcional (PL, SIL) derivados de aplicação de norma vão em `dados-seguranca-funcionais`. Este tipo coleta a norma como documento, não o resultado de sua aplicação.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos relevantes com base na norma e na tarefa. Exemplos:

- Para uma norma ISO: número completo (ex: ISO 10218-1:2011), título oficial, organismo, ano, status, escopo literal, URL de catálogo
- Para uma diretiva EU: número, ano, escopo declarado, estado de transposição nacional, link para jornal oficial
- Para norma ABNT: número, título em português, status, se é adoção de ISO/IEC ou norma original
