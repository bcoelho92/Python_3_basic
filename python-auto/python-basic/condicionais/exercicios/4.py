# Peça ao usuário uma nota de 0 a 10 para um filme. Classifique a avaliação assim:

# Nota 9 ou 10: "Excelente!"

# Nota 7 ou 8: "Muito bom"

# Nota 5 ou 6: "Regular"

# Menor que 5: "Ruim"

nota = float(input("De 0 a 10, qual nota você dá para esse filme?: "))
# nota = 8

if nota >= 9:
    print("Excelente!")
elif nota >= 8:
    print("Muito bom!")
elif nota >= 6:
    print("Regular.")
elif nota < 5:
    print("Ruim.")
