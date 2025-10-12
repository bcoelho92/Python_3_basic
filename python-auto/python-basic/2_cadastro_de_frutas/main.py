frutas = []

def cadastrar_frutas():
    fruta = input("Digite o nome da fruta: ")
    quantidade = int(input("Digite a quantidade da fruta: "))
    cor = input("Digite a cor da fruta: ")
    data_cadastro = input("Digite a data de cadastro (dd/mm/aaaa): ")

    cadastro = {
        'fruta': fruta,
        'quantidade': quantidade,
        'cor': cor,
        'data_cadastro': data_cadastro
    }

    frutas.append(cadastro)

def list_frutas():
    if len(frutas) == 0:
        print("Frutas não cadastrada.")
        return
    for fruta in frutas:
        print(f'\nFruta: {fruta["fruta"]}\nQuantidade: {fruta["quantidade"]}\nCor: {fruta["cor"]}\nData de Cadastro: {fruta["data_cadastro"]}\n')

while True:
    opcao = int(input("Digite uma opção: "))
    match opcao:
        case 1:
            cadastrar_frutas()
        case 2:
            list_frutas()
        case 0:
            break