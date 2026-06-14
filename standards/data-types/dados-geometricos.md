# dados-geometricos — Tipo de Dado

## Descrição
Modelos digitais e descrições formais da geometria de um componente: arquivos CAD, URDF, STEP, envelope de trabalho, dimensões de montagem e footprint. Serve como base para simulação, planejamento de layout e análise de alcance.

## Campos a coletar

| Campo | Obrigatório | Tipo | Notas |
|---|---|---|---|
| Componente (fabricante + modelo) | S | Texto | — |
| Formato do arquivo | S | Texto | STEP, IGES, STL, URDF, SDF, DXF, etc. |
| Versão / revisão do arquivo | S | Texto | Data ou número de revisão |
| URL / fonte de download | S | URL + data acesso | Link oficial |
| Software de origem (se relevante) | N | Texto | SolidWorks, CATIA, FreeCAD, etc. |
| Dimensões de envelope de trabalho | N | mm | Descrição do volume alcançável (shape, raio mín/máx) |
| Footprint de montagem | N | mm × mm | Área ocupada na base |
| Altura total (robô estendido) | N | mm | — |
| Distância flange–base (max extensão) | N | mm | — |
| Sistema de coordenadas de referência | N | Texto | Declarar convenção (base frame, world frame) |
| Compatibilidade de simulador | N | Lista | ROS/Gazebo, RoboDK, Webots, CoppeliaSim, etc. |
| Licença de uso do arquivo | N | Texto | Se declarada pelo fabricante |

## Fontes válidas (em ordem de prioridade)
1. Portal oficial de download do fabricante (CAD library)
2. Repositório GitHub oficial do fabricante (URDF, STEP)
3. ROS-Industrial repository (verificar se é oficial ou contribuição da comunidade)
4. Datasheet com dimensões certificadas pelo fabricante

## Fontes inválidas
- GrabCAD ou sites de compartilhamento de CAD por terceiros (não verificáveis)
- URDF gerados por terceiros sem referência ao fabricante
- Modelos extraídos de vídeos ou imagens

## Regras de qualidade
- Registrar versão do arquivo — geometria pode mudar entre revisões mecânicas
- Envelope de trabalho: especificar se é dado gráfico (extraído de figura) ou numérico (tabela) — confiabilidade diferente
- Compatibilidade de simulador declarada pelo fabricante ≠ funcionamento garantido na versão atual do simulador
- Dados ausentes: `NULL-MISSING`
- Se apenas o envelope gráfico estiver disponível (sem coordenadas numéricas), registrar como `nao-verificavel` para campos numéricos

## Armadilhas comuns
- URDF de repositórios da comunidade frequentemente têm parâmetros de inércia incorretos — verificar se fabricante disponibiliza versão oficial
- STEP e URDF podem ter sistemas de coordenadas diferentes — nunca assumir alinhamento sem verificar
- Envelope de trabalho "reachable" vs. "dexterous workspace" são conceitos diferentes — registrar qual está sendo descrito
