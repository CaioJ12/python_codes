#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

def convert_temp(temperaturaF):
    temperaturaC = 5*((temperaturaF - 32)/9)
    return temperaturaC
#--------------------------------------------------

#Pedimos o valor da temperatura atual
temperaturaF = int(input('Por favor insira aqui a temperatura atual em Fahrenheit: '))

#mostramos o resultado 
print(f'O resultado convertido em celsius foi de {convert_temp(temperaturaF):.2f}')