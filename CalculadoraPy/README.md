# 🧮 Calculadora

Calculadora de terminal em Python com as quatro operações básicas, tratamento de erros e interface interativa por menu.

---

## ✨ Funcionalidades

- Soma, subtração, multiplicação e divisão
- Tratamento de **divisão por zero**
- Validação de entrada (rejeita valores não numéricos)
- Loop contínuo até o usuário escolher sair

---

## 🖥️ Exemplo de uso

```
=== CALCULADORA ===
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
5 - Sair
Escolha uma opção: 1
Primeiro número: 10
Segundo número: 5
10.0 + 5.0 = 15.0

=== CALCULADORA ===
...
Escolha uma opção: 4
Primeiro número: 8
Segundo número: 0
Erro: divisão por zero!

=== CALCULADORA ===
...
Escolha uma opção: 5
Até logo!
```

---

## 🚀 Como executar

### Pré-requisitos

- Python 3.x instalado

### Execução

```bash
python calculadora.py
```

---

## 📁 Estrutura do projeto

```
.
└── calculadora.py   # Código-fonte principal
```

---

## 🛠️ Tecnologias

- **Linguagem:** Python 3
- Sem dependências externas — apenas a biblioteca padrão

---

## 📌 Observações

- Os números são aceitos como `float`, suportando valores decimais.
- Entradas inválidas (letras, símbolos) são capturadas com `try/except ValueError` e não encerram o programa.