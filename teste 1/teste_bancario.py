                            #Sistema Bancario#
#1- Seus dados#
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
saldo = 1300
#Entrada no Banco#
Banco = (f'Olá {nome, sobrenome} ')
while True:
    print('''Escolha uma opção:
            [1] Consultar Saldo
            [2] Depósito
            [3] Saque
            [4] Encerrar o serviço''')
    opção = int(input("Escolha o que deseja fazer"))
    if opção == 1:
            print(f'Saldo é {saldo}')
    elif opção == 2:
            Novo_valor = int(input('Digite o valor de depósito R$: '))
            novo_saldo = Novo_valor + saldo
            print(f"Seu novo saldo é R$: {novo_saldo}")
    elif opção == 3:
            Novo_saque = int(input('Digite o valor que deseja sacar R$: '))
            novo_saldo = saldo - Novo_saque
            print(f'Seu novo saldo é R$: {novo_saldo}')
    elif opção == 4:
            print(f"Serviço Encerrado\n Muito obrigado por utilizar nossos serviços\n Até breve {nome, sobrenome}")
            break
    #Se chegou nessa parte é porque o sistema funicionou KKKK#