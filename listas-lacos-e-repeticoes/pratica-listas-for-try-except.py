# Pratica 01
''' Crie uma lista para cada informação a seguir:
        - Lista de números de 1 a 10;
        - Lista com quatro nomes;
        - Lista com o ano que você nasceu e o ano atual.
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Marcos', 'Pedro', 'Matheus', 'Andrew']
ano_nascimento = 1996
ano_atual = 2024

# Prática 02
''' Crie uma lista e utilize um loop for para percorrer todos os elementos da lista. '''
def pratica_02():
    for numero in numeros:
        print(numero)

    for nome in nomes:
        print(nome)

# Prática 03
''' Utilize um loop for para calcular a soma dos números ímpares de 1 a 10. '''
def pratica_03():
    total = 0
    for numero in numeros:
        if numero % 2 == 1:
            total = total + numero
    print(total)  

# Prática 04
''' Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente. '''    
def pratica_04():
    for i in range(10, 0, -1):
        print(i)

# Prática 05
''' Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10. '''        
def pratica_05():
    numero = int(input('Digite um número para visualizar a tabuada de multiplicação dele: '))
    for n in numeros:
        print(f'{numero} x {n} = ', numero * n)
    
# Prática 06
''' Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções. '''
def pratica_06():
    total = 0
    try:
        for numero in numeros:
            total = total + numero
        print(total)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Prática 07
''' Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia. '''
def pratica_07():
    total = 0
    try:
        for numero in numeros:
            total = total + numero
            media = total / len(numeros)
        print(media)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

