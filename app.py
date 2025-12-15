import os #importar biblioteca do python

# restaurantes = ['Pizza', 'Sushi'] #criando listas
restaurantes = [{'nome':'Praca','categoria':'Japonesa','ativo':False,}, 
                {'nome': 'Delicias Caseiras', 'categoria':'Salgados','ativo':True},
                {'nome':'Cantina','categoria':'Italiano','ativo':False,}] #Dicionario

def exibir_nome_do_programa():
    '''Essa funcao exibe o nome do Programa'''
    print("""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

def exibir_opcoes():
    '''Essa funcao exibe as opcoes do programa'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa funcao finaliza o programa'''
    os.system('cls') #limpando terminal no Windows
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''Essa funcao volta para o menu principal do programa'''
    input('\nDigite ENTER para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Essa funcao exibe um Print caso nao corresponda nenhuma opcao do programa'''
    print('Opcao invalida!\n')
    voltar_ao_menu_principal()
    main()

def exibir_subtitulo(texto):
    '''Essa funcao exibe os subtitulos de cada opcao no programa'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''Essa funcao e responsavel por cadastrar um novo restaurante
    
    Inputs:
    - Nome do Restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurane que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante) #adicionando elementos na lista
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa funcao exibe os Restaurantes'''
    exibir_subtitulo('Listando restaurantes')


    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alterar_estado_do_restaurante():
    '''Essa funcao exibe o estado de cada restaurante, definindo como True(Ativo) ou False(desativado)'''
    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    '''Essa funcao exibe as opcoes para escolher no programa'''
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa seria a funcao principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
