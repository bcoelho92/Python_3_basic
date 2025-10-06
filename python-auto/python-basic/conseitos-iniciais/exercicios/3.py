# Crie um código onde o usuário deve digitar três notas escolares e calcular a média delas.

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))

soma = primeira_nota + segunda_nota + terceira_nota
media = soma / 3

print(f"Essa é a media das tres notas: {media}")