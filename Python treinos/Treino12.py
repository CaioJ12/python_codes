#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
def comp(number):
    if number > 0:
        print(f'{number} é um número positivo')
        return
    print(f'aparentemente {number} é um número negativo')
    
#----------------------------------------------------------------------------------------

comparacente = int(input('Por favo insira um numero: '))

comp(comparacente)
    