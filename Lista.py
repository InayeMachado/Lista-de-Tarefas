class Tarefa:
    #Como retirar uma tarefa da lista quando tem o mesmo identificador.

    def __init__(self, identificador, descricao, tempo_limite):
        self.identificador = identificador
        self.descricao = descricao
        self.tempo_limite = tempo_limite
        self.situacao = "ativa"

    def exibir_tarefa(self):
        return f"ID: {self.identificador}, Descrição: {self.descricao}, Tempo Limite: {self.tempo_limite} horas, Situação: {self.situacao}"
#Função para adicionar uma tarefa à lista
def adicionar_tarefa(lista_tarefas, identificador, descricao, tempo_limite):
    # Verificar se já existe uma tarefa com o mesmo identificador
    for tarefa in lista_tarefas:
        if tarefa.identificador == identificador:
            print("Ops, já existe uma tarefa com esse identificador!")
            return

    nova_tarefa = Tarefa(identificador, descricao, tempo_limite)
    lista_tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")
#Função para visualizar tarefas
def visualizar_tarefas(lista_tarefas, situacao=None):
    if situacao:
        tarefas_filtradas = [tarefa for tarefa in lista_tarefas if tarefa.situacao == situacao]
    else:
        tarefas_filtradas = lista_tarefas
    if not tarefas_filtradas:
        if situacao == "concluida":
            print("Você ainda não concluiu nenhuma tarefa :(")
        else:
            print("Não há tarefas disponíveis.")
        return

    # Nesta parte o código vai colocar em ordem por situação(Ativa ou Concluída)e tempo limite
    tarefas_ordenadas = sorted(tarefas_filtradas, key=lambda x: (x.situacao, x.tempo_limite))

    for tarefa in tarefas_ordenadas:
        print(tarefa.exibir_tarefa())
#Função para atualizar uma tarefa
def atualizar_tarefa(lista_tarefas, identificador, nova_descricao, novo_tempo_limite):
    for tarefa in lista_tarefas:
        if tarefa.identificador == identificador:
            tarefa.descricao = nova_descricao
            tarefa.tempo_limite = novo_tempo_limite
            print("Tarefa atualizada com sucesso!")
            return
    print("Tarefa não encontrada.")
#Função para mudar o status da tarefa para concluído.
def concluir_tarefa(lista_tarefas, identificador):
    for tarefa in lista_tarefas:
        if tarefa.identificador == identificador:
            tarefa.situacao = "concluida"
            print("Tarefa concluída com sucesso!")
            return
    print("Tarefa não encontrada.")
#Função para excluir uma tarefa
def excluir_tarefa(lista_tarefas, identificador):
    for tarefa in lista_tarefas:
        if tarefa.identificador == identificador:
            lista_tarefas.remove(tarefa)
            print("Tarefa excluída com sucesso!")
            return
    print("Tarefa não encontrada.:()")

#Menu de Opções para tarefas.
def exibir_menu():
    print("\n===== Menu de Opções =====")
    print("Digite 1 para adicionar uma tarefa")
    print("Digite 2 para visualizar as tarefas ativas")
    print("Digite 3 para visualizar as tarefas concluídas")
    print("Digite 4 para visualizar Todas as tarefas (tanto concluídas como ativas)")
    print("Digite 5 para atualizar as informações de uma tarefa")
    print("Digite 6 para mudar o status de uma tarefa para concluído")
    print("Digite 7 para excluir uma tarefa")
    print("Digite 8 para sair")

# Lista para armazenar as tarefas
lista_tarefas = []

while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        identificador = int(input("Digite o identificador da tarefa: "))
        descricao = input("Digite a descrição da tarefa: ")
        tempo_limite = float(input("Digite o tempo limite da tarefa em horas: "))
        adicionar_tarefa(lista_tarefas, identificador, descricao, tempo_limite)
    elif opcao == "2":
        visualizar_tarefas(lista_tarefas, situacao="ativa")
    elif opcao == "3":
        visualizar_tarefas(lista_tarefas, situacao="concluida")
    elif opcao == "4":
        visualizar_tarefas(lista_tarefas)
    elif opcao == "5":
        identificador = int(input("Digite o identificador da tarefa que deseja atualizar: "))
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        novo_tempo_limite = float(input("Digite o novo tempo limite da tarefa em horas: "))
        atualizar_tarefa(lista_tarefas, identificador, nova_descricao, novo_tempo_limite)
    elif opcao == "6":
        identificador = int(input("Digite o identificador da tarefa que deseja concluir: "))
        concluir_tarefa(lista_tarefas, identificador)
    elif opcao == "7":
        identificador = int(input("Digite o identificador da tarefa que deseja excluir: "))
        excluir_tarefa(lista_tarefas, identificador)
    elif opcao == "8":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")