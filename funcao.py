from datetime import datetime
import os
import pytz
from classe import Usuario, Endereco

agora = datetime.now(pytz.timezone("America/Sao_Paulo"))
mascara_ptbr=('%d/%m/%Y %a %H:%M:%S')
data_registrada = agora.strftime(mascara_ptbr)
saldo = 0
limite_de_saque = 0
posicao = 0
transacao = 0
continuar = 0
extrato = []
database = []
registro = {}
usuario = {'CPF: ':''}
database.append(usuario)

def linha():
    print(f'-'*45)
def limpar_a_tela():
    seguir = input('Aperte ENTER para continuar:')
    os.system('cls' if os.name =='nt' else 'clear')

def saque():
    global saldo, transacao, limite_de_saque
    saque = float(input('Valor a ser sacado R$').replace(',','.'))
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
    
    elif saque< (saldo + 0.001):
        saldo -= saque
        limite_de_saque += saque
        transacao += 1
        registro = {'Data do saque :':data_registrada, 'Saque R$': f'{saque:.2f}', 
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

def mostrar_saldo():
    global saldo
    print(f' Data: {data_registrada} \n Saldo atual em conta é de R${saldo:.2f}')
    limpar_a_tela()
    print('')

def deposito():
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
        registro = {'Data do depósito: ':data_registrada,'Saldo R$': f'{saldo:.2f}', 
                'Depósito R$': f'{deposito:.2f}'}
    extrato.append(registro)
    saldo += deposito 
    print(f'DEPÓSITO REALIZADO')
    limpar_a_tela()
    print('')

def mostrar_extrato():
    global extrato
    for aux in extrato:
        for keys, value in aux.items():
            print(f'{keys} {value}')
        print('')
    mostrar_saldo()
    limpar_a_tela()

def validacao(cpf):
    global database, posicao, continuar
    controle = 0
    while controle < len(database):
        for dados in database[controle].items():
            keys = dados[0]
            values = dados[1]
            if cpf == values:
                print('')
                print(f'Dado cadastrado!!! {keys}: {values}')
                posicao = controle
                continuar =+ 1
                break

        controle += 1
            
def cadastrar_usuario():
    global database, continuar, posicao
    print('')
    print(f'Cadastro de usuario!')
    cpf = input('Digite seu CPF (Apenas numeros): ')
    validacao(cpf)
    if continuar == 0:
        entrada_de_dados(cpf)
        database.append(usuario)
        print(f'Cadastro concluido')
    else:
        cadastrar = str(input('deseja atualizar cadastro? [S/N]').upper())
        if cadastrar == 'S':
            entrada_de_dados(cpf)
            database[posicao]= usuario
            print(f'Atualização cadastral concluido')
    posicao = 0
    continuar = 0

def entrada_de_dados(cpf):
        global usuario
        cliente = Usuario
        print('Digite seus dados: ')
        cliente.nome = str(input(f'Nome completo: ').title())
        cliente.telefone = int(input(f'telefone (apenas numeros com DDD): '))
        cliente.email =  str(input(f'E-mail: '))
        usuario = {'CPF: ': cpf,
                    'Nome: ': cliente.nome,
                    'Telefone: ': cliente.telefone,
                    'E-mail: ': cliente.email}
        cadastrar_endereco = str(input(f'Deseja cadastrar o enredeço? [S/N]').upper())
        if cadastrar_endereco == 'S':
            print(f'Cadastro de endereço ')
            moradia = Endereco
            moradia.cep = input('CEP (Apenas números): ')
            moradia.logradouro = input('Rua: ')
            moradia.numero = input('Numero: ')
            moradia.cidade = input('Cidade: ')
            moradia.estado = input('Estado [XX]')
            moradia.pais = input('País [XX]')
            usuario.update({'CEP: ': moradia.cep,
                            'Rua: ': moradia.logradouro,
                            'Numero: ': moradia.numero,
                            'Cidade: ': moradia.cidade,
                            'Estado: ': moradia.estado,
                            'País: ': moradia.pais})
            
def mostrar_cadastro():
    controle = 1
    if len(database) <= 1:
        print('')
        print('Nenhum usuario cadastrado! ')
        limpar_a_tela()
        print('')
    else:
        while controle < len(database):
            linha()
            for usuario in database[controle].items():
                keys = usuario[0]
                value = usuario[1]
                print(f'{keys}{value}')
            controle += 1
        limpar_a_tela()
def mostrar_menu_principal():
    print('''| PARA FUNÇÕES BANCÁRIAS -------------- [1] |
| PARA FUNÇÕES INTERNAS --------------- [2] |''')
    
def menu_principal():
        while True:
            linha()
            mostrar_menu_principal()
            linha()
            navegar = int(input(''))
            if navegar == 1:
                menu_bancario()
            elif navegar == 2:
                menu_interno()
            else:
                
                print('| ----------------- ERRO!!! --------------- |')
                limpar_a_tela()

def mostrar_menu_bancario():
    linha()
    print('''| Para SACAR -------------------------- [1] |
| Para DEPOSITAR ---------------------- [2] |
| Para SALDO -------------------------- [3] |
| Para EXTRATO------------------------- [4] |
| Para VOLTAR AO MENU PRINCIPAL ------- [5] |''')
    linha()

def menu_bancario():
    while True:
        mostrar_menu_bancario()
        navegar = int(input(''))
        if navegar == 1:
            saque()
        elif navegar == 2:
            deposito()
        elif navegar == 3:
            mostrar_saldo()
        elif navegar == 4:
            mostrar_extrato()
        elif navegar == 5:
            limpar_a_tela()
            menu_principal()
        else:
            print('| ----------------- ERRO!!! --------------- |')
            limpar_a_tela()

def mostrar_menu_interno():
    linha()
    print('''| Para CADASTRAR NOVOS USUARIOS ------- [1] |
| Para LISTAR USUARIOS ---------------- [2] |
| Para VOLTAR AO MENU PRINCIPAL ------- [3] |''')

def menu_interno():
    while True:
        mostrar_menu_interno()
        linha()
        navegar = int(input(''))
        if navegar == 1:
            cadastrar_usuario()
        elif navegar == 2:
            mostrar_cadastro()
        elif navegar ==3:
            limpar_a_tela()
            menu_principal()
        else:
            print('| ----------------- ERRO!!! --------------- |')
            linha()

def main():
    print(f'-' * 17, 'Bem vindo', '-' * 17)
    menu_principal()
    fechar = input('Aperte tecla ENTER para fechar')
    while fechar != '':
        menu_principal()
    print(f'-' * 17, 'Bem vindo', '-' * 17)
    menu_principal()
    fechar = input('Aperte tecla ENTER para fechar')
    while fechar != '':
        menu_principal()
