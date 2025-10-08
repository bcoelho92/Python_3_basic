'''
Crie um sistema de votação onde o usuário escolhe entre:

1."Pizza"

2."Hambúrguer"

3."Sair"

Enquanto ele não digitar "3", continue perguntando

No final, mostre quantos votos cada item recebeu
'''
voto = 0
votacao = {
    'Pizza': 0,
    'Hambúrguer': 0
}

while voto != 3:
    voto = int(input('''
    Qual a melhor comida?
        
    Digite 1 para Pizza
    Digite 2 para Hambúrguer
    digite 3 para sair 

    Qual é o seu voto? '''))

    if voto == 1:
        votacao['Pizza'] += 1
    elif voto == 2:
        votacao['Hambúrguer'] += 1
    elif voto not in (1,2,3):
        print(f'''\n  !!! Opção de Voto invalida !!!''')
        continue
print(f'''
    Contagem dos votos:
      
    Pizza: {votacao["Pizza"]}
    Hambúrguer: {votacao["Hambúrguer"]}

    Obrigado por participar!
''') 