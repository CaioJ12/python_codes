lista = [1, 2, 3, 4, 5, 6, 7]

insert = int(input('Qual o index que você deseja inserir = '))
insertValuation = int(input('Qual o valor que você deseja inserir = '))
# conversão aqui

tamanho = len(lista)

try:
    if tamanho != insert:
        resposta = input("O valor inserido está fora de range. Deseja continuar e adicionar o valor ao último índice? [S]im [N]ão: ")
        if resposta.lower() != "s":
            
            print("Operação cancelada.")
        else:
            lista.insert(insert, insertValuation)
    else:
        lista.insert(insert, insertValuation)
    print(lista)
except:
    print("Ocorreu um erro.")
