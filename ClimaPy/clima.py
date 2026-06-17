import requests

def buscar_clima(cidade):
    tentar_urls = [
        f"https://wttr.in/{cidade}?format=j1&lang=pt",
        f"http://wttr.in/{cidade}?format=j1&lang=pt",
    ]

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    dados = None
    for url in tentar_urls:
        try:
            resposta = requests.get(url, headers=headers, timeout=10)
            dados = resposta.json()
            break
        except requests.exceptions.SSLError:
            continue
        except Exception as e:
            print(f"Erro: {type(e).__name__} - {e}")
            return

    if not dados:
        print("Nao foi possivel conectar ao servidor do clima.")
        return

    clima = dados["current_condition"][0]
    local = dados["nearest_area"][0]["areaName"][0]["value"]
    pais = dados["nearest_area"][0]["country"][0]["value"]

    temp = clima["temp_C"]
    sensacao = clima["FeelsLikeC"]
    descricao = clima["weatherDesc"][0]["value"]
    umidade = clima["humidity"]
    vento = clima["windspeedKmph"]
    direcao = clima["winddir16Point"]

    print("\n" + "=" * 40)
    print(f"  CLIMA EM {local.upper()} - {pais}")
    print("=" * 40)
    print(f"  Temperatura:  {temp}°C")
    print(f"  Sensacao:     {sensacao}°C")
    print(f"  Céu:          {descricao}")
    print(f"  Umidade:      {umidade}%")
    print(f"  Vento:        {vento} km/h ({direcao})")
    print("=" * 40 + "\n")


print("=== PREVISAO DO TEMPO ===")

while True:
    cidade = input("Digite o nome da cidade (ou 'sair'): ").strip()

    if cidade.lower() == "sair":
        print("Ate logo!")
        break

    if cidade:
        buscar_clima(cidade)
    else:
        print("Digite um nome valido.")