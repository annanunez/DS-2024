quantidade = int(input('Digite a quantidade de livros para compra: '))
print(quantidade)

print("Opções: ")
print(" [1] - R$: 0,25 por cada livro + R$:7,50 fixo ")
print(" [2] - R$: 0,50 por livro + R$: 2,50 Fixo")

opcao_a = (quantidade * 0.25) + 7.50
opcao_b = (quantidade * 0.50) + 2.50

if opcao_a > opcao_b:
        print('A melhor opção é R$: 0.50 por livros + R$: 2.50 fixo [2]')
elif opcao_a < opcao_b:
        print("A melhor opção é R$: 0.25 por livros + R$: 7.50 fixo [1]")
