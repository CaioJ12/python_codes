import random
import os

def acerto(resposta, tentativa):
    if resposta.lower() == tentativa.lower():
        print('Você acertou!')
    else:
        print(f'Você errou! A resposta correta era: {resposta}')

perguntas = [
    {'Pergunta': 'Quanto é 2+2?', 'Opções': ['1', '3', '4', '5'], 'Resposta': '4'},
    {'Pergunta': 'Quanto é 5*5?', 'Opções': ['25', '55', '10', '51'], 'Resposta': '25'},
    {'Pergunta': 'Quanto é 10/2?', 'Opções': ['4', '5', '2', '1'], 'Resposta': '5'},
    {'Pergunta': 'Qual é a capital da França?', 'Opções': ['Paris', 'Londres', 'Roma', 'Madri'], 'Resposta': 'Paris'},
    {'Pergunta': 'Qual planeta é conhecido como Planeta Vermelho?', 'Opções': ['Terra', 'Marte', 'Júpiter', 'Vênus'], 'Resposta': 'Marte'},
    {'Pergunta': 'Qual é o maior animal terrestre?', 'Opções': ['Elefante africano', 'Girafa', 'Hipopótamo', 'Baleia-azul'], 'Resposta': 'Elefante africano'},
    {'Pergunta': 'Quem escreveu "Dom Casmurro"?', 'Opções': ['Machado de Assis', 'José de Alencar', 'Graciliano Ramos', 'Monteiro Lobato'], 'Resposta': 'Machado de Assis'},
    {'Pergunta': 'Qual é o oceano que banha o litoral leste do Brasil?', 'Opções': ['Pacífico', 'Atlântico', 'Índico', 'Ártico'], 'Resposta': 'Atlântico'},
    {'Pergunta': 'Em que continente fica o Egito?', 'Opções': ['África', 'Ásia', 'Europa', 'América'], 'Resposta': 'África'},
    {'Pergunta': 'Qual gás os seres humanos precisam para respirar?', 'Opções': ['Oxigênio', 'Hidrogênio', 'Gás carbônico', 'Nitrogênio'], 'Resposta': 'Oxigênio'},
    {'Pergunta': 'Qual é o idioma oficial do Japão?', 'Opções': ['Chinês', 'Coreano', 'Japonês', 'Tailandês'], 'Resposta': 'Japonês'}
]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    escolha = random.choice(perguntas)  
    pergunta = escolha['Pergunta']
    opcoes = escolha['Opções']
    resposta = escolha['Resposta']
    
    print(pergunta)
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    
    tentativa = input("\nResposta (ou digite 'sair' para encerrar): ")
    
    if tentativa.lower() == 'sair':
        print("Encerrando o jogo...")
        break
    
    # Se o usuário digitar o número da opção
    if tentativa.isdigit():
        tentativa = opcoes[int(tentativa) - 1]
    
    acerto(resposta, tentativa)
    input("\nPressione ENTER para continuar...")
