# Tipo de Dado: `interfaces-compatibilidade`

## Natureza

Dados que descrevem a **relação entre dois objetos específicos** — como eles se conectam, comunicam ou interagem. São dados relacionais: sempre envolvem dois sujeitos (A ↔ B) e descrevem o que acontece na fronteira entre eles.

Todo dado deste tipo responde à pergunta: "como A e B se conectam ou interagem?"

Os objetos podem ser componentes físicos (flange de robô ↔ garra), sistemas de software (controlador ↔ PLC), protocolos (servidor OPC UA ↔ cliente), ou qualquer combinação. O tipo se aplica a qualquer fronteira técnica onde compatibilidade precisa ser verificada.

## Critérios de qualidade

- **Ambos os objetos identificados explicitamente** — fabricante, modelo, versão. Dado de interface sem identificação dos dois lados é inválido.
- **Natureza da interface declarada** — mecânica, elétrica, de comunicação, de software, ou combinação
- **Condição ou restrição** — quando a compatibilidade depende de versão, configuração ou adaptador, isso deve ser registrado
- **Fonte** — documento que confirma a compatibilidade (datasheet de qualquer dos lados, nota de aplicação, certificado de integração)

## Fontes válidas

- Documentação OEM de qualquer dos dois lados que declare compatibilidade com o outro
- Notas de aplicação do fabricante sobre integração entre os dois objetos
- Certificados de integração emitidos por fabricante ou organismo credenciado
- Especificações de protocolo que definam os requisitos de cada lado

## Fontes inválidas

- Afirmações de que "funciona" sem documentação técnica (fórum, experiência de usuário)
- Compatibilidade inferida por semelhança de protocolo sem verificação de implementação específica
- Documentação de uma versão aplicada a outra versão sem confirmação de retrocompatibilidade

## Limites com outros tipos

- **Não é `parametros-componente`:** parâmetros de um componente isolado vão em `parametros-componente`. Este tipo só existe quando há dois objetos e uma fronteira entre eles.
- **Não é `dados-conectividade-comunicacao`:** topologia de rede, endereçamento e configuração de infraestrutura vão em `dados-conectividade-comunicacao`. Este tipo trata da compatibilidade entre dois objetos específicos.
- **Não é `software-firmware`:** versões de software e SDKs vão em `software-firmware`. A compatibilidade entre versão X de um SDK e versão Y de um controlador é `interfaces-compatibilidade`.

## Exemplos de campos (não exaustivo)

O Ordenador determina os campos relevantes com base nos dois objetos e na natureza da interface. Exemplos:

- Para flange mecânico (robô ↔ garra): padrão de furos, diâmetro, torque máximo, pino de centragem
- Para comunicação (CLP ↔ cobot): protocolo suportado, versão, porta, parâmetros de configuração necessários
- Para software (URCap ↔ versão de PolyScope): versão mínima exigida, dependências, restrições conhecidas
- Para elétrico (fonte ↔ atuador): tensão, corrente, tipo de conector, pinagem

A primeira coisa que o Ordenador registra é: "objeto A" e "objeto B". Sem isso, a coleta não começa.
