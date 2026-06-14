# fornecedores-integradores — Tipo de Dado

## Descrição
Dados sobre empresas que fabricam, distribuem, integram ou suportam componentes e sistemas relevantes. Registra relações factuais entre empresas e produtos/funções — sem avaliação de qualidade, capacidade ou recomendação.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Nome da empresa | S | Texto | Razão social ou nome comercial |
| Papel | S | Texto | Fabricante / Distribuidor / Integrador / Suporte técnico / OEM |
| Produtos ou marcas representados | S | Lista | — |
| Cobertura geográfica | S | Texto | Brasil / estado(s) / América do Sul / global |
| Site oficial | S | URL | — |
| Contato técnico (se público) | N | Texto | E-mail ou formulário de contato |
| Certificações relevantes | N | Lista | Ex: UR Certified Integrator, FANUC Authorized Distributor |
| Data da consulta | S | Data | — |

## Fontes válidas (em ordem de prioridade)
1. Página de parceiros/distribuidores do fabricante do produto
2. Site oficial da empresa
3. Catálogos de associações setoriais (ABIMAQ, ABR — Associação Brasileira de Robótica)
4. Certificação verificável pelo fabricante (ex: lista de integradores certificados UR no site da Universal Robots)

## Fontes inválidas
- LinkedIn (informações não verificadas tecnicamente)
- Listas de fornecedores em sites de comparação ou licitação
- Indicações informais sem confirmação por fonte primária

## Regras de qualidade
- Papel declarado deve ser verificável: "integrador certificado" deve aparecer na lista oficial do fabricante
- Não incluir avaliações de qualidade, experiência, capacidade ou histórico de projetos
- Cobertura geográfica deve ser baseada no que a empresa declara, não em inferências
- Se a empresa tem múltiplos papéis (distribuidor E integrador), registrar cada papel separadamente
- Dados ausentes: `NULL-MISSING`

## Armadilhas comuns
- "Parceiro" e "distribuidor autorizado" têm significados diferentes dependendo do fabricante — não normalizar
- Integradores independentes podem trabalhar com múltiplas marcas — listar todas que aparecem na fonte
- Contato de contato pode mudar — sempre registrar data da consulta
