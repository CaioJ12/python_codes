def salario(G_hora, T_hora):
    result = G_hora * T_hora
    return result

def color(salario):
    # Definindo cores
    if salario < 1400:
        return '\033[1;31m'  # Cor vermelha para salários abaixo de 1400
    else:
        return '\033[1;32m'  # Cor verde para salários acima de 1400
    
def alert(total):
    if total < 1400:
        print('\033[1;30;41mAtenção, o salário calculado parece estar abaixo do mínimo, a tirania é inerente ao sistema\033[m')

#---------------------------------------

G_hora = float(input('Por favor informe a sua relação "salário por hora": \n'))
T_hora = float(input('\nPor favor informe o número de horas trabalhadas: \n'))

total = salario(G_hora, T_hora)

# Exibe o salário com a cor correta
print(f'O seu saldo do mês será de: {color(total)} {total}\033[m')

alert(total)