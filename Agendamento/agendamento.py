agendamento = []

def adicionar_agendamento(data, hora, cliente, advo):
    consulta = {
        'data': data,
        'hora': hora,
        'cliente': cliente,
        'advo': advo
    }
    agendamento.append(consulta)
    return "Agendamento feito com sucesso."

def listar_agendamento():
    if not agendamento:
        return "Nenhuma consulta agendada."
    for consulta in agendamento:
        print(f"Data: {consulta['data']}, Hora: {consulta['hora']}, cliente: {consulta['cliente']}, Médico: {consulta['advo']}")

def pesquisar_agendamento(data_pesquisa):
    agendamento_filtradas = [consulta for consulta in agendamento if consulta['data'] == data_pesquisa]
    if not agendamento_filtradas:
        return "Nenhuma consulta encontrada para esta data."
    for consulta in agendamento_filtradas:
        print(f"Data: {consulta['data']}, Hora: {consulta['hora']}, cliente: {consulta['cliente']}, Médico: {consulta['advo']}")
