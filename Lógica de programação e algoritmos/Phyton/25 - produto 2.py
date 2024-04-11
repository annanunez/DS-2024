from click import clear

opcao = 0
nome_produto = []
valor_produto = []
descricao_produto = []
quantidade_produto = []

def adicionar():
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    descricao = input('Digite a descrição do produto: ')
    quantidade = int(input('Digite a quantidade: '))

    nome_produto.append(nome)
    valor_produto.append(valor)
    descricao_produto.append(descricao)
    quantidade_produto.append(quantidade)


def mostrar():
    print('nome do produto  \t valor do produto \t quantidade  \t descricao do produto ')
    for i in range(0, len(nome_produto)):
        print(f'{nome_produto[i]} \t\t {valor_produto[i]} \t\t\t {quantidade_produto[i]} \t\t {descricao_produto[i]}')
    input("pressione ENTER para continuar...")

def excluir():
    opcao = int(input('Qual registro deseja deletar?'))
    nome_produto.pop(opcao)
    valor_produto.pop(opcao)
    descricao_produto.pop(opcao)
    quantidade_produto.pop(opcao)


while True:
    clear()

    print("Escolha uma opção")
    print("1 - Para adicionar um produto")
    print("2 - Para mostrar produtos")
    print("3 - Para excuir um produto")
    print("4 - Para sair")
    print("5 - Para abrir txt")
    opcao = int(input("O que deseja fazer? "))
    if opcao == 1:
        adicionar()
    elif opcao == 2:
        mostrar()
    elif opcao == 3:
        excluir()
    elif opcao == 4:
        sair()
    elif opcao == 5:
        abrir()
        break


def adicionar_proutos():
    nome_produto = input('Digite o produto: ')
    valor_produto = input('Digite o valor do produto: ')
    descricao_produto = input('Digite a descrição do produto: ')
    quantidade_produto = input('Digite a quantidade de produto: ')

    with open('Loja.txt', 'a') as arquivo:
        arquivo.write(f'{nome_produto}, {valor_produto}, {descricao_produto}, {quantidade_produto}\n')

        print('produtos cadastrados com sucesso!')


def listar_produtos():
    with open('loja.txt', 'a') as arquivo:
        print('produtos cadastrados com sucesso!')
        for linha in arquivo:
            nome_produto, valor_produto, quantidade_produto, descricao_produto = linha.split(';')
            print(f'Nome do produto: {nome_produto}, Valor do produto: {valor_produto}, Quantidade do produto: {quantidade_produto}, Descrição do produto {descricao_produto}\n')



listar_produtos()