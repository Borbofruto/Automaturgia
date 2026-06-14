# solucoes-mercado — Tipo de Dado

## Descrição
Catálogo de produtos e soluções comercialmente disponíveis que atendem a uma função técnica específica. Registra o que existe no mercado, com especificações básicas e disponibilidade — sem avaliação, ranking ou recomendação.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Nome do produto | S | Texto | Nome comercial oficial |
| Fabricante | S | Texto | — |
| Modelo / SKU | S | Texto | — |
| Categoria / função | S | Texto | Ex: "Cobot 6-DOF payload 10 kg" |
| Especificações-chave | S | Lista | Os parâmetros mais relevantes para a função (3-5 specs) |
| Disponibilidade geográfica | N | Texto | Brasil / América do Sul / Global |
| Distribuidor no Brasil | N | Texto | Se identificado — nome + site |
| Status comercial | S | Texto | Disponível / Descontinuado / Anunciado / Fim de produção |
| Data da consulta | S | Data | — |
| URL do produto | S | URL | Página oficial do fabricante |

## Fontes válidas (em ordem de prioridade)
1. Site oficial do fabricante (página do produto)
2. Portal de distribuidores autorizados com informações verificáveis
3. Catálogo técnico oficial do fabricante (PDF datado)
4. Base de dados setorial (ABIMAQ, IFR, Tecnomatix market data — apenas para existência, não specs)

## Fontes inválidas
- Sites de e-commerce (Mercado Livre, Amazon — specs podem estar incorretas)
- Comparativos de terceiros sem link para fonte primária
- Notícias sobre produtos não lançados sem anúncio oficial do fabricante

## Regras de qualidade
- Especificações-chave devem ser as mais relevantes para a função descrita na tarefa — não todos os campos do datasheet
- Disponibilidade no Brasil deve ser verificada: muitos produtos têm disponibilidade global mas sem suporte local
- Status "Disponível" deve ser confirmado na data de consulta — linha de produto pode ser encerrada
- Não incluir preço: preços variam e não são dados técnicos
- Não ordenar por preferência — ordenar alfabeticamente ou por fabricante
- Dados ausentes: `NULL-MISSING`

## Armadilhas comuns
- Produtos OEM podem ter modelos com nomes diferentes por região — verificar se são o mesmo produto
- "Disponível globalmente" não significa estoque imediato no Brasil — verificar prazo com distribuidor
- Fabricantes frequentemente lançam sucessores sem descontinuar formalmente o modelo anterior — registrar ambos se encontrados
