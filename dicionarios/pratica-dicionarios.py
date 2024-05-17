# Pratíca 01
''' Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade. '''
dados_pessoa = {
    'nome': 'Lucas',
    'idade': 23,
    'cidade': 'Salvador'
}

# Prática 02
''' Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário. 
'''

dados_pessoa['idade'] = 25

dados_pessoa['profissão:'] = 'Programador'

del dados_pessoa['idade']
print(dados_pessoa)

# Prática 03
''' Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5. '''
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


# Prática 04
''' Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário. '''
refeicoes = {
    'manhã': 'café da manhã',
    'tarde': 'almoço',
    'noite': 'jantar'
}
print('Chave existente!' if refeicoes['manhã'] else 'Chave inexistente!')

# Prática 05
''' Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário. '''

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
