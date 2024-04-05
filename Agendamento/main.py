# main.py
import agendamento

def menu():
    while True:
        print("\nSistema de Agendamento \n")
        print("1 - Agendar novo horario")
        print("2 - Listar consultas")
        print("3 - Pesquisar consultas por data")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            data = input("Data: ")
            hora = input("Hora: ")
            cliente = input("Nome do cliente: ")
            advo = input("Nome do Advogado: ")
            agendamento.adicionar_consulta(data, hora, cliente, advo)
        elif opcao == '2':
            agendamento.listar_consultas()
        elif opcao == '3':
            data = input("Informe a data para pesquisa: ")
            agendamento.pesquisar_consultas_por_data(data)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    menu()
