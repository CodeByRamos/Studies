lista = []
print("Bem-vindo à To-Do List, a sua lista de afazeres!")
print("Selecione o que você gostaria de fazer com a sua lista:")
print("1 - Adicionar tarefa")
print("2 - Excluir tarefa")
print("3 - Mostrar lista")
print("4 - Sair")

while True:
    opcao = input("\nDigite sua opção: ")
    if opcao == '1':
        add = input("Nos diga a tarefa que gostaria de adicionar: ")
        lista.append(add)
        print(f"Tarefa '{add}' adicionada com sucesso!")
    elif opcao == '2':
        if lista:
            print("Tarefas disponíveis:")
            for i, tarefa in enumerate(lista, start=1):
                print(f"{i} - {tarefa}")
            try:
                excluir = int(input("Digite o número da tarefa que deseja excluir: "))
                if 1 <= excluir <= len(lista):
                    removida = lista.pop(excluir - 1)
                    print(f"Tarefa '{removida}' excluída com sucesso!")
                else:
                    print("Número inválido!")
            except ValueError:
                print("Por favor, digite um número válido!")
        else:
            print("A lista está vazia. Nada para excluir.")
    elif opcao == '3':
        if lista:
            print("Sua lista de tarefas:")
            for i, tarefa in enumerate(lista, start=1):
                print(f"{i} - {tarefa}")
        else:
            print("Sua lista está vazia.")
    elif opcao == '4':
        print("Saindo... Até mais!")
        break
    else:
        print("Opção inválida! Por favor, tente novamente.")
