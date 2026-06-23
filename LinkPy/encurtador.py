import requests
import json
import os

ARQUIVO = "historico.json"


def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar(historico):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=2, ensure_ascii=False)


def encurtar(url):
    api = f"https://is.gd/create.php?format=json&url={url}"
    try:
        r = requests.get(api, timeout=10)
        dados = r.json()
        if "shorturl" in dados:
            return dados["shorturl"]
        return f"Erro: {dados.get('errormessage', 'desconhecido')}"
    except Exception as e:
        return f"Erro: {e}"


def menu():
    print("\n=== ENCURTADOR DE LINKS ===")
    print("1 - Encurtar link")
    print("2 - Ver historico")
    print("3 - Limpar historico")
    print("4 - Sair")


historico = carregar()

while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        url = input("Link: ").strip()
        if url:
            print("Encurtando...")
            resultado = encurtar(url)
            print(f"Link encurtado: {resultado}")
            historico.append({"original": url, "curto": resultado})
            salvar(historico)
        else:
            print("Link invalido.")

    elif opcao == "2":
        if not historico:
            print("Nenhum link encurtado ainda.")
        else:
            print()
            for i, item in enumerate(historico, 1):
                print(f"  {i}. Original: {item['original']}")
                print(f"     Curto:   {item['curto']}")
                print()

    elif opcao == "3":
        historico = []
        salvar(historico)
        print("Historico limpo.")

    elif opcao == "4":
        print("Ate logo!")
        break

    else:
        print("Opcao invalida.")
