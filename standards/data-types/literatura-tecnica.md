# Tipo de Dado: `literatura-tecnica`

## Natureza

Índice de existência de **publicações técnicas** relevantes. Registra que a publicação existe, o que ela aborda e onde encontrar — sem síntese do conteúdo, sem extração de conclusões, sem avaliação de qualidade metodológica.

Todo dado deste tipo responde à pergunta: "esta publicação existe, sobre o que trata, e onde pode ser encontrada?"

O tipo se aplica a qualquer forma de publicação técnica: papers de journal, artigos de conferência, relatórios técnicos, teses, white papers. Não se limita a robótica. É um índice — não é uma revisão bibliográfica.

## Critérios de qualidade

- **Identificação completa** — título exato, autores, veículo de publicação, ano, DOI preferido
- **Status de acesso declarado** — aberto, paywall, repositório institucional (registro independe de ter acesso ao conteúdo)
- **Abstract transcrito literalmente** — nunca parafraseado, nunca resumido pelo Executor
- **Tópicos das keywords da publicação** — não gerados pelo Executor

A publicação é registrada mesmo que o Executor não tenha acesso ao conteúdo completo.

## Fontes válidas

- IEEE Xplore, ACM Digital Library, Scopus, Web of Science
- Google Scholar (para localização — verificar acesso)
- arXiv.org (preprints — verificar se há versão de journal)
- Repositórios institucionais de universidades

## Fontes inválidas

- Sites que oferecem PDFs sem autorização do autor ou editora
- Resumos de terceiros que interpretam o paper

## Limites com outros tipos

- **Não é `desempenho-ensaio`:** um paper que contém resultados de medição: o índice do paper é `literatura-tecnica`; os resultados extraídos do paper são `desempenho-ensaio`. São registros distintos.
- **Não é `normas-regulamentacoes`:** normas técnicas (ISO, IEC, ABNT) têm tipo próprio. Publicações acadêmicas ou técnicas sobre o tema de uma norma são `literatura-tecnica`.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos com base na publicação e na tarefa. Exemplos:

- Para paper de journal: título exato, todos os autores, nome do journal, ano, DOI, status de acesso, abstract literal, keywords
- Para relatório técnico: título, autores/instituição, ano, URL ou número de relatório, status de acesso
- Para tese: título, autor, instituição, ano, URL do repositório, resumo literal
