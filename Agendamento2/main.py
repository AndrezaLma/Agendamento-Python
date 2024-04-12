import config

def menu():
    service = config.get_service()  # Inicializa o serviço aqui e usa em todas as chamadas necessárias

    while True:
        print("\nSistema de Agendamento de Consultas\n")
        print("1 - Agendar nova consulta")
        print("2 - Listar consultas")
        print("3 - Pesquisar consultas por data")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            data = input("Data: ")
            hora = input("Hora: ")
            paciente = input("Nome do Paciente: ")
            medico = input("Nome do Médico: ")
            config.adicionar(service, data, hora, paciente, medico)
        # elif opcao == '2':
        #     # config.listar_consultas(service)
        # elif opcao == '3':
        #     data = input("Informe a data para pesquisa: ")
        #     # config.pesquisar_consultas_data(service, data)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    menu()
