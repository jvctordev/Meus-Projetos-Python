perguntas = [
    {
        "pergunta": "Qual comando exibe uma mensagem na tela em Python?",
        "opcoes": ["a) echo", "b) print()", "c) console.log()", "d) write()"],
        "resposta": "b"
    },
    {
        "pergunta": "Qual o tipo da variável `x = 10`?",
        "opcoes": ["a) string", "b) float", "c) int", "d) bool"],
        "resposta": "c"
    },
    {
        "pergunta": "Qual estrutura repete um bloco de código?",
        "opcoes": ["a) if", "b) for", "c) def", "d) import"],
        "resposta": "b"
    },
    {
        "pergunta": "Como se define uma função em Python?",
        "opcoes": ["a) function", "b) def", "c) func", "d) define"],
        "resposta": "b"
    },
    {
        "pergunta": "Qual operador verifica igualdade?",
        "opcoes": ["a) =", "b) ==", "c) !=", "d) ==="],
        "resposta": "b"
    },
]

acertos = 0
total = len(perguntas)

print("=" * 40)
print("        QUIZ - PYTHON")
print("=" * 40)
print(f"Responda {total} perguntas sobre Python!\n")

for i, q in enumerate(perguntas, 1):
    print(f"{i}. {q['pergunta']}")
    for opcao in q["opcoes"]:
        print(f"   {opcao}")

    resposta = input("\nSua resposta (a/b/c/d): ").strip().lower()

    if resposta == q["resposta"]:
        print("[OK] Correto!\n")
        acertos += 1
    else:
        print(f"[X] Errado! A resposta era {q['resposta']}\n")

print("=" * 40)
print("       RESULTADO FINAL")
print("=" * 40)
print(f"Acertos: {acertos}/{total} ({acertos * 100 // total}%)")

if acertos == total:
    print("Perfeito! Voce gabaritou!")
elif acertos >= total * 0.6:
    print("Muito bom! Continue estudando!")
else:
    print("Bons estudos, voce vai melhorar!")