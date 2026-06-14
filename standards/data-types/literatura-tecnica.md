# literatura-tecnica — Tipo de Dado

## Descrição
Índice de existência de publicações técnicas relevantes: papers, artigos de conferência, relatórios técnicos, teses, white papers. Registra que a publicação existe, o que ela aborda e onde encontrar — sem síntese do conteúdo, sem extração de conclusões, sem avaliação de qualidade metodológica.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Título | S | Texto | Título exato |
| Autor(es) | S | Lista | Sobrenome, Nome — todos os autores |
| Tipo de publicação | S | Texto | Journal article / Conference paper / Technical report / Thesis / White paper |
| Veículo de publicação | S | Texto | Nome do journal, conferência ou instituição |
| Ano | S | Ano | — |
| DOI ou URL | S | DOI preferido; URL como alternativa | — |
| Acesso | S | Texto | Aberto / Restrito (paywall) / Repositório institucional |
| Resumo (abstract) | N | Texto | Transcrição literal do abstract da publicação — nunca paráfrase |
| Tópicos principais | N | Lista | Extraídos das keywords da publicação |
| Relação com o contexto da tarefa | N | Texto | Qual tipo de dado esta referência suporta — ex: "contém parâmetros DH do UR5" |

## Fontes válidas para localização de publicações
1. IEEE Xplore (papers de engenharia)
2. Google Scholar (localização; verificar acesso)
3. Scopus / Web of Science
4. arXiv.org (preprints)
5. Repositórios institucionais de universidades
6. ACM Digital Library

## Fontes inválidas
- Sites que oferecem PDFs sem autorização do autor ou editora
- Resumos de terceiros que interpretam o paper

## Regras de qualidade
- Abstract deve ser transcrição literal — nunca síntese ou interpretação própria
- DOI é preferido a URL porque URLs de journals mudam; DOI é permanente
- "Acesso restrito" não impede o registro — registrar mesmo sem ter acesso ao conteúdo completo
- Não incluir avaliação do paper (metodologia boa/ruim, resultado importante/irrelevante)
- Tópicos principais: usar as keywords da publicação, não gerar keywords próprias
- Dados ausentes: `NULL-MISSING`

## Armadilhas comuns
- Preprints (arXiv) podem ter versões revisadas publicadas em journal — verificar se há versão publicada e registrar ambas
- Papers com mesmo título e autores podem ser versões de conferência e journal do mesmo trabalho — registrar separadamente
- "Citado por X papers" não é um dado a coletar — relevância não é julgada neste tipo de dado
