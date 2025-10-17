# Disciplina: Lógica de Programação e Algoritmos
# Questão 04 do Trabalho Prático 01
# Data: Maio/2024 (Módulo A - fase II)

#Este programa oferece ao usuário uma interface de cadastro e consulta de livros e seus respectivos dados

def cadastrar_livro(id):
# Funçao para cadastrar um livro, solicitando nome, autor e editora
# Os dados são captados em um dicionário e adicionados em uma lista global
    print('-------------MENU CADASTRAR LIVRO--------------')
    print(f'Id do livro: {id}')
    nome_livro = input('Por favor entre com o nome do livro: ')
    autor_livro = input('Por favor entre com o autor do livro: ')
    editora_livro = input('Por favor entre com a editora do livro: ')
    dados_livro = { 'id':id, 'nome': nome_livro, 'autor': autor_livro, 'editora': editora_livro}
    lista_livro.append(dados_livro)
    return


def consultar_livro():
# Funçao que consulta os livros cadastrados anteriormente.
# É dado ao usuário várias opções de consulta
# Os dados apresentados são lidos de uma lista global, cujos elementos são dicionarios
    while True:
        print('-------MENU CONSULTAR LIVRO--------------')
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos')
        print('2 - Consultar por Id')
        print('3 - Consultar por Autor')
        print('4 - Retornar ao Menu')
        escolha = input('>>> ')
        print('-----------------------------------------')

        if escolha == '1':
            for livro in lista_livro:
                print(f'Id: ',livro['id'])
                print(f'Livro: ',livro['nome'])
                print(f'Autor: ',livro['autor'])
                print(f'Editora: ',livro['editora'])
                print()
        elif escolha == '2':
           try:
               id = int(input('Digite o Id do livro: '))
           except ValueError:
               continue
           for livro in lista_livro:
               if livro['id'] == id:
                   print(f'Id: ', livro['id'])
                   print(f'Livro: ', livro['nome'])
                   print(f'Autor: ', livro['autor'])
                   print(f'Editora: ', livro['editora'])
                   print()
        elif escolha == '3':
            autor = input('Digite o Autor do livro: ')
            for livro in lista_livro:
                if livro['autor'] == autor:
                    print(f'Id: ', livro['id'])
                    print(f'Livro: ', livro['nome'])
                    print(f'Autor: ', livro['autor'])
                    print(f'Editora: ', livro['editora'])
                    print()
        elif escolha == '4':
            break
        else:
            print('Opção inválida!')
            continue

    return

def remover_livro():
# Função que tem por objetivo retirar da lista global um livro previamente cadastrado
    while True:
        id = int(input('Digite o Id do livro a ser removido: '))
        for livro in lista_livro:
            if livro['id'] == id:
                lista_livro.remove(livro)
                print('Livro removido com sucesso.')
                return
        print('Id inválido.')
    return

# Programa principal
lista_livro = [] #lista inicializada com vazio para ser utilizada durante a execução do programa
id_global = 0 #variável global para armazenar o id do livro a ser consultado ou removido

print('Bem Vindo à Livraria do Michel Marconssin')
print('-----------------------------------------')
while True:
    print('-------------MENU PRINCIPAL--------------')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro')
    print('3 - Remover Livro')
    print('4 - Encerrar Programa')
    escolha = input('>>> ')
    print('-----------------------------------------')

    if escolha == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif escolha == '2':
        consultar_livro()
    elif escolha == '3':
        remover_livro()
    elif escolha == '4':
        break
    else:
        print('Opção inválida!')
        continue



