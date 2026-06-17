import json
import os

ARQUIVO = "tarefas.json"


def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=2, ensure_ascii=False)


def listar(tarefas):
    if not tarefas:
        print("  Nenhuma tarefa cadastrada.")
        return

    for i, t in enumerate(tarefas, 1):
        status = "[x]" if t["feita"] else "[ ]"
        print(f"  {i}. {status} {t['nome']}")


def adicionar(tarefas):
    nome = input("  Nome da tarefa: ").strip()
    if nome:
        tarefas.append({"nome": nome, "feita": False})
        salvar(tarefas)
        print(f"  Tarefa '{nome}' adicionada!")
    else:
        print("  Nome invalido.")


def concluir(tarefas):
    listar(tarefas)
    try:
        idx = int(input("  Numero da tarefa concluida: ")) - 1
        if 0 <= idx < len(tarefas):
            tarefas[idx]["feita"] = True
            salvar(tarefas)
            print(f"  Tarefa '{tarefas[idx]['nome']}' concluida!")
        else:
            print("  Numero invalido.")
    except ValueError:
        print("  Digite um numero.")


def deletar(tarefas):
    listar(tarefas)
    try:
        idx = int(input("  Numero da tarefa para deletar: ")) - 1
        if 0 <= idx < len(tarefas):
            removida = tarefas.pop(idx)
            salvar(tarefas)
            print(f"  Tarefa '{removida['nome']}' removida!")
        else:
            print("  Numero invalido.")
    except ValueError:
        print("  Digite um numero.")


def menu():
    print("\n=== LISTA DE TAREFAS ===")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Marcar como concluida")
    print("4 - Deletar tarefa")
    print("5 - Sair")


tarefas = carregar()

while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        listar(tarefas)
    elif opcao == "2":
        adicionar(tarefas)
    elif opcao == "3":
        concluir(tarefas)
    elif opcao == "4":
        deletar(tarefas)
    elif opcao == "5":
        print("Ate logo!")
        break
    else:
        print("Opcao invalida.")