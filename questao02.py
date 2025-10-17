# Disciplina: Lógica de Programação e Algoritmos
# Questão 02 do Trabalho Prático 01
# Data: Maio/2024 (Módulo A - fase II)

#Este programa recebe o pedido do cliente e calcula o valor total da compra

print('Bem Vindo à Loja de Gelados do Michel Marconssin')
print('---------------Cardápio-------------------------')
print('------------------------------------------------')
print('---|  Tamanho  | Cupuaçu (CP) |  Açaí (AC)  |---')
print('---|     P     |   R$  9,00   |  R$  11,00  |---')
print('---|     M     |   R$ 14,00   |  R$  26,00  |---')
print('---|     G     |   R$ 18,00   |  R$  20,00  |---')
print('------------------------------------------------')

valor_total = 0.00 #variável inicializada para acumular o valor total da compra
while True: # Loop para captar a opção do usuário.
    sabor = input('Entre com o sabor desejado (AC/CP): ')
    sabor = sabor.upper() #transforma a escolha do usuário em caixa alta para facilitar a validação do dado
    if sabor == 'CP':
        nome_sabor = 'Cupuaçu'
        while True:
            tamanho = input('Entre com o tamanho desejado (P/M/G): ')
            tamanho = tamanho.upper()
            if tamanho == 'P':
                valor = 9.00
                break
            elif tamanho == 'M':
                valor = 14.00
                break
            elif tamanho == 'G':
                valor = 18.00
                break
            else:
                print('Tamanho inválido. Tente novamente.')
        print(f'Você pediu um {nome_sabor} tamanho {tamanho}: R$ {valor:,.2f}')
        valor_total += valor
        escolha = input('Deseja mais alguma coisa? (S/N)')
        escolha = escolha.upper()
        if escolha == 'N':
            break
        else:
            continue
    elif sabor == 'AC':
        nome_sabor = 'Açaí'
        while True:
            tamanho = input('Entre com o tamanho desejado (P/M/G): ')
            tamanho = tamanho.upper()
            if tamanho == 'P':
                valor = 11.00
                break
            elif tamanho == 'M':
                valor = 16.00
                break
            elif tamanho == 'G':
                valor = 20.00
                break
            else:
                print('Tamanho inválido. Tente novamente.')
        print(f'Você pediu um {nome_sabor} tamanho {tamanho}: R$ {valor:,.2f}')
        valor_total += valor
        escolha = input('Deseja mais alguma coisa? (S/N)')
        escolha = escolha.upper()
        if escolha == 'N':
            break
        else:
            continue
    else:
        print('Sabor inválido. Tente novamente.')

print(f'Valor total a ser pago: R$ {valor_total:,.2f}')



