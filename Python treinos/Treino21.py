"""numeros = range(1, 10,2)

for numero in numeros:
    print(numero)"""
    
texto = 'Caio'
iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break