#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
import math

def area_quadrado(lado):
 result = math.pow(lado,2)
 return result

#-------------------------------------------------------------------------------------------------------
roxo = '\033[1;35m'

entrada= float(input("por favor digite o valor de um dos lados do seu quadrado: "))

# Exemplo de como aplicar a cor no texto corretamente
print(f'{roxo}A area calculada foi de /033[m {area_quadrado(entrada)}')

print(f'E o dobro da area é de {(area_quadrado(entrada))*2}')