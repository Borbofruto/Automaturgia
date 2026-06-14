# Tipo de Dado: `dados-geometricos`

## Natureza

Dados que descrevem a **forma, dimensões e representação espacial** de um componente ou sistema. Inclui arquivos de modelo digital (CAD, URDF, STEP) e dados que descrevem limites espaciais como envelope de trabalho, footprint e dimensões de instalação.

Todo dado deste tipo responde à pergunta: "qual é a forma e o espaço que este componente ocupa ou alcança?"

O tipo se aplica a qualquer componente para o qual a geometria seja relevante: robôs, garras, estruturas de suporte, layouts de célula, envelopes de movimento. Não se limita a componentes físicos — pode cobrir representações formais usadas em simulação.

## Critérios de qualidade

- **Componente identificado** — fabricante, modelo, revisão mecânica se aplicável
- **Versão ou data do arquivo/dado** — geometria pode mudar entre revisões
- **Sistema de referência declarado** — qual frame, qual convenção de eixos
- **Fonte** — link oficial com data de acesso, ou documento OEM com página/seção

Dados de envelope extraídos de figuras têm confiabilidade menor que dados numéricos tabelados — declarar qual tipo foi coletado.

## Fontes válidas

- Portal oficial de download do fabricante (CAD library, URDF oficial)
- Repositório GitHub oficial do fabricante
- Datasheet com dimensões certificadas pelo fabricante
- Documentação de simulação oficial do fabricante

## Fontes inválidas

- Sites de compartilhamento de CAD por terceiros (GrabCAD, etc.) sem referência ao fabricante
- URDF gerados por terceiros sem referência ao documento OEM
- Modelos extraídos de imagens ou vídeos

## Limites com outros tipos

- **Não é `parametros-componente`:** alcance declarado como parâmetro de especificação (capacidade) vai em `parametros-componente`. Aqui coleta-se a geometria e o espaço ocupado/percorrido.
- **Não é `modelos-interoperabilidade`:** esquemas formais para intercâmbio de dados (EXPRESS, eCl@ss) vão em `modelos-interoperabilidade`. Aqui coleta-se o arquivo de geometria em si, não o esquema.
- **Não é `dados-layout-infraestrutura`:** dados do ambiente físico da instalação vão em `dados-layout-infraestrutura`. Aqui coleta-se a geometria do componente, não do espaço onde ele opera.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos relevantes com base no componente e na tarefa. Exemplos:

- Para robô articulado: formato e URL do URDF oficial, envelope de trabalho (numérico e/ou gráfico), footprint de base, altura máxima
- Para garra: dimensões externas, área de contato, modelo STEP para verificação de colisão
- Para célula completa: plantas baixas, modelo 3D de layout, cotas de segurança
- Para arquivo CAD: formato, versão, software de origem, sistema de coordenadas declarado
