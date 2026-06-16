def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def menu():
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Até logo!")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida!")
        continue

    try:
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
    except ValueError:
        print("Erro: digite um número válido!")
        continue

    if opcao == "1":
        resultado = somar(num1, num2)
        operador = "+"
    elif opcao == "2":
        resultado = subtrair(num1, num2)
        operador = "-"
    elif opcao == "3":
        resultado = multiplicar(num1, num2)
        operador = "x"
    elif opcao == "4":
        resultado = dividir(num1, num2)
        operador = "/"

    print(f"{num1} {operador} {num2} = {resultado}")