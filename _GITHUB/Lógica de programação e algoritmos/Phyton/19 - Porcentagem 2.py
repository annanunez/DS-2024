letra = 's'
while letra == 's':

    n1 = float(input('Digite o número que você deseja calcular a porcentagem: '))
    n2 = float(input('Digite a porcentagem que você deseja descobrir do número: '))

    porcentagem = n1/100
    valor = porcentagem*2

    print(f"O valor é: {valor}")

    letra = input('Deseja continuar: [S/N]: ')