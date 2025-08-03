# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
def criar_multiplicacao(number):
    def double(number):
        return number * 2
    
    def triple(number):
        return number * 3
    
    def quadruple(number):
        return number * 4
    
    result = (double(number), triple(number), quadruple(number))
    
    return result

multiply_one = criar_multiplicacao(2)
#dobro, triplo, quadruplo = criar_multiplicacao(2)

print('O resultado é: ', *multiply_one)


#result = criar_multiplicacao


# o número recebido como parâmetro.