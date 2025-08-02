def choices(numero1, numero2):
    if numero1 > numero2:
        print(f'Hye o numero {numero2} é o maior')
        return
    print(f'teste010203')
    
#--------------------------------------------------

entrada = input('por favor digite dois numeros inteiros separados por espaço: ')
numero1, numero2 = map(int, entrada.split())
choices(numero1,numero2)