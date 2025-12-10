tarefas = []  # cada elemento será {"titulo": str, "status": str}

def inserirTarefa():

def mostrarTarefas():


def ler_indice(mensagem):


def concluirTarefa():


def removerTarefa():


def editarTarefa():


def menu():
    print("\nMenu")
    print("1 - Inserir Tarefa")
    print("2 - Mostrar Tarefas")
    print("3 - Concluir Tarefa")
    print("4 - Editar Tarefa")
    print("5 - Remover Tarefa")
    print("6 - Sair")

while True:
    menu()
    op = input("Escolha uma opção: ")
    if op == "1":
        inserirTarefa()
    elif op == "2":
        mostrarTarefas()
    elif op == "3":
        concluirTarefa()
    elif op == "4":
        editarTarefa()
    elif op == "5":
        removerTarefa()
    elif op == "6":
        break
    else:
        print("Opção inválida.")
