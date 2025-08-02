# Jogo: adivinhe a palavra secreta

PALAVRA_SECRETA = "Eclair"
palavra_format = "*" * len(PALAVRA_SECRETA)
tentativas = 0
letra_inserida = ""

while True:

    print("A palavra tem", len(PALAVRA_SECRETA), "letras.")
    print("Palavra atual:", palavra_format)

    while True:
        letra_inserida = input("Digite uma letra: ").lower()

        if len(letra_inserida) != 1 or not letra_inserida.isalpha():
            print("Digite apenas uma letra.")
            continue

        tentativas += 1
        nova_palavra_format = ""

        for i in range(len(PALAVRA_SECRETA)):
            letra = PALAVRA_SECRETA[i].lower()
            if letra == letra_inserida:
                nova_palavra_format += PALAVRA_SECRETA[i]  # Mantém maiúsculas
            else:
                nova_palavra_format += palavra_format[i]

        if nova_palavra_format == palavra_format:
            print("Letra incorreta!")
        else:
            print("Boa! Letra correta!")

        palavra_format = nova_palavra_format
        print("Palavra atual:", palavra_format)
        print(f"Tentativas até agora: {tentativas}")

        if palavra_format.lower() == PALAVRA_SECRETA.lower():
            print("\nParabéns! Você descobriu a palavra!")
            print(f"Você acertou em {tentativas} tentativas.")
            break

    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        print("Até a próxima!")
        break