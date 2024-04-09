taxa = float(input(' Qual a cotação do Dólar atual:'))
opcao = int(input(' escolha:'
                  '[1] Converter Dólar para Real:'
                  '[2] Converter Real para Dólar:'))
if opcao == 1:
    moeda = float(input('Qual o valor do dólar a ser convertido em real: '))
    resultado = taxa * moeda
    print(f'O valor é R${resultado:}')

else:
    moeda = float(input('Qual o valor do real a ser convertido em Dólar:'))
    resultado = moeda/taxa
    print(f'O valor em Dólar é: {resultado}')