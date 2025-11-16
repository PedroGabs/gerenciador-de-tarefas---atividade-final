import os
import time
import json
from datetime import datetime

#id global
id_tarefa = 1

#lista principal
ToDo = []

#lista excluidos
Tasks_del = []

#lista concluídas
Tasks_con = []


#essa lista é pra validar as opções das variáveis, pq o usuário pode digitar em caixa alta, precisa melhorar um pouco pra evitar erros.

prioridades_validas = {"urgente": 1, "alta": 2, "média": 3, "baixa":4}
status_validos = ["pendente", "fazendo", "concluído", "excluída"]
origens_validas = ["email", "telefone", "chamado do sistema"]

#função pra adicionar a tarefa, pra mim eu acho melhor ter pra ficar mais simples e fácil... continuação abaixo
def addAtividade(titulo, desc, prioridade, status, origemTar, DataCreation):
    global id_tarefa
    task = {"ID" : id_tarefa,"titulo" : titulo, "desc" : desc, "prioridade" : prioridade, "status" : status, "origemTar" : origemTar, "DataCreation" : DataCreation}
    ToDo.append(task)
    id_tarefa += 1

#é bem mais prático fazer a função de criar a tarefa e dps no finalzinho só chamar a função de add a tarefa na lista, fica mais simples e menos poluído visualmente dizendo(minha visão, podem concordar ou discordar)
def criarAtividade():
    titulo = str(input('Digite o título da tarefa: '))
    if len(titulo) >= 50:
        print('\033[31m Título muito grande! (limite de 50 caracteres) \033[0m \n')
        time.sleep(2.1)
        os.system('cls')
        return criarAtividade()
    else:
        desc = input('(opcional) Digite a descrição da tarefa: ')
        while True:    
            prioridade = input('Informe a prioridade da tarefa (baixa, média, alta ou Urgente): ').lower()
            if prioridade in prioridades_validas:
                break
            else:
                print('\033[31m Prioridade inválida. Tente novamente! \033[0m ')
                time.sleep(2.1)
                os.system('cls')
                return #Precisa coisar pra ele voltar pra informar de novo a prioridade 
        status = "pendente"
        while True:
            origemTar = input('Informe a origem da tarefa (Email, Telefone ou Chamado do sistema): ').lower()
            if origemTar in origens_validas:
                break
            else:
                print('\033[31m Origem desconhecida. Tente novamente! \033[0m')
                time.sleep(2.1)
                os.system('cls')
                return #Mesma fita que a prioridade
            
        DataCreation = datetime.now().strftime("%H:%M:%S %d/%m/%Y") #para pegar o horario
        addAtividade(titulo, desc, prioridade, status, origemTar, DataCreation)
        os.system('cls')
    
def MostrarTasks(): #função pra imprimir as informações da lista na tela do usuário
    if not ToDo: #Validação simples pra ver se tem algo ou não na lista
        print('\033[31m \nNão há nenhuma tarefa registrada no momento! \033[0m ')
        time.sleep(2.1)
        os.system('cls')
    else:
        for i in range(21):
                bar = '█' * i + '░' * (20 - i)
                print(f'\rCarregando: |{bar}| {i*5}%', end='') #apenas estética, pra criar efeito de carregamento.
                time.sleep(0.03)
                os.system('cls')
        tarefas_ordenadas = sorted(ToDo, key=lambda t: prioridades_validas[t["prioridade"]])
        for Tasks in tarefas_ordenadas:
            print(f"\nId: {Tasks['ID']}\nTítulo: {Tasks['titulo']}\ndescrição: {Tasks['desc']}\nprioridade: {Tasks['prioridade']}\nstatus: {Tasks['status']}\nOrigem: {Tasks['origemTar']}\nData de criação: {Tasks['DataCreation']}")
        input("\nPrecione qualquer tecla para continuar...")
        os.system('cls')

def AtualizarStatus(): #função para editar alguma tarefa
    if not ToDo:
        print('\033[31m \nNão há nenhuma tarefa registrada para atualizar! \033[0m')
        time.sleep(2.1)
        os.system('cls')
        return
    else:
        for i in range(21):
                bar = '█' * i + '░' * (20 - i)
                print(f'\rCarregando: |{bar}| {i*5}%', end='') #apenas estética, pra criar efeito de carregamento.
                time.sleep(0.03)
                os.system('cls')

        #1° parte da função

        print('Qual tarefa você deseja atualizar?')
        tarefas_ordenadas = sorted(ToDo, key=lambda t: prioridades_validas[t["prioridade"]]) #método para colocar no topo as prioridades mais altas, seguindo uma sequência numerica declarada na lista de prioridades validas.
        for Tasks in tarefas_ordenadas:
            print(f'\nId: {Tasks['ID']}\nTítulo: {Tasks['titulo']}\nprioridade: {Tasks['prioridade']}\nstatus: {Tasks['status']}') 
            
            #adicionei ao For o enumerate pra ele atribuir um ID numérico as tarefas (provisóriamente, a ideia é ele ja ser declarado na criação sem precisar diretamente da interação do usuário igual o status que por padrão vem como pendente).
        try:
            id_digitado = int(input(': '))   
            Tasks = next((t for t in ToDo if t["ID"] == id_digitado), None) # Procura a tarefa com esse ID
            if Tasks is None:
                print('\033[31m \nÍndice desconhecido, tente novamente! \033[0m')
                time.sleep(1.7)
                os.system('cls')
                return
            os.system('cls')
        except (ValueError, IndexError):
            print('\033[31m \nÍndice desconhecido, Utilize apenas! \033[0m')
            time.sleep(1.7)
            os.system('cls')
            return
        
        #2° parte da função

        print('O que você deseja alterar?') #Menu de alterações
        print('> 1 - Prioridade')
        print('> 2 - Status')
        try:
            option = int(input(': ')) #parte pra validar o valor da opção
            os.system('cls')
        except ValueError:
            print('\033[31m Utilize apenas números!!\033[0m\n') 
            time.sleep(2.1)
            os.system('cls')
            return

        match option:
            case 1: #se o usuário optar pela primeira opção, ele passará pela etapa de cadastro na respectiva parte da tarefa.   
                nova_prioridade = input('Informe a prioridade da tarefa (baixa, média, alta ou Urgente): ').lower()
                if nova_prioridade in prioridades_validas:
                    Tasks['prioridade'] = nova_prioridade
                    print('\033[32m Prioridade alterada com sucesso! \033[0m')
                    time.sleep(1.7)
                    os.system('cls')

                else:
                    print('\033[31m Prioridade inválida. Tente novamente! \033[0m ')
                    time.sleep(2.1)
                    os.system('cls')
                    return #Precisa coisar pra ele voltar pra informar de novo a prioridade

            case 2:
                novo_status = input('Informe o status da tarefa (pendente ou fazendo): ').lower()
                if novo_status in status_validos:
                    Tasks['status'] = novo_status
                    print('\033[32m Status alterado com sucesso! \033[0m')
                    time.sleep(1.7)
                    os.system('cls')

                else:
                    print('\033[31m Status inválido. Tente novamente! \033[0m ')
                    time.sleep(2.1)
                    os.system('cls')
                    return #Precisa coisar pra ele voltar pra informar de novo a prioridade


            case _:
                print('\033[31m Opção inválida. Tente novamente! \033[0m \n')
                time.sleep(2.1)
                os.system('cls')
        
def ConcluirTask():
    if not ToDo:
        print('\033[31m \nNão há nenhuma tarefa registrada para concluir! \033[0m')
        time.sleep(2.1)
        os.system('cls')
        return
    else:
        for i in range(21):
                bar = '█' * i + '░' * (20 - i)
                print(f'\rCarregando: |{bar}| {i*5}%', end='') #apenas estética, pra criar efeito de carregamento.
                time.sleep(0.03)
                os.system('cls')

        #1° parte da função

        print('Qual tarefa você deseja concluir?')
        tarefas_ordenadas = sorted(ToDo, key=lambda t: prioridades_validas[t["prioridade"]]) #método para colocar no topo as prioridades mais altas, seguindo uma sequência numerica declarada na lista de prioridades validas.
        for Tasks in tarefas_ordenadas:
            print(f'\nId: {Tasks['ID']}\nTítulo: {Tasks['titulo']}\nprioridade: {Tasks['prioridade']}\nstatus: {Tasks['status']}')

        try:
            id_digitado = int(input(': '))   
            Tasks = next((t for t in ToDo if t["ID"] == id_digitado), None) # Procura a tarefa com esse ID
            if Tasks is None:
                print('\033[31m \nÍndice desconhecido, tente novamente! \033[0m')
                time.sleep(1.7)
                os.system('cls')
                return
            os.system('cls')
        except (ValueError, IndexError):
            print('\033[31m \nÍndice desconhecido, Utilize apenas! \033[0m')
            time.sleep(1.7)
            os.system('cls')
            return

        novo_status = "concluído"
        Tasks['status'] = novo_status
        Tasks["DataConclusao"] = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        print('\033[32m Tarefa concluída com sucesso! \033[0m')
        Tasks_con.append(Tasks)
        ToDo.remove(Tasks)
        time.sleep(1.7)
        os.system('cls')

def ExcluirTask():
    if not ToDo:
        print('\033[31m \nNão há nenhuma tarefa registrada para excluir! \033[0m')
        time.sleep(2.1)
        os.system('cls')
        return
    else:
        for i in range(21):
                bar = '█' * i + '░' * (20 - i)
                print(f'\rCarregando: |{bar}| {i*5}%', end='') #apenas estética, pra criar efeito de carregamento.
                time.sleep(0.03)
                os.system('cls')

        #1° parte da função

        print('Qual tarefa você deseja excluir?')
        tarefas_ordenadas = sorted(ToDo, key=lambda t: prioridades_validas[t["prioridade"]]) #método para colocar no topo as prioridades mais altas, seguindo uma sequência numerica declarada na lista de prioridades validas.
        for Tasks in tarefas_ordenadas:
            print(f'\nId: {Tasks['ID']}\nTítulo: {Tasks['titulo']}\nprioridade: {Tasks['prioridade']}\nstatus: {Tasks['status']}')

        try:
            id_digitado = int(input(': '))   
            Tasks = next((t for t in ToDo if t["ID"] == id_digitado), None) # Procura a tarefa com esse ID
            if Tasks is None:
                print('\033[31m \nÍndice desconhecido, tente novamente! \033[0m')
                time.sleep(1.7)
                os.system('cls')
                return
            os.system('cls')
        except (ValueError, IndexError):
            print('\033[31m \nÍndice desconhecido, Utilize apenas! \033[0m')
            time.sleep(1.7)
            os.system('cls')
            return

        novo_status = "excluída"
        Tasks['status'] = novo_status
        print('\033[32m Tarefa excluída com sucesso! \033[0m')
        Tasks_del.append(Tasks)
        ToDo.remove(Tasks)
        time.sleep(1.7)
        os.system('cls')


###############################################   Menu   ######################################################

#\033[35m \033[0m

while True:
    print('                                                              ')
    print(r'  ████████╗ █████╗ ███████╗██╗  ██╗       ██╗  ██╗██╗   ██╗██████╗   ')
    print(r'  ╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝       ██║  ██║██║   ██║██╔══██╗  ')
    print(r'     ██║   ███████║███████╗█████╔╝        ███████║██║   ██║██████╔╝  ')
    print(r'     ██║   ██╔══██║╚════██║██╔═██╗        ██╔══██║██║   ██║██╔══██╗  ')
    print(r'     ██║   ██║  ██║███████║██║  ██╗       ██║  ██║╚██████╔╝██████╔╝  ')
    print(r'     ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝  ╚═╝ ╚═════╝ ╚═════╝   ')
    print('                                                                      ')
    print('  ╔════════════════════════════════════════════════════════════════╗  ')
    print('  ║                                                                ║  ')
    print('  ║\033[35m                > 1 - Criar tarefa                   \033[0m           ║  ')
    print('  ║\033[35m                > 2 - Ver lista de tarefas           \033[0m           ║  ')
    print('  ║\033[35m                > 3 - Atualizar tarefas              \033[0m           ║  ')
    print('  ║\033[35m                > 4 - Concluir tarefa                \033[0m           ║  ')
    print('  ║\033[35m                > 5 - Excluir tarefa                 \033[0m           ║  ')
    print('  ║\033[35m                > 6 - Sair                           \033[0m           ║  ')
    print('  ║                                                                ║  ')
    print('  ╚════════════════════════════════════════════════════════════════╝  ')

#Validação básica para o usuário interagir com o menu apenas utilizando números inteiros

    try:
        opcao = int(input(': '))
    except ValueError:
        print('\033[31m Utilize apenas números!!\033[0m\n') 
        time.sleep(1.7)
        os.system('cls')
        continue

    match opcao:
        case 1:
            criarAtividade()

        case 2:
            MostrarTasks()

        case 3:
            AtualizarStatus()

        case 4:
            ConcluirTask()

        case 5:
            ExcluirTask()

        case 6:
            break

        case _:
            print('\033[31m Opção inválida. Tente novamente! \033[0m \n')
            time.sleep(1.7)
            os.system('cls')

# caracteres do menu!
#  \033[31m \033[0m
# ╔╗═╚╝╠╣╦╬║╩