# Pratica 01
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('O número que você digitou é par!')
else:
    print('O número que você digitou é ímpar!')

# Pratica 02
idade = int(input('Digite a sua idade: '))
if 0 <= idade <= 12:
    print('Você é uma criança.')
elif 13 <= idade <= 18:
    print('Você é um adolescente.')
else:
    print('Você é um adulto.')

# Pratica 03
usuario = input('Digite um nome de usuário: ')
senha = input('Digite uma senha: ')

if usuario == 'Admin' and senha == '123':
    print(f'{usuario}, bem vindo ao sistema!')
else:
    print(f'{usuario}, credenciais inválidas. Tente novamente!')

# Pratica 04
coordenada_x = float(input('Digite uma coordenada x: '))
coordenada_y = float(input('Digite uma coordenada y: '))

if coordenada_x > 0 and coordenada_y > 0:
    print('Primeiro Quadrante do plano cartesiano')
elif coordenada_x < 0 and coordenada_y > 0:
    print('Segundo Quadrante do plano cartesiano')
elif coordenada_x < 0 and coordenada_y < 0:
    print('Terceiro Quadrante do plano cartesiano')
elif coordenada_x > 0 and coordenada_y < 0:
    print('Quarto Quadrante do plano cartesiano')
else:
    print('Ponto está localizado no eixo ou origem')
