import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}]

def exibir_nome_do_programa():
    ''' Essa função exibe o nome do programa'''

    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

    ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')

def exibir_opcoes():
    ''' Essa função exibe as opções disponível no menu '''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar o estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Essa função existe uma mensagem confirmando a finalização da aplicação quando o usuário seleciona a opção para Sair no menu
    
    Output:
    - Mensagem 'App finalizado!'
    
    '''

    exibir_subtitulo('App finalizado!')

def voltar_ao_menu_principal():
    ''' Essa função explica ao usuário como retornar para o menu principal e faz o redirecionamento para ele quando o usuário pressiona alguma tecla
    
    Input:
    - Acionamento de alguma tecla

    Output:
    - Retorno ao menu principal

    '''

    input('\nPressione qualquer tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    ''' Essa função mostra uma mensagem de alerta quando o usuário digita qualquer carctere diferente dos listados como opção no menu 
    
    Inputs:
    Não possui
    
    Outputs:
    - Mensagem de alerta
    '''
    
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Essa função exibe o subtítulo das opções do menu
    
    Argumento:
    texto (srt): subtítulo de uma opção do menu

    Outputs:
    - Limpa o prompt
    - Exibe * antes e depois do subtítulo de acordo com a quantidade de caracteres do argumento texto para melhorar a estética do output no prompt
    - Quebra de linha

    '''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurentes
     
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Essa função lista os restaurantes cadastrados 

    Inputs:
    Não possui

    Outputs:
    - Nome do restaurante
    - Categoria do restaurante
    - Estado ativado ou desativado
    
    '''

    exibir_subtitulo('Lista dos restaurantes cadastrados: ')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status' )
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Essa função alterna o estado do restaurante entre Ativo e Inativo
    
    Inputs:
    - Nome do restaurante

    Output:
    - Mensagem de sucesso o u insucesso ao ativar ou desativar o restaurante
    - Mensagem de restaurante não encontrado caso o restaurante pesquisado não esteja cadastrado na lista
    
    '''

    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!' 
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Essa função orienta o usuário a escolher uma opção do menu
    
    Inputs:
    - Uma opção do menu 
    - Uma opção não especificada no menu

    Outputs:
    - Opção 1: Cadastro de um novo restaurante
    - Opção 2: Listagem dos restaurantes
    - Opção 3: Mudança de estado de cadastro do restaurante (ativado ou desativado)
    - Opção 4: Mensagem informativa sobre a finalização do programa
    - Opção inválida: Mensagem de alerta sobre opção inválida 
    
    '''

    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Essa função limpa o terminal, exibe o nome do programa, as opções do menu e chama as funções de acordo com a escolha do usuário
    
    Inputs:
    - Comando cls no terminal
    - Opção escolhida pelo usuário

    Outputs:
    - Terminal limpo
    - Nome do programa
    - Opções do menu
    
    '''
    
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
    
