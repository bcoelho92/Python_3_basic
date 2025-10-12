'''
Crie uma função chamada verificar_par(numero) que retorna:

"Par" se o número for par

"Ímpar" se for ímpar

Peça um número ao usuário com input(), chame a função e mostre o resultado.
'''

def verificar_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# print(f'O numero é {verificar_par(int(input("Digite um numero: ")))}')

numero = int(input("Digite um numero: "))
print(f'O numero {numero} é {verificar_par(numero)}')