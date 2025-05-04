palavra = "python"
letras_digitadas = []
chances = 6
ganhou = False
# etapas do boneco (índice 0 = sem erro, índice 6 = enforcado)
boneco = [
        """
         -----
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\  |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\  |
        /    |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========
        """
    ]

while True:
    print(boneco[6 - chances]) # mostra o boneco atual

    for letra in palavra:
        if letra in letras_digitadas:
            print(letra, end= " ")
        else:
            print("_", end= " ")
    print(f"Você tem {chances} chances")
    tentativa = input("Escolha uma letra para advinhar: ")
    letras_digitadas += [tentativa]
    if tentativa not in palavra:
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra not in letras_digitadas:
            ganhou = False

    if chances == 0 or ganhou:
        break

print(boneco[6 - chances])

if ganhou:
    print(f"Parabéns, você ganhou! A palavra era: {palavra}")
else:
    print(f"Você perdeu! A palavra era: {palavra}")