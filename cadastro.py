def valida_int(pergunta, min, max):
    """Valida um número inteiro dentro do intervalo [min, max]."""
    while True:
        try:
            op = int(input(pergunta))
            if min <= op <= max:
                return op
            else:
                print("Valor inválido. Digite um número entre {} e {}.".format(min, max))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")


def criaArquivo(nomeArquivo):
    """Cria um arquivo de texto com o nome especificado."""
    try:
        with open(nomeArquivo, 'wt+') as a:
            pass
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))


def existeArquivo(nomeArquivo):
    """Verifica se um arquivo existe."""
    try:
        with open(nomeArquivo, 'rt'):
            pass
    except FileNotFoundError:
        return False
    else:
        return True


def listarArquivo(nomeArquivo):
    """Lista o conteúdo de um arquivo."""
    try:
        with open(nomeArquivo, 'rt') as a:
            print(a.read())
    except:
        print('Erro ao ler o arquivo')


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    """Cadastra um jogo e o respectivo videogame no arquivo."""
    try:
        with open(nomeArquivo, 'at') as a:
            a.write('{};{}\n'.format(nomeJogo, nomeVideogame))
    except:
        print('Erro ao abrir o arquivo')


def excluirJogo(nomeArquivo, nomeJogo):
    """Exclui um jogo e o respectivo videogame do arquivo."""
    try:
        with open(nomeArquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
        with open(nomeArquivo, 'w') as arquivo:
            for linha in linhas:
                if nomeJogo not in linha:
                    arquivo.write(linha)
        print("Jogo excluído com sucesso.")
    except:
        print('Erro ao excluir o jogo.')


# PROGRAMA PRINCIPAL
arquivo = "games.txt"

if not existeArquivo(arquivo):
    print('Arquivo inexistente')
    criaArquivo(arquivo)
else:
    print('Arquivo localizado no computador')

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastro')
    print('3 - Excluir item')
    print('4 - Sair')

    op = valida_int('Escolha a opção: ', 1, 4)
    if op == 1:
        print('Opção de cadastrar novo item selecionada...')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif op == 2:
        print('Opção de listar selecionada...\n')
        listarArquivo(arquivo)

    elif op == 3:
        print('Opção de excluir item selecionada...')
        nomeJogo = input('Digite o nome do jogo a ser excluído: ')
        excluirJogo(arquivo, nomeJogo)

    elif op == 4:
        print('Encerrando o programa...')
        break
