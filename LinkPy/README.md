# 🔗 Encurtador de Links

Encurta URLs usando a API gratuita do [is.gd](https://is.gd). Mantém histórico local em JSON.

## Funcionalidades

- **Encurtar** qualquer URL
- **Histórico** dos links encurtados (salvo em `historico.json`)
- **Limpar** histórico

## Como executar

### Pré-requisitos

```bash
pip install requests
```

### Execução

```bash
python encurtador.py
```

## Exemplo de uso

```
=== ENCURTADOR DE LINKS ===
1 - Encurtar link
2 - Ver histórico
3 - Limpar histórico
4 - Sair
Escolha: 1
Link: https://github.com
Link encurtado: https://is.gd/SzNOOZ

Escolha: 2

  1. Original: https://github.com
     Curto:   https://is.gd/SzNOOZ
```

## Estrutura do código

| Função | Descrição |
|---|---|
| `carregar()` | Lê o histórico do JSON |
| `salvar()` | Grava o histórico no JSON |
| `encurtar()` | Chama a API do is.gd e retorna a URL encurtada |
| `menu()` | Exibe o menu de opções |

## API utilizada

- [is.gd](https://is.gd) — sem cadastro, sem chave de API, gratuita
