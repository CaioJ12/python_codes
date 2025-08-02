#Faça um Programa que peça dois números e imprima a soma.

def soma_total(numero1,numero2):
    soma = numero1 +numero2
    return soma

#--------------------------------------------------------------------

numero1= (int(input('digite seu primeiro número: ')))
numero2= (int(input('digite seu segundo numero: ')))

print(f'A soma total calculada foi: {soma_total(numero1,numero2)}')