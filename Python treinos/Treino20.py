while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador (+, -, /, *): ")
    numeros_validos = None  
    numero_1_float = float(numero_1)
    numero_2_float = float(numero_2)
    operadores_permitidos = "+-/*"

    try:
        numeros_validos = True  
    except:
        numeros_validos = None
        print("Erro ao converter os números:")

    if not numeros_validos:
        print("Existem números inválidos na operação...")
        continue
    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue
    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    # Realiza a operação
    if operador == "+":
        resultado = numero_1_float + numero_2_float
    elif operador == "-":
        resultado = numero_1_float - numero_2_float
    elif operador == "*":
        resultado = numero_1_float * numero_2_float
    elif operador == "/":
        if numero_2_float == 0:
            print("Erro: divisão por zero.")
            continue
        resultado = numero_1_float / numero_2_float

    print(f"O resultado é: {resultado}")

    sair = input("Quer sair? [S]im: ").lower().startswith("s")
    if sair:
        break
