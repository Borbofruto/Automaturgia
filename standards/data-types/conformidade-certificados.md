# conformidade-certificados — Tipo de Dado

## Descrição
Registros de certificados e declarações de conformidade emitidos para um componente ou sistema. Documenta o que existe: número do certificado, quem emitiu, quando, com base em quais normas e qual o escopo. Nunca infere status de conformidade a partir de protocolos ou características técnicas.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Componente / produto certificado | S | Texto | Fabricante + modelo + versão exata |
| Tipo de certificação | S | Texto | CE, UL, TÜV, cULus, INMETRO, CB Scheme, etc. |
| Número do certificado | S | Texto | Exatamente como emitido |
| Organismo certificador | S | Texto | TÜV Rheinland, SGS, Bureau Veritas, etc. |
| Data de emissão | S | Data | — |
| Data de validade | N | Data | Se aplicável; `NULL-MISSING` se não tiver |
| Normas cobertas | S | Lista | Cada norma com número e ano |
| Escopo da certificação | S | Texto | O que exatamente está coberto (pode haver exclusões) |
| URL ou referência do certificado | N | URL / ref | Página pública do organismo ou do fabricante |
| Status atual | S | Texto | Válido / Expirado / Suspenso / Retirado |

## Fontes válidas (em ordem de prioridade)
1. Banco de dados público do organismo certificador (ex: UL Product iQ, TÜV database, EU Declaration database)
2. Declaração de Conformidade emitida pelo fabricante (DoC/EU Declaration of Conformity)
3. Página oficial de compliance do fabricante com número de certificado verificável
4. Cópia digital do certificado original fornecida pelo fabricante

## Fontes inválidas
- Afirmações de conformidade sem número de certificado verificável
- Sites de revendedores declarando conformidade por conta própria
- Documentos sem identificação de organismo emitente

## Regras de qualidade
- Nunca inferir conformidade: se não há certificado documentado, o campo fica `NULL-MISSING`
- Escopo pode excluir itens — "certificado CE" pode não cobrir todos os módulos do produto
- Validade deve ser verificada: certificados podem ser retirados sem atualização do site do fabricante
- Versão do produto importa: um certificado para o modelo X.1 não cobre o X.2 automaticamente
- Dados ausentes: `NULL-MISSING` com nota de quais bases de dados foram consultadas

## Armadilhas comuns
- "Marcação CE" não é uma certificação por organismo — é uma auto-declaração do fabricante (exceto para categorias de alto risco)
- INMETRO homologação ≠ certificação de segurança funcional
- Um produto pode ter CE mas não ter aprovação UL, e vice-versa — coletar cada certificação individualmente
- Certificados podem ser reemitidos com novo número quando a norma de referência é atualizada
