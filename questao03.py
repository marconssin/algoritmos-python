# Disciplina: Lógica de Programação e Algoritmos
# Questão 03 do Trabalho Prático 01
# Data: Maio/2024 (Módulo A - fase II)

#Este programa capta a opção do usuário e calcula o valor final dos serviços escolhidos
def escolha_servico():
# Função que oferece os serviços e capta a opção do usuário retornando o custo do serviço ao programa principal
    while True:
        print('Entre com o serviço desejado')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        escolha = input('>>> ')
        escolha = escolha.upper()  #coloca tudo em caixa alta para facilitar a validação
        if escolha != 'DIG' and escolha != 'ICO' and escolha != 'IPB' and escolha != 'FOT':
            print('Escolha inválida, entre com o tipo de serviço novamente!\n')
        else:
            break

    if escolha == 'DIG':
        custo = 1.10
    elif escolha == 'ICO':
        custo = 1.00
    elif escolha == 'IPB':
        custo = 0.40
    elif escolha == 'FOT':
        custo = 0.20

    return custo  #retorna o custo baseado no serviço escolhido

def num_pagina():
#Funçao que recebe o número de páginas que o usuário precisa
    while True:
        try:
            num_paginas = int(input('Entre com o número de páginas: '))
            if num_paginas >= 20000:  #limite de 19999 páginas
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com o número de páginas novamente.')
            else:
                break
        except ValueError:  # tratamento de dados que não sejam numeros inteiros
            continue

    if 20 <= num_paginas < 200:
        num_paginas = num_paginas - num_paginas * 15 // 100 #desprezando os decimais
    elif 200 <= num_paginas < 2000:
        num_paginas = num_paginas - num_paginas * 20 // 100  # desprezando os decimais
    elif 2000 <= num_paginas < 20000:
        num_paginas = num_paginas - num_paginas * 25 // 100  # desprezando os decimais

    return num_paginas  # retorna o número de páginas ajustado de acordo com o desconto oferecido

def servico_extra():
# Função que oferece ao usuário um serviço extra ao anteriormente adquirido
    while True:
        print('Deseja adicionar algum serviço?')
        print('1 - Encadernação Simples - R$ 15,00')
        print('2 - Encadernação Capa Dura - R$ 40,00')
        print('0 - Não desejo mais nada')
        servico = input('>>> ')

        if servico != '0' and servico != '1' and servico != '2':
            continue
        else:
            break

    if servico == '1':
        valor = 15.00
    elif servico == '2':
        valor = 40.00
    elif servico == '0':
        valor = 0.00

    return valor  #retorna ao programa principal o valor do serviço contratado


# Programa principal

print('Bem Vindo à Copiadora do Michel Marconssin')
print()
servico = escolha_servico()
num_pagina = num_pagina()
extra = servico_extra()
total = servico * num_pagina + extra
# Apresenta ao usuário os serviços contratados e os custos totais
print(f'Total: R$ {total:,.2f} (serviço: R$ {servico:,.2f} * páginas: {num_pagina} + extra: R$ {extra:,.2f})')






