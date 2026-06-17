# 📋 Lista de Tarefas

Gerenciador de tarefas via terminal com persistência em JSON. Adicione, conclua e remova tarefas de forma simples e rápida.

## Funcionalidades

- **Adicionar** novas tarefas
- **Listar** tarefas com status (concluída `/` pendente)
- **Concluir** tarefas existentes
- **Deletar** tarefas
- **Persistência** automática em `tarefas.json`

## Como executar

```bash
python tarefas.py
```

> Compatível com Python 3.x — sem dependências externas.

## Exemplo de uso

```
=== LISTA DE TAREFAS ===
1 - Listar tarefas
2 - Adicionar tarefa
3 - Marcar como concluída
4 - Deletar tarefa
5 - Sair
Escolha: 2
  Nome da tarefa: Estudar Python
  Tarefa 'Estudar Python' adicionada!

Escolha: 1
  1. [ ] Estudar Python

Escolha: 3
  1. [ ] Estudar Python
  Número da tarefa concluída: 1
  Tarefa 'Estudar Python' concluída!

Escolha: 1
  1. [x] Estudar Python

Escolha: 5
  Até logo!
```

## Estrutura do código

| Função | Descrição |
|---|---|
| `carregar()` | Lê as tarefas do arquivo JSON |
| `salvar()` | Grava as tarefas no arquivo JSON |
| `listar()` | Exibe todas as tarefas com numeração e status |
| `adicionar()` | Cria uma nova tarefa |
| `concluir()` | Marca uma tarefa como concluída |
| `deletar()` | Remove uma tarefa |
| `menu()` | Exibe o menu de opções |

## Dados

As tarefas são salvas no arquivo `tarefas.json` na mesma pasta do script:

```json
[
  { "nome": "Estudar Python", "feita": true },
  { "nome": "Criar projeto", "feita": false }
]
```
