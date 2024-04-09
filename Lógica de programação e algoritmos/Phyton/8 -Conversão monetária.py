letra = 's'
while letra == 's':
    cotacao = float(input('Digite a cotação do Dólar: '))

    print('Escolha uma opção: ')
    opcao = int(input('1 - Converter real para Dólar'
                      ' 2 - Converter Dólar para real: '))

if opcao == 1:
    valor = float(input('Digite o valor em real que seá convertido em Dólar:'))
    resultado1 = valor / cotacao
    print(F'O valor é $: {resultado1}')
elif opcao == 2:
    valor = float(input('Digite o valor em em Dólar que será convertido para real: '))
    resultado2 = valor * cotacao
    print(F'O valor é R$: {resultado2}')
else:
    print('Digite uma opção')

letra = input('Deseja continuar? [s/n')