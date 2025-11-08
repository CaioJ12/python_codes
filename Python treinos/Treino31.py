#Aumente os preços dos produtos em 10%
#Gere 'novos_produtos' por deepcopy
import copy

produtos = [
    
    {'nome': 'Coca Cola', 'preco' : 10.00},
    {'nome': 'Bolo-de-rolo', 'preco' : 33.45},
    {'nome': 'Doritos Sweet Chilli', 'preco' : 22.50},
    {'nome': 'Biscoito', 'preco' : 17.99},
    {'nome': 'Trufa', 'preco' : 6.50},

]


novos_produtos = [ 
    {**p,'preco': round(p['preco'] *1.10,2)}
    for p in copy.deepcopy(produtos)

]

print('\n',novos_produtos)

#Ordene novos produtos por ordem nome decrescente
novos_produtos.sort(key=lambda item: len(item['nome']), reverse=True)
print('\n', novos_produtos)
# Gere 'novos_produtos_ordenados' por deepcopy
novos_produtos_ordenados_nome = copy.deepcopy(novos_produtos)
print('\n', novos_produtos_ordenados_nome)


#Ordene novos produtos por preço crescente
novos_produtos.sort(key=lambda item:item['preco'])
# Gere 'novos_produtos_ordenados_preco' por deepcopy
novos_produtos_ordenados_preco = copy.deepcopy(novos_produtos)
print('\n', novos_produtos_ordenados_preco)
