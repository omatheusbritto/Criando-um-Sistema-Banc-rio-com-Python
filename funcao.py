from datetime import datetime
import os
import pytz

usuarios = {} 
saldo = 0.0 
contas = {'cpf': '', 'Agência: ':'', 'Nº da conta:':'numero_conta'}
extrato = []
registro = {}
transacao = 0
limite_de_saque = 0
saques_dia = 0
agencia = '00001'

agora = datetime.now(pytz.timezone("America/Sao_Paulo"))
mascara_ptbr=('%d/%m/%Y %a %H:%M:%S')
data_registrada = agora.strftime(mascara_ptbr)


def limpar_a_tela():
    seguir = input('Aperte ENTER')
    os.system('cls' if os.name =='nt' else 'clear')

def mostrar_menu_principal():
    print("""| ============== MENU PRINCIPAL =========== |
| PARA FUNÇÕES BANCÁRIAS -------------- [1] |
| PARA FUNÇÕES INTERNAS --------------- [2] |
| PARA SAIR --------------------------- [0] | 
| ========================================= |""") 
    
def mostrar_menu_bancario():
            print('''| ============ FUNÇÕES BANCÁRIAS ========== |
| Para SACAR -------------------------- [1] |
| Para DEPOSITAR ---------------------- [2] |
| Para SALDO -------------------------- [3] |
| Para EXTRATO ------------------------ [4] |
| Para VOLTAR AO MENU PRINCIPAL ------- [5] |''') 

def mostrar_menu_internas():
    print("""| ============= FUNÇÕES INTERNAS ========== | 
| Para CADASTRAR NOVOS USUARIOS ------- [1] |
| Para LISTAR USUARIOS ---------------- [2] |
| Para VOLTAR AO MENU PRINCIPAL ------- [3] | 
| Para CRIAR CONTA BANCÁRIA ----------- [4] |""") 
    
def menu_principal(): 
    while True: 
        mostrar_menu_principal()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            limpar_a_tela()
            menu_funcoes_bancarias()
        elif opcao == "2":
            limpar_a_tela()
            menu_funcoes_internas()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
            limpar_a_tela()
    limpar_a_tela()

def menu_funcoes_bancarias(): 
    global transacao
    while True: 
        mostrar_menu_bancario()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            sacar()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            ver_saldo()
        elif opcao == "4":
            ver_extrato()
        elif opcao == "5":
            limpar_a_tela()
            menu_principal()
        else:
            print("Opção inválida!")
            limpar_a_tela()

def menu_funcoes_internas(): 
    while True: 
        mostrar_menu_internas()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            limpar_a_tela()
            cadastrar_usuario()
        elif opcao == "2":
            limpar_a_tela()
            listar_usuarios()
        elif opcao == "3":
            limpar_a_tela()
            menu_principal()
        elif opcao == "4":
            criar_conta()
            limpar_a_tela()
        else:
            print("Opção inválida!")
            limpar_a_tela()


def sacar():
    global saldo, transacao, limite_de_saque
    saque = float(input('Valor a ser sacado R$').replace(',', '.'))
    if saque < saldo and transacao < 10 and limite_de_saque < 1500 and saque < 0:
        if saque > 500:
            print('ERRO - Valor maior que o permitido')
            limpar_a_tela()
        elif (limite_de_saque + saque) > 1500:
            resta = 1500 - limite_de_saque
            if resta == 0:
                print('Limite de saque diário atingido')
                print('')
                limpar_a_tela()
            else:
                print(f'ERRO!!! valor restante de saque diário permitido é de R${resta:.2f}')
                print('')
                limpar_a_tela()

        elif saque < 0:
            print(f'ERRO!!! Valor inválido')
            limpar_a_tela()

        else:
            print(f'Saldo insuficiente')
            limpar_a_tela()

    if transacao == 10:
        print(f'Limite de transação diária atingida')
        print('')
        limpar_a_tela()

    elif saque < (saldo + 0.001):
        saldo -= saque
        limite_de_saque += saque
        transacao += 1
        registro = {'Data do saque :': data_registrada, 'Saque R$': f'{saque:.2f}',
                    'Saldo R$': f'{saldo:.2f}'}
        print(registro)
        print(f'SAQUE REALIZADO')
        print('')
        limpar_a_tela()
        extrato.append(registro)
    else:
        print('ERRO!!! Saldo insuficiente')
        print('')
        limpar_a_tela()

def criar_conta():
    global agencia
    cpf = input("CPF do titular: ")
    if cpf not in usuarios:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return
    numero_conta = input("Digite o número da nova conta: ")
    aux = 0
    encontrado = 0
    while aux < len(usuarios):
        dados = usuarios
        for keys, values in dados.items():
            if numero_conta in values:
                print("Conta já existente.")
                encontrado +=1
                break
            else:
                aux = + 1

    if encontrado == 0:
        contas = {'Agência: ':agencia, 'Nº da conta: ':numero_conta}
        usuarios[cpf].update(contas)
        print(contas)

    print("Conta criada com sucesso.")

def depositar():
    global saldo, registro, transacao
    deposito = float(input('Valor a ser depósitado R$').replace(',','.'))
    if deposito < 0 or transacao == 10:
        if transacao == 10:
            print('Limite de transação diaria atingida')
            limpar_a_tela()
        else:
            print('Valor inválido!!!')
            limpar_a_tela()
    else:
        transacao += 1
        saldo += deposito
        registro = {'Data do depósito: ':data_registrada,'Saldo em conta R$': f'{saldo:.2f}',
                'Depósito R$': f'{deposito:.2f}'}
        print(registro)
    extrato.append(registro)
    print(f'DEPÓSITO REALIZADO')
    limpar_a_tela()
    print('')

def ver_saldo(): 
    print(f"Saldo atual: R$ {saldo:.2f} - {data_registrada}")

def ver_extrato(): 
    print("===== EXTRATO =====") 
    for tipo, valor, data in extrato: 
        print(f"{tipo}: R$ {valor:.2f} - {data}") 
        print("====================")
    limpar_a_tela()


def cadastrar_usuario():
    cpf = input("Digite o CPF do usuário: ") 
    if cpf in usuarios:
        print("Usuário já cadastrado!")
        atualizar = input("Deseja atualizar os dados? (s/n): ")
    else:
        print('Usuario não cadastrado')
        atualizar = input("Deseja cadastrar os dados? (s/n): ")
    if atualizar.lower() != 's': 
        return
    nome = input("Nome completo: ").title()
    email = input("Email: ")
    telefone = input("Telefone: ")
    usuarios[cpf] = {"nome": nome,
        "email": email,
        "telefone": telefone,}
    atualizar_endereco = input("Deseja atualizar o endereço? (s/n): ") 
    if atualizar_endereco.lower() != 's': 
        return
    cep = input('CEP (Apenas numeros)')
    logradouro = input('Logradouro: [Rua/Avenida/Estrada]: ').title()
    numeral = input('Numero: ')
    lavrado = input('Lavradouro: [bairro/lote]: ').title()
    cidade = input('Cidade: ').title()
    estado = input('Estado: [EE]:').title()
    pais  = input('Cidade [BR]:').title()
    usuarios[cpf].update({'CEP: ':cep,
                          'Logradouro: ': logradouro,
                          'Nº': numeral,
                          'Lavradouro: ':lavrado,
                          'Cidade: ':cidade,
                          'Estado: ':estado,
                          'País: ':pais})


    print("Usuário cadastrado/atualizado com sucesso!")
    limpar_a_tela()

def listar_usuarios(): 
    cpf = input("Digite o CPF para listar os dados: ") 
    
    if cpf in usuarios: 
        dados = usuarios[cpf]
        for keys, values in dados.items():
            print(f'\n{keys}:{values}')
    else: print("Usuário não encontrado!")

menu_principal()
