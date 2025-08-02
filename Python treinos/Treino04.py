#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def media_semestre (number1,number2,number3,number4):
    media = (number1 + number2 + number3 + number4)/4
    return media

#--------------------------------------------------------------------
try: 
    entrada = input("Digite as 4 notas separadas por espaço: ")
    number1, number2, number3, number4 = map(float, entrada.split())
    print(f'A media total foi {media_semestre(number1,number2,number3,number4):.2f}')

except ValueError: 
    print("por favor, insira apenas 4 valores inteiros ")