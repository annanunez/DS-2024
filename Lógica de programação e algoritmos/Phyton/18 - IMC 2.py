letra = 's'
while letra == 's':
    N1 = float(input('Digite a altura em metros: '))
    N2 = float(input('Digite seu peso em kg: '))
    IMC = N2 /(N1*N1)
    print(f'Seu IMC é de {IMC}')
    if IMC <= 18.4:
        print('Abaixo do peso')

    elif IMC <= 24.9:
      print('Peso estável')
    elif IMC <= 29.9:
        print('Sobrepeso')
    elif IMC <= 34.9:
        print('Obesidade grau 1')
    elif IMC <= 39.9:
        print('Obesidade grau 2')
    else:
        print('Obesidade grau 3')

    if IMC > 30:
        print('Cuidado com a saúde, seu peso está acima do recomendado')
    elif IMC < 18.5:
        print('Cuidado com sua saúde, seu peso está abaixo do recomendado')
    else:
        print("Está tudo bem")

        letra = input('Deseja continuar: [S/N]: ')