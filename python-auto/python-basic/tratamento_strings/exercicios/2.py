# Exercício 2 – Pegando um trecho da frase
# Peça ao usuário uma frase e dois números: início e fim. Mostre o fatiamento da frase entre esses índices.

frase = str(input("Digite uma frase: "))
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

print(f"A frase fatiada é: {frase[n1:n2]}")