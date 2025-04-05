# Sistema bancário
''' 
crie um menu principal com as opções de funções bancárias e internas
1° Funcões Bancarias

1.1 Crie um menu com as funções bancarias como Sacar, Depositar, extrato voltar ao menu principal

1.2° Saque:
1.1 O usuario não pode fazer mais que 10 transações bancarias por dia
(Caso o numero de transação seja atingida mostrar mensagem de erro)

1.2.1 O usuario não pode sacar valor acima de R$ 500 por vez
(Mostrar a mensagem, valor não foi permitido por saque)

1.2.2 usuario pode sacar no maximo R$1500 por dia
(Mostrar a mensagem, valor de saque diario atingido)

1.2.3 usuario não poderá sacar valores negativo
(Mostrar a mensagem, valor não permitido)

1.2.4 Em saque realizado, mostrar dados como saldo atual, data e hora do saque

1.2 Depósito 
1.2.1 Na função deposito, não será permitido deposito com valores negativo
(Mostrar a mensagem, valor não permitido)

1.2.2 Não permitir do pedosito caso o numero de transação diária tenha atingida 
(Mostrar a mensagem, Transação diaria ja atingida)

1.2.3 Em depósito concluido, mostrar mensagem com o valor do depósito, 
saldo atual em conta, Data e hora

1.3 Saldo
1.3.1 Na função Saldo, mostrar o valor em conta
( Mostrar saldo com data e horario em que foi solicitado)

1.4 Extrato
1.4.1 na função extrato, mostrar detalhadamente todas as transações
( Mostrar se foi depositado ou sacado, valor, data e hora)

2° Funcões internas

2.1 Menu interno
2.1.1 Crie um menu com as funções de cadastrar novo usuario, listar usuarios e voltar ao menu principal

2.1.2 Na função cadastrar novos usuarios

2.1.2.1 validar dados com o CPF
Caso CPF ja esteja cadastrado oferecer a opção de atualização de cadastro

2.1.2.2 Novo cadastro de usuario deve, o usuario deve inserir
Nome completo, Email, Telefone e endereco

2.1.3 mostrar todos os dados do usuario que tenha esse CPF
cadastrar nome, email, telefone e endereço

2.1.4 criar a função de volTar ao menu principal

'''
from funcao import main

main()
