# normas-regulamentacoes — Tipo de Dado

## Descrição
Identificação e escopo de normas técnicas relevantes: ISO, IEC, ABNT, EN e similares. Este tipo de dado registra o que a norma é e o que ela cobre — nunca interpreta requisitos, nunca extrai obrigações, nunca conclui o que um produto deve fazer para estar em conformidade.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Número da norma | S | Texto | Ex: "ISO 10218-1:2011" |
| Título oficial | S | Texto | Título exato, no idioma original |
| Organismo emitente | S | Texto | ISO, IEC, ABNT, EN, ANSI, etc. |
| Ano de publicação | S | Ano | — |
| Status | S | Texto | Ativa / Supersedida / Retirada / Em revisão |
| Norma que a supersede (se aplicável) | N | Texto | Número da norma mais recente |
| Escopo declarado | S | Texto | Transcrição literal do campo "Scope" da norma |
| Aplicabilidade ao contexto | N | Texto | Como esta norma se aplica à tarefa em questão — descritivo, sem interpretação de requisitos |
| Partes / seções relevantes | N | Lista | Ex: "Parte 2 — Sistemas de robô" |
| Disponibilidade | N | Texto | Paga (ISO Store), gratuita (IEC acesso livre), ABNT Catalogo |
| URL de catálogo | N | URL | Link para página oficial da norma, não para cópia |

## Fontes válidas
1. ISO.org — catálogo oficial ISO
2. IEC Webstore — catálogo oficial IEC
3. ABNT Catálogo — abntcatalogo.abnt.org.br
4. Portais nacionais oficiais (DIN, BSI, ANSI, etc.)
5. Texto da própria norma (quando disponível e autenticado)

## Fontes inválidas
- Resumos de normas em blogs, consultoras ou sites de treinamento
- Wikipedia ou Wikiwand
- PDFs de origem desconhecida
- Textos que parafraseiam ou interpretam a norma

## Regras de qualidade
- O campo "escopo declarado" deve ser transcrição literal — nunca resumo ou paráfrase
- Status deve ser verificado no catálogo oficial: normas são revisadas e substituídas
- Aplicabilidade ao contexto é descritiva ("esta norma cobre robôs colaborativos, o que inclui o sistema X") — nunca normativa ("o sistema X deve atender ao requisito Y")
- Conflito de status entre fontes (ex: duas fontes com datas de publicação diferentes): registrar ambos, criar `registro-conflitos`
- Dados ausentes: `NULL-MISSING`

## Armadilhas comuns
- ISO 10218-1 e ISO 10218-2 são partes distintas — coletar individualmente
- ISO/TS 15066 e ISO 10218-2 tratam de temas sobrepostos mas não são equivalentes — não consolidar
- Normas EN frequentemente adotam texto de ISO/IEC mas podem ter adendos nacionais — registrar se há adendo
- Data de publicação da norma ≠ data de adoção nacional — registrar ambas quando relevante
