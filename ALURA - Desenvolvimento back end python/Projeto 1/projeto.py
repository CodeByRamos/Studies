import os


def exibir_boas_vindas():
            
    print ("Food Express")
    print ("Bem vindo ao menu do restaurante\n")

def exibir_opcoes():
    print ("1- Cadastrar restaurante")
    print ("2- Listar restaurante")
    print ("3- Ativar restaurante")
    print ("4- Sair\n")

def opcao_invalida(opcao_escolhida):
    if not opcao_escolhida.isalpha():
        print("Opção inválida")

def selecionar_opcao():
    opcao_escolhida=int(input("Digite a opção escolhida:"))


    if opcao_escolhida == 1:
            nome_restaurante=input("Digite o nome do restaurante:")
            cnpj_restaurante=input("Digite o cnpj do restaurante:")

    elif opcao_escolhida == 2:
            print (nome_restaurante)
            print (cnpj_restaurante)
    elif opcao_escolhida == 3:
            print("Restaurante cadastrado foi devidamente ativado")
    elif opcao_escolhida == 4:
        os.system('cls')
        print("Encerrando o sistema.")
    else:
           opcao_invalida()



def main():
       exibir_boas_vindas()
       exibir_opcoes()
       selecionar_opcao()
       opcao_invalida()

if __name__ == "__main__":
       main()



