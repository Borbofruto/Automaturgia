# Tipo de Dado: `software-firmware`

## Natureza

Dados sobre **artefatos de software e firmware** associados a um componente ou sistema: o que existe, em qual versão, o que cada versão muda, e quais são as dependências e restrições de uso.

Todo dado deste tipo responde à pergunta: "qual software/firmware existe, em que versão, e o que isso implica?"

Cobre desde firmware embarcado em componentes (cobot, sensor, CLP) até software de desenvolvimento (SDKs, extensões, bibliotecas), passando por ferramentas de configuração e ambientes de execução.

## Critérios de qualidade

- **Versão identificada com precisão** — número de versão exato, não "versão atual" ou "última versão"
- **Data de referência** — a versão coletada estava vigente em qual data (software muda)
- **Fonte** — release notes oficiais, changelog, ou documentação do fabricante que mencione a versão
- **Escopo declarado** — o que a versão cobre (quais dispositivos, quais funcionalidades)

Para changelogs e release notes: transcrever o conteúdo relevante literalmente — não resumir nem interpretar.

## Fontes válidas

- Release notes e changelogs oficiais do fabricante
- Documentação de SDK publicada pelo fabricante com número de versão
- Portal de downloads oficial com data de acesso
- Registro de versão no próprio dispositivo (screenshot ou log — registrar data e contexto)

## Fontes inválidas

- Repositórios de terceiros que redistribuem software sem controle de versão rastreável
- Fóruns e comunidades para dados de versão
- "Versão mais recente" sem identificação exata
- Comparações de versão feitas por terceiros sem referência à documentação original

## Limites com outros tipos

- **Não é `interfaces-compatibilidade`:** a compatibilidade entre versão X e dispositivo Y é `interfaces-compatibilidade`. Aqui coleta-se o que existe e o que cada versão contém.
- **Não é `parametros-componente`:** capacidades operacionais do componente (payload, alcance) são `parametros-componente`. O firmware que habilita uma funcionalidade é `software-firmware`.
- **Não é `processos-procedimentos`:** o procedimento de atualização de firmware é `processos-procedimentos`. A versão do firmware a instalar é `software-firmware`.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos relevantes com base no software/firmware e na tarefa. Exemplos:

- Para firmware de cobot: versão, data de lançamento, dispositivos suportados, breaking changes
- Para SDK: versão, linguagens suportadas, dependências, data de lançamento, EOL se declarado
- Para extensão de software (URCap, plugin): versão, requisito de ambiente mínimo, funcionalidades incluídas
- Para ferramenta de configuração: versão, sistemas operacionais suportados, restrições de compatibilidade
