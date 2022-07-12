from time import sleep
print('******************** Python Calculator ******************** ')
sleep(1)

while True:
    print('\nSelecione o número da opção desejada: '
          '\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
    opcao = int(input('\nDigite sua opção (1/2/3/4): '))
    while opcao not in (1, 2, 3, 4):
        opcao = int(input('Opção inválida! Digite sua opção (1/2/3/4): '))

    sleep(1)
    n1 = int(input('\nDigite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    sleep(2)

    if opcao == 1:
        print(f'\n{n1} + {n2} = {n1+n2}')
    elif opcao == 2:
        print(f'\n{n1} - {n2} = {n1-n2}')
    elif opcao == 3:
        print(f'\n{n1} x {n2} = {n1*n2}')
    elif opcao == 4:
        print(f'\n{n1} / {n2} = {n1/n2}')

    resposta = str(input('\nDeseja utilizar a Python Calculator novamente? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
sleep(1)
print('\nObrigado por utilizar a Python Calculator!')
input('Pressione qualquer tecla para encerrar... ')


