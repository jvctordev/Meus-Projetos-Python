# 🌤️ Previsão do Tempo

App CLI que consulta a temperatura e condições climáticas de qualquer cidade do mundo usando a API pública [wttr.in](https://wttr.in).

## Como funciona

O usuário digita o nome de uma cidade e o programa exibe:
- Temperatura atual (°C)
- Sensação térmica
- Descrição do céu (ensolarado, nublado, etc.)
- Umidade relativa do ar
- Velocidade e direção do vento

## Como executar

### Pré-requisitos

- Python 3.x instalado
- Biblioteca `requests`

Instale a dependência:

```bash
pip install requests
```

### Execução

```bash
python clima.py
```

## Exemplo de uso

```
=== PREVISAO DO TEMPO ===
Digite o nome da cidade (ou 'sair'): São Paulo

========================================
  CLIMA EM SÃO PAULO - Brazil
========================================
  Temperatura:   22°C
  Sensação:      24°C
  Céu:           Sunny
  Umidade:       43%
  Vento:         6 km/h (SSW)
========================================

Digite o nome da cidade (ou 'sair'): sair
Até logo!
```

## Estrutura do código

| Parte | Descrição |
|---|---|
| `buscar_clima()` | Função que faz a requisição à API e exibe os dados |
| Loop principal | Lê cidades do usuário até ele digitar "sair" |
| Tratamento de erros | Captura falhas de conexão com `try/except` |

## API utilizada

- [wttr.in](https://wttr.in) — API pública gratuita, sem necessidade de cadastro ou chave de acesso
- Formato: JSON (`?format=j1`)
- Idioma: português (`&lang=pt`)