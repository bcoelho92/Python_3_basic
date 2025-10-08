# Usando loops, peça 5 números ao usuário (com input()), some todos e mostre o resultado.

resultado = 0
for c in range(1,6):
    numero = int(input('Digite um numero: '))
    resultado += numero

print(f'Essa é a soma dos seus numeros: {resultado}')
