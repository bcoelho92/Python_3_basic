# Elegibilidade para um Evento (Idade Mínima): Imagine um evento para maiores de 15 anos. Crie um código que pergunte a idade do usuário. Verifique se a idade do usuário é maior ou igual a 15. Se for, exiba "Você pode participar do evento!".

idade = int(input("Digite sua idade: "))
idade_minima = 15 # Fica mais facil de realizar a manutenção do parametro

if idade >= idade_minima:
    print("Você pode participar do evento!")