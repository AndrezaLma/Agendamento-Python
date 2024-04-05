import agendamento

def menu_principal():
    while True:
        print("\nSistema de Agendamentos\n")
        print("1. Agendar nova consulta")
        print("2. Listar todas as agendamentos")
        print("3. Pesquisar agendamentos por data")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            data = input("Data: ")
            hora = input("Hora: ")
            cliente = input("Nome do cliente : ")
            advo = input("Nome do Advogado: ")
            print(agendamento.adicionar_agendamento(data, hora, cliente, advo))
        elif escolha == '2':
            agendamento.listar_agendamento()
        elif escolha == '3':
            data_pesquisa = input("Data para pesquisa: ")
            agendamento.pesquisar_agendamento(data_pesquisa)
        elif escolha == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
