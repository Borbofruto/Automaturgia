# software-firmware — Tipo de Dado

## Descrição
Informações sobre software de controle, firmware de equipamento, SDKs, APIs, plugins e changelogs relevantes para um componente específico. Cobre o que existe, qual versão, o que ela faz e onde encontrar — sem avaliação comparativa entre versões.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Componente (fabricante + modelo) | S | Texto | A qual hardware este software pertence |
| Nome do software / firmware | S | Texto | Nome oficial |
| Versão | S | Texto | Número exato (ex: "5.14.3") |
| Data de lançamento | S | Data | DD/MM/AAAA |
| Tipo | S | Texto | Firmware / SDK / API / Plugin / URCap / App |
| Linguagens suportadas | N | Lista | Python, C++, Java, PolyScope, etc. |
| Plataformas suportadas | N | Lista | Windows, Linux, ROS, etc. |
| Funcionalidades principais | N | Lista | Extraídas literalmente das release notes |
| Mudanças em relação à versão anterior | N | Lista | De changelog oficial, sem síntese |
| Compatibilidade declarada (hardware) | N | Texto | Versões de hardware suportadas |
| Compatibilidade declarada (software) | N | Texto | Dependências, versões de OS, libs |
| URL de download / repositório | N | URL | Link oficial, com data de acesso |
| Licença | N | Texto | Proprietária, MIT, Apache, etc. |
| Status | S | Texto | Ativo / LTS / End of Life / Beta |

## Fontes válidas (em ordem de prioridade)
1. Portal oficial de download do fabricante (com versão e data de publicação visíveis)
2. Repositório GitHub oficial do fabricante
3. Release notes / changelog oficial
4. SDK documentation oficial
5. URCap / plugin marketplace do fabricante

## Fontes inválidas
- Repositórios de terceiros não oficiais
- Sites de mirror sem verificação de origem
- Changelog extraído de fóruns ou comentários de issues

## Regras de qualidade
- Sempre registrar versão exata — nunca "versão recente" ou "versão atual"
- Data de acesso é obrigatória para URLs (firmware pode ser atualizado sem aviso)
- Funcionalidades e mudanças devem ser transcritas do changelog, não parafrasadas
- Não sintetizar nem comparar versões — coletar cada versão como registro independente
- Valores ausentes: `NULL-MISSING`
- Se o fabricante não publica changelog público, registrar isso explicitamente como `nao-encontrado`

## Armadilhas comuns
- Versão de SDK e versão de firmware são dados separados — coletar individualmente
- URCaps têm versão própria além da versão de PolyScope compatível — ambas devem ser registradas
- "Versão mais recente" muda ao longo do tempo — sempre fixar a versão coletada e a data
