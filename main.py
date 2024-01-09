from src._functions import incluir, alterar, excluir, listagem_geral

print("1 - Incluir")
print("2 - Alterar")
print("3 - Excluir")
print("4 - Listagem geral")
print("5 - Listagem por saldo")
print("S - Sair")
opcao = input("Digite uma opção \n").strip().upper()

match (opcao):
    case '1':
        name = input("Digite o nome \n")
        balance = input("Digite o balanço \n")
        gender = input("digite o genero \n")

        values = (name, balance, gender)
        incluir(values)

    case '2':
        name = input("Digite o nome \n")
        balance = input("Digite o balanço \n")
        gender = input("digite o genero \n")
        values = (name, balance, gender)

        alterar(values) 

    case '3':
        id = input("Digite o id \n")
        excluir(id) 
    case '4': 
        listagem_geral()
    case '5':
        pass
        """ listagem_saldo() """
            
