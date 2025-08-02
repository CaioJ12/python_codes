def definicente(letter):
    if letter == 'f':
        print(f'A letra escrita é F, o sexo associado a essa letraa é ''FEMININO'' ')
    elif letter == 'm':
        print(f'A letra escrita é M, o sexo associiado a essa letra é ''MASCULINO'' ')
    else:
        print(f'Infelizmente não foi possivel identificar a letra escrita')
        
#----------------------------------------------------------------------------------------

resultado = input('Por favor insira a sigla do genero aqui: ').strip().lower()

definicente(resultado)
