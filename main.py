'''Crie um menu principal com as opções de funções bancárias e internas
1° Funções Bancarias

1.1 Crie um menu com as funções bancárias como Sacar, Depositar, extrato voltar ao menu principal

1.2 Saque:

1.2.1 O usuário não pode fazer mais que 10 transações bancárias por dia
(Caso o número de transação seja atingido mostrar mensagem de erro)

1.2.2 O usuário não pode sacar valor acima de R$ 500 por vez
(Mostrar a mensagem, valor não permitido por saque)

1.2.3 usuários podem sacar no máximo R$1500 por dia
(Mostrar a mensagem, valor de saque diário atingido)

1.2.4 usuários não poderá sacar valores negativos
(Mostrar a mensagem, valor não permitido)

1.2.5 Em saque realizado, mostrar dados como saldo atual, data e hora do saque

1.2 Depósito:

1.2.1 Na função deposito, não será permitido deposito com valores negativos
(Mostrar a mensagem, valor não permitido)

1.2.2 Não permitir do depósito caso o número de transação diária tenha atingido 
(Mostrar a mensagem, Transação diária atingida)

1.2.3 Em depósito concluído, mostrar mensagem com o valor do depósito, 
saldo atual em conta, Data e hora

1.3 Saldo:

1.3.1 Na função Saldo, mostrar o valor em conta
( Mostrar saldo com data e horário em que foi solicitado)

1.4 Extrato:

1.4.1 na função extrato, mostrar detalhadamente todas as transações
( Mostrar se foi depositado ou sacado, valor, data e hora)

2° Funções internas

2.1 Menu interno:

2.1.1 Crie um menu com as funções de cadastrar novos usuários, listar usuários e voltar ao menu principal

2.1.2 Na função cadastrar novos usuários

2.1.2.1 validar dados com o CPF
Caso CPF já esteja cadastrado oferecer a opção de atualização de cadastro

2.1.2.2 Novo cadastro de usuário deve, o usuário deve inserir
Nome completo, E-mail, Telefone e endereço

2.2 Listar Usuários:

2.2.1 mostrar todos os dados do usuário que tenha esse CPF
cadastrar nome, email, telefone e endereço

2.3 Voltar ao menu principal:

2.3.1  Criar a função de voltar ao menu principal'''

import funcoes from menu_principal

menu_principal()
