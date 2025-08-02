nome = input('Digita o teu nome: ')
idade = input('Digita a tua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu invertido nome é {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A primeira letra do seu nome é {nome[-1]}')
    
    if ' ' in nome:
        print(f'Seu nome contem espaços')    

    else:
        print(f'Seu nome não contém espaços')
        


else:
    print("Deculpe voce deixou campos vazios.")