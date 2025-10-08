# teste menu

# # opcao = 3
# opcao = int(input("escolha uma opção de 1 a 3: "))
# match opcao:
#     case 1:
#         print("Escolheu a opção 1!")
#     case 2:
#         print("Escolheu a opção 2!")
#     case 3:
#         print("Escolheu a opção 3!")
#     case _:
#         print("opção invalida.")

# teste Notas

# nota = 7
nota = int(input("Qual é a suua nota na prova: "))
match nota:
    case 10 | 9:
        print("Excelente, parabens!")
    case 8 | 7:
        print("Muito bem, parabens!")
    case 6 | 5:
        print("Da para melhorar.")
    case 4 | 3 | 2 | 1 | 0:
        print("Reprovado!")
    case _:
        print("Nota invalida!")