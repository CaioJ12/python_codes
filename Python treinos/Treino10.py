#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
def pesoIdeal(altura):
    result = (72.7*altura) - 58
    print(f'o seu peso ideal seria: {result}')
    
#------------------------------------------

altura = float(input('Por favor insira aqui a sua altura: '))
pesoIdeal(altura)