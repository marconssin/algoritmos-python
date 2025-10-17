# Disciplina: Lógica de Programação e Algoritmos
# Questão 01 do Trabalho Prático 01
# Data: Maio/2024 (Módulo A - fase II)

#Este programa calcula o valor do desconto a ser aplicado de acordo com a quantidade comprada pelo cliente

print(f'Bem Vindo à Loja do Michel Marconssin')

valor_unitario = float(input(f'Entre com o valor do produto: '))
quantidade = int(input(f'Entre com a quantidade do produto: '))

valor_sem_desconto = float(valor_unitario * quantidade)

# Os percentuais variam de 4, 7 e 11% aplicados em cima do valor da compra
if valor_sem_desconto >= 10000:
    percentual_desconto = 11
elif 6000 <= valor_sem_desconto < 10000:
    percentual_desconto = 7
elif 2500 <= valor_sem_desconto < 6000:
    percentual_desconto = 4
else:
    percentual_desconto = 0

desconto = float(valor_sem_desconto * percentual_desconto/100)
valor_com_desconto = float(valor_sem_desconto - desconto)

# Mensagem final mostrando o valor com o desconto aplicado
print(f'O valor SEM desconto: R$ {valor_sem_desconto:,.2f}')
print(f'O valor COM desconto: R$ {valor_com_desconto:,.2f}')
