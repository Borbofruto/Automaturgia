# Tipo de Dado: `parametros-ventosa`

## Descrição

Parâmetros técnicos de ventosas individuais usadas em garras de vácuo para paletização. Cobre geometria, materiais, faixa de operação e dados de desempenho declarados pelo fabricante. Não inclui arquitetura da garra (ver `arquitetura-garra-vacuo`) nem dados do sistema pneumático (ver `sistema-vacuo-pneumatico`).

---

## Campos a coletar

| Campo | Descrição | Unidade | Estado típico |
|---|---|---|---|
| fabricante | Nome do fabricante OEM | — | confirmado |
| modelo | Referência exata do modelo (número de parte) | — | confirmado |
| diametro_nominal | Diâmetro nominal da ventosa | mm | confirmado |
| diametro_real | Diâmetro real de contato (pode diferir do nominal) | mm | confirmado / nao-verificavel |
| perfil | Perfil da ventosa (flat, bellows 1.5, bellows 2.5, bellows 3.5, oval) | — | confirmado |
| material_lábio | Material de contato com o produto (NBR, silicone, poliuretano, EPDM, Viton, etc.) | — | confirmado |
| material_corpo | Material do corpo da ventosa | — | confirmado |
| forca_sustentacao_nominal | Força de sustentação declarada pelo fabricante em condição padrão | N | confirmado |
| pressao_operacao_nominal | Pressão de vácuo nominal de operação | kPa / mbar | confirmado |
| pressao_maxima_admissivel | Pressão máxima admissível (não ultrapassar) | kPa / mbar | confirmado |
| temperatura_min | Temperatura mínima de operação | °C | confirmado |
| temperatura_max | Temperatura máxima de operação | °C | confirmado |
| certificacao_alimentar | Certificação para contato com alimentos (FDA, EU 10/2011) | — | confirmado / nao-aplicavel |
| conexao_tipo | Tipo de conexão pneumática (rosca macho/fêmea, diâmetro) | — | confirmado |
| conexao_tamanho | Tamanho da conexão (G1/8, M5, etc.) | — | confirmado |
| altura_montagem | Altura total montada (ventosa + conector) | mm | confirmado |
| peso | Peso da ventosa | g | confirmado |
| vida_util_ciclos | Vida útil declarada em número de ciclos | ciclos | confirmado / nao-verificavel |
| compatibilidade_superficies | Superfícies para as quais a ventosa é declarada compatível | — | confirmado |
| incompatibilidade_superficies | Superfícies para as quais o fabricante desaconselha o uso | — | confirmado / nao-verificavel |
| numero_foles | Número de foles (para ventosas bellows) | — | confirmado / nao-aplicavel |

---

## Fontes válidas

- Datasheet oficial do fabricante (PDF ou página do produto no site OEM)
- Catálogo técnico do fabricante com especificações por modelo
- Manual de seleção do fabricante com tabelas de força por pressão e diâmetro

---

## Fontes inválidas

- Distribuidores sem documentação OEM
- Fóruns, vídeos, tutoriais
- Fichas de segurança (FISPQ/SDS) — contêm dados químicos, não de desempenho
- Valores interpolados de tabelas de modelos similares sem fonte explícita

---

## Regras de qualidade

1. `diametro_nominal` e `diametro_real` são campos distintos — não substituir um pelo outro.
2. `forca_sustentacao_nominal` deve sempre vir acompanhada das condições: pressão de vácuo e orientação de força (vertical / horizontal).
3. Certificações alimentares: se o fabricante não declara, use `nao-verificavel` — não infira da composição do material.
4. Força de sustentação declarada para superfícies lisas não pode ser extrapolada para superfícies porosas ou corrugadas.
5. Se houver variações de modelo (NBR vs silicone, mesmo diâmetro), cada variação é um registro separado.

---

## Armadilhas comuns

- **Força ≠ capacidade de carga efetiva:** A força nominal é em condição controlada (superfície lisa, pressão estável). Não extrapolar para condições reais de paletização.
- **Diâmetro de catálogo vs diâmetro de contato:** Ventosas bellows podem ter diâmetro externo maior que o diâmetro efetivo de vedação. Verificar qual o fabricante declara.
- **Temperatura e material:** Silicone suporta temperaturas mais altas que NBR. Não assumir que modelos com o mesmo número de parte mas material diferente têm a mesma faixa de temperatura.
- **Vida útil em ciclos:** Dado raramente disponível em datasheet; mais comum em publicações técnicas do fabricante. Se não encontrado, `NULL-MISSING`.
