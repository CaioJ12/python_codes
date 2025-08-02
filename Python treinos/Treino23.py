palavra_secreta = 'perfume'
letra_acertada = ''

while True:
    letra_digitada = input('DIGITE UMA LETRA: ')
     
    if len(letra_digitada) > 1 or not letra_digitada.isalpha():
        print("Digite apenas uma letra.")
        continue

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada
        
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            print(letra_secreta)
        else:
            print("*")

