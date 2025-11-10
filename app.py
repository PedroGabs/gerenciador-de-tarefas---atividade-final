import os
import time
from datetime import datetime

#é pra chamar a função que pega o horário do pc
agora = datetime.now()

#Formatar para o padrão brasileiro completo (HH:MM:SS DD/MM/AAAA)
Now = agora.strftime("%H:%M:%S %d/%m/%Y")

#lista principal
ToDo = []

#essa lista é pra validar as opções das variáveis, pq o usuário pode digitar em caixa alta, precisa melhorar um pouco pra evitar erros.

prioridades_validas = ["urgente", "alta", "média", "baixa"]
status_validos = ["pendente", "fazendo", "concluído"]
origens_validas = ["email", "telefone", "chamado do sistema"]

#função pra adicionar a tarefa, pra mim eu acho melhor ter pra ficar mais simples e fácil... continuação abaixo
def addAtividade(titulo, desc, prioridade, status, origemTar, DataCreation):
    task = {"titulo" : titulo, "desc" : desc, "prioridade" : prioridade, "status" : status, "origemTar" : origemTar, "DataCreation" : DataCreation}
    ToDo.append(task)

#é bem mais prático fazer a função de criar a tarefa e dps no finalzinho só chamar a função de add a tarefa na lista, fica mais simples e menos poluído visualmente dizendo(minha visão, podem concordar ou discordar)
def criarAtividade():
    titulo = str(input('Digite o título da tarefa: '))
    if len(titulo) >= 50:
        print('Título muito grande! (limite de 50 caracteres)\n')
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
                print('Prioridade inválida. Tente novamente!')
                time.sleep(2.1)
                os.system('cls')
                return #Precisa coisar pra ele voltar pra informar de novo a prioridade 
        status = "pendente"
        while True:
            origemTar = input('Informe a origem da tarefa (Email, Telefone ou Chamado do sistema): ').lower()
            if origemTar in origens_validas:
                break
            else:
                print('Origem desconhecida. Tente novamente!')
                time.sleep(2.1)
                os.system('cls')
                return #Mesma fita que a prioridade
            
        DataCreation = Now
        addAtividade(titulo, desc, prioridade, status, origemTar, DataCreation)
        os.system('cls')

###############################################   Menu   ######################################################


while True:
    print('                                                              ')
    print(r'  ████████╗ █████╗ ███████╗██╗  ██╗██╗  ██╗██╗   ██╗██████╗   ')
    print(r'  ╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██║  ██║██║   ██║██╔══██╗  ')
    print(r'     ██║   ███████║███████╗█████╔╝ ███████║██║   ██║██████╔╝  ')
    print(r'     ██║   ██╔══██║╚════██║██╔═██╗ ██╔══██║██║   ██║██╔══██╗  ')
    print(r'     ██║   ██║  ██║███████║██║  ██╗██║  ██║╚██████╔╝██████╔╝  ')
    print(r'     ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝   ')
    print('                                                              ')
    print('  ╔════════════════════════════════════════════════════════╗  ')
    print('  ║                                                        ║  ')
    print('  ║                > 1 - Criar tarefa                      ║  ')
    print('  ║                > 2 - Ver lista de tarefas              ║  ')
    print('  ║                > 3 - Sei la, teste                     ║  ')
    print('  ║                > 4 - Sair                              ║  ')
    print('  ║                                                        ║  ')
    print('  ╚════════════════════════════════════════════════════════╝  ')

#Validação básica para o usuário interagir com o menu apenas utilizando números inteiros

    try:
        opcao = int(input(': '))
    except ValueError:
        print('\nUtilize apenas números!!\n') 
        time.sleep(1.7)
        os.system('cls')
        continue

    match opcao:
        case 1:
            criarAtividade()

        case 2:
            print(ToDo)
            input("")
            os.system('cls')

        case 3:
            print('fndfs')

        case 4:
            break

        case _:
            print('\nOpção inválida. Tente novamente!\n')
            time.sleep(1.7)
            os.system('cls')

# caracteres do menu!
# 
# ╔╗═╚╝╠╣╦╬║╩