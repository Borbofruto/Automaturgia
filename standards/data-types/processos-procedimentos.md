# Tipo de Dado: `processos-procedimentos`

## Natureza

Sequências técnicas documentadas para **executar uma operação** em um componente ou sistema. Os passos são coletados como estão na fonte — sem simplificação, sem adaptação, sem inferência de passos ausentes.

Todo dado deste tipo responde à pergunta: "como esta operação é executada, passo a passo, conforme documentado pelo fabricante ou fonte técnica?"

O tipo se aplica a qualquer tipo de operação técnica documentada: calibração, montagem, parametrização, manutenção preventiva, configuração de segurança, comissionamento, atualização de firmware. Não se limita a robótica.

## Critérios de qualidade

- **Componente ou sistema identificado** — fabricante, modelo, versão
- **Versão do documento** — procedimentos mudam entre revisões; versão é obrigatória
- **Passos transcritos literalmente** — não resumidos, não reordenados, não simplificados
- **Avisos de segurança preservados** — se a fonte tem avisos entre os passos, estão no registro
- **Fonte com página ou seção** — o trecho exato de onde veio o procedimento

Passos ausentes não são inferidos. Se o procedimento parece incompleto, o campo recebe `nao-verificavel`.

## Fontes válidas

- Manual técnico oficial do fabricante (com número de revisão)
- Application note ou boletim técnico oficial
- Procedimento validado de laboratório certificado com registro

## Fontes inválidas

- Tutoriais de YouTube ou blogs
- Fóruns técnicos sem referência a documento oficial
- Procedimentos sem identificação de fonte ou versão

## Limites com outros tipos

- **Não é `software-firmware`:** a versão do firmware a instalar é `software-firmware`. O procedimento de como instalar é `processos-procedimentos`.
- **Não é `desempenho-ensaio`:** resultados medidos durante um procedimento são `desempenho-ensaio`. O procedimento em si é `processos-procedimentos`.
- **Não é `dados-seguranca-funcionais`:** parâmetros de segurança funcional (PL, SIL) são `dados-seguranca-funcionais`. O procedimento de configuração de zona de segurança é `processos-procedimentos`.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos com base no procedimento e na tarefa. Exemplos:

- Para procedimento de calibração: nome, componente (fabricante + modelo + versão), ferramentas necessárias, passos literais, avisos de segurança, fonte + página
- Para procedimento de montagem de garra: pré-requisitos, torques declarados, sequência de parafusamento, referência à norma de torque
- Para configuração de parâmetros de segurança: quais parâmetros, em qual interface, em qual sequência, com quais valores — transcritos da fonte
