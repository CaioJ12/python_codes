def media_semestre(nota1, nota2, nota3, nota4):
    """Calcula a média de 4 notas."""
    return (nota1 + nota2 + nota3 + nota4) / 4

#--------------------------------------- Solicitação de notas ao usuário
try:
    entrada = input("Digite as 4 notas separadas por espaço: ")
    
    # Dividir entrada e converter para float, o map aplica float em todas as entradas e depois a lista as guarda
    notas = list(map(float, entrada.split()))
    
    # Verificar se o número de notas é exatamente 4
    if len(notas) != 4:
        raise ValueError("É necessário informar exatamente 4 notas.")
    
    # Calcular e exibir a média usando '*' para desempacotar os valores que eu guardei na lista 
    print(f"A média total foi: {media_semestre(*notas):.2f}")

except ValueError as e:
    print(f"Erro: {e}. Por favor, insira valores numéricos válidos e separados por espaço.")
