letra = 's'
while letra == 's':
    numero1 = float(input('Digite a primeira nota: '))
    numero2 = float(input('Digite a segunda nota: '))
    numero3 = float(input('Digite a terceira nota: '))

    soma = numero1 + numero2 + numero3
    media = soma / 3

    print(f"A médisa do aluno é: {round(media, 2)}")

    if media >= 7:
        print('Aprovado')
    elif media >=3:
        print('Recuperação')
    else:
        print('Reprovado')