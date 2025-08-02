#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
def validacao(letra):
    """Valida se a entrada é uma única letra."""
    if not letra.isalpha():  # Verifica se é alfabético
        print("A entrada não é válida! Apenas letras são permitidas.")
        return False
    elif len(letra) > 1:  # Verifica se é apenas uma letra
        print("A entrada não é válida! Digite apenas uma única letra.")
        return False
    return True

valores = ['a', 'e', 'i', 'o', 'u']  # Lista de vogais

def comparacao(letra):
    """Verifica se a letra é uma vogal ou consoante."""
    if letra in valores:
        print("A letra digitada pelo usuário é uma vogal.")
    else:
        print("A letra digitada é uma consoante.")

# ---------------------------- Entrada do usuário ---------------------------------------
letra = input('Por favor, digite aqui a sua letra escolhida: ').lower().strip()

# Validação da entrada
if validacao(letra):
    comparacao(letra)
