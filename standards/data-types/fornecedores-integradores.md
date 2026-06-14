# Tipo de Dado: `fornecedores-integradores`

## Natureza

Dados sobre **empresas que fabricam, distribuem, integram ou suportam** componentes e sistemas técnicos. Registra relações factuais entre empresas e produtos/funções — sem avaliação de qualidade, capacidade ou recomendação.

Todo dado deste tipo responde à pergunta: "quem está envolvido com este produto ou função, e em qual papel?"

Os papéis podem variar: fabricante, distribuidor autorizado, integrador certificado, suporte técnico, OEM, revendedor. O tipo se aplica a qualquer cadeia de fornecimento técnico — não se limita a robótica.

## Critérios de qualidade

- **Papel verificável** — "integrador certificado" deve aparecer na lista oficial do fabricante; não basta a empresa se autodeclarar
- **Cobertura geográfica baseada no que a empresa declara** — não inferida por localização da sede
- **Data de consulta registrada** — relações comerciais mudam (distribuidores perdem autorização, empresas encerram)
- **Sem avaliação** — não há campo de qualidade, experiência, recomendação ou capacidade

## Fontes válidas

- Página de parceiros/distribuidores do fabricante do produto
- Site oficial da empresa
- Catálogos de associações setoriais (ABIMAQ, ABR, etc.)
- Lista de integradores certificados publicada pelo fabricante

## Fontes inválidas

- LinkedIn (informações não verificadas tecnicamente)
- Listas de fornecedores em sites de comparação ou licitação
- Indicações informais sem confirmação por fonte primária

## Limites com outros tipos

- **Não é `solucoes-mercado`:** os produtos em si vão em `solucoes-mercado`. Este tipo coleta quem está na cadeia de fornecimento desses produtos.
- **Não é `casos-aplicacao`:** registros de instalações reais (mesmo que envolvam um integrador) vão em `casos-aplicacao`. Este tipo coleta a empresa e seu papel, não o projeto que executou.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos com base na empresa e na tarefa. Exemplos:

- Para distribuidor autorizado: razão social, papel, marcas representadas, cobertura geográfica, URL, data de consulta
- Para integrador certificado: nome, certificação verificada (com link para lista do fabricante), especialidades declaradas, cobertura
- Para suporte técnico: empresa, tipo de suporte (telefone, campo, remoto), cobertura geográfica, contato público
