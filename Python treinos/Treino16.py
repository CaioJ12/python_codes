"""Testar se o numero é par ou ímpar"""
try:
    numero = input('Por favor insira um número...: ')
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except:
    print("Valor inválido. Por favor, insira um número inteiro.")
    
"""Código de saudação"""
try:
    horario = input('Por favor informe um horario...: ')
    horario_int = int(horario)
    
    if (horario_int > -1 ) and (horario_int < 12):
        print("Tenha um bom dia...")
    elif (horario_int > 11 ) and (horario_int < 18):
        print("tenha uma boa tarde")
    else:
        print("tenha uma boa noite")
except:
    print("Formato inválido! insira outro formato...")   
    
"""Código de tamanho de nome"""

try:
    nome = input('Por favor informe um nome...: ')
    nome = str(nome)
    nome_len = len(nome)
    if (nome_len < 5 ) :
        print("Voce tem um nome curto")
    elif (nome_len > 4 ) and (nome_len < 7):
        print("Voce tem um nome medio")
    else:
        print("Voce tem um longo nome")
except:
    print("Formato inválido! insira outro formato...")