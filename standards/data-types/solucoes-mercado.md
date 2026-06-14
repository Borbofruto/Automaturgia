# Tipo de Dado: `solucoes-mercado`

## Natureza

Catálogo de **produtos e soluções comercialmente disponíveis** que atendem a uma função técnica específica. Registra o que existe no mercado — sem avaliação, ranking ou recomendação entre produtos.

Todo dado deste tipo responde à pergunta: "quais produtos estão disponíveis comercialmente para executar esta função?"

A função pode ser qualquer coisa: cobot para paletização, sensor de força para montagem, válvula proporcional para vácuo, software de simulação. O tipo não é específico a nenhum domínio — aplica-se a qualquer função técnica para a qual exista oferta de mercado.

## Critérios de qualidade

- **Função declarada explicitamente** — o catálogo deve declarar qual função está sendo coberta (sem isso, a coleção não tem critério de inclusão)
- **Status comercial verificado** — disponível, descontinuado, anunciado — verificado na data de consulta
- **Data de consulta registrada** — disponibilidade muda
- **Especificações de fonte OEM** — não de distribuidores ou e-commerce
- **Sem ranking** — não há coluna de preferência, pontuação ou recomendação

## Fontes válidas

- Site oficial do fabricante (página do produto)
- Catálogo técnico oficial do fabricante com data
- Portal de distribuidores autorizados com especificações verificáveis
- Bases de dados setoriais para existência de produtos (não para especificações)

## Fontes inválidas

- Sites de e-commerce (Amazon, Mercado Livre — specs podem estar incorretas)
- Comparativos de terceiros sem link para fonte primária
- Notícias sobre produtos não lançados sem anúncio oficial do fabricante

## Limites com outros tipos

- **Não é `parametros-componente`:** especificações técnicas detalhadas de um produto específico selecionado vão em `parametros-componente`. Este tipo coleta o panorama de mercado — quais existem e specs básicas para comparação.
- **Não é `fornecedores-integradores`:** quem vende ou integra os produtos vão em `fornecedores-integradores`. Este tipo coleta os produtos em si.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos com base na função e na tarefa. Exemplos:

- Para catálogo de cobots até 10 kg: fabricante, modelo, payload, alcance, IP, status comercial, URL
- Para catálogo de garras de vácuo para paletização: fabricante, modelo, faixa de produtos suportados, configurações disponíveis, status
- Para catálogo de software de simulação robótica: nome, fabricante, plataformas suportadas, tipo de licença, versão atual
