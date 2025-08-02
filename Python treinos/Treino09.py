#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

#o produto do dobro do primeiro com metade do segundo .
def functionOne(primeiroN, segundoN):
    result = (primeiroN * 2) + (segundoN/2)
    return result

#a soma do triplo do primeiro com o terceiro.
def functionTwo(primeiroN,terceiroN):
    result = ((primeiroN * 3) + terceiroN)
    return result
    
#o terceiro elevado ao cubo.
def functionThree(terceiroN):
    result = (terceiroN**3)
    return result
    
#--------------------------------------------------------------------------------

numeroUm = int(input('por favor insira aqui o primeiro numero inteiro: '))
numeroDois = int(input('por favor insira aqui o segundo numero inteiro: '))
numeroTres = float(input('por favor insira aqui o terceiro numero real: '))

print(f'consecutivamente os resultados das funções são:\n')
print(f'a soma do triplo do primeiro com o terceiro é: {functionOne(numeroUm,numeroDois):.2f}\n a soma do triplo do primeiro com o terceiro é: {functionTwo(numeroUm,numeroTres):.2}\n o terceiro elevado ao cubo é de {functionThree(numeroTres):.2}')
