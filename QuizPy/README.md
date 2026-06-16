# 🐍 Quiz Python

Quiz de múltipla escolha via terminal para testar conhecimentos básicos de Python.

## Como funciona

O programa apresenta **5 perguntas** sobre fundamentos de Python, uma por vez, com 4 alternativas cada. O usuário digita a letra correspondente à resposta (`a`, `b`, `c` ou `d`) e recebe feedback imediato. Ao final, é exibido o resultado com o percentual de acertos e uma mensagem personalizada.

## Como executar

Não requer instalação de dependências — só o Python padrão.

```bash
python quiz.py
```

> Compatível com Python 3.x.

## Exemplo de uso

```
========================================
        QUIZ - PYTHON
========================================
Responda 5 perguntas sobre Python!

1. Qual comando exibe uma mensagem na tela em Python?
   a) echo
   b) print()
   c) console.log()
   d) write()

Sua resposta (a/b/c/d): b
[OK] Correto!

...

========================================
       RESULTADO FINAL
========================================
Acertos: 4/5 (80%)
Muito bom! Continue estudando!
```

## Temas abordados

- Saída de dados (`print`)
- Tipos de variáveis
- Estruturas de repetição
- Definição de funções
- Operadores de comparação

## Estrutura do código

| Parte | Descrição |
|---|---|
| `perguntas` | Lista de dicionários com pergunta, opções e resposta correta |
| Loop principal | Itera sobre as perguntas, coleta e valida a resposta do usuário |
| Resultado final | Calcula percentual de acertos e exibe mensagem de desempenho |

## Adicionando novas perguntas

Basta inserir um novo dicionário na lista `perguntas` seguindo o padrão:

```python
{
    "pergunta": "Sua pergunta aqui?",
    "opcoes": ["a) Opção 1", "b) Opção 2", "c) Opção 3", "d) Opção 4"],
    "resposta": "a"  # letra da alternativa correta
}
```
