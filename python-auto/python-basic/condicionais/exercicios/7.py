# Peça para o usuário digitar um meio de transporte. Mostre uma mensagem conforme a entrada:

# "carro" → "Veículo terrestre"

# "bicicleta" → "Transporte sustentável"

# "avião" ou "helicóptero" → "Transporte aéreo"

# Qualquer outro → "Transporte desconhecido"

opcao = str(input(
    ''' 
    Meios de transporte:      
        - carro
        - bicicleta
        - avião
        - helicóptero 

    Digite um meio de transporte: 
'''))

match opcao:
    case "carro":
        print("Veículo terrestre")
    case "bicicleta":
        print("Transporte sustentável")
    case "avião" | "helicóptero":
        print("Transporte aéreo")
    case _:
        print("Transporte desconhecido")