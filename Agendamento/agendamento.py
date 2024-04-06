import config

sheet = config()


def adicionar_consulta(data, hora, cliente, advo):
    sheet.append_row([data, hora, cliente, advo])
    print("Consulta adicionada com sucesso.")


def listar_consultas():
    consultas = sheet.get_all_records()
    for consulta in consultas:
        print(consulta)


def pesquisar_consultas_por_data(data):
    consultas = sheet.get_all_values()
    for consulta in consultas:
        if consulta[0] == data:
            print(consulta)
