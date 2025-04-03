# Sistema bancário
''' 
crie um menu principal com as opções de funções bancárias e internas

Para a funções bancárias
Crie um menu com as funções bancarias como Sacar, Depositar, extrato voltar ao menu principal

RESTRIÇÕES!!!
1º O usuario não pode fazer mais que 10 transações bancarias por dia
(Caso o numero de transação seja atingida mostrar mensagem de erro)

2º O usuario não pode sacar valor acima de R$ 500 por vez
(Mostrar a mensagem de erro, valor não foi permitido por saque)

3º O usuario pode sacar no maximo R$1500 por dia
(Mostrar a mensagem de erro, valor de saque diario atingido)

4º O usuario não poderá sacar valores negativo
(Mostrar a mensagem de erro, valor não permitido)

5º Na função deposito, não será permitido deposito com valores negativo
(Mostrar a mensagem de erro, valor não permitido)

6º Na função Saldo, mostrar o valor em conta
( Mostrar saldo com data e horario em que foi solicitado)

7º na função extrato, mostrar detalhadamente todas as transações
( Mostrar se foi depositado ou sacado, valor, data e hora)

Para funções externas
Crie um menu com as funções de cadastrar novo usuario, listar usuarios e voltar ao menu principal

1º Na função cadastrar novos usuarios
validar com o CPF
Caso CPF ja esteja cadastrado mostrar mensagem de erro (dados ja cadastrado)
mostrar todos os dados do usuario que tenha esse CPF
cadastrar nome, email, telefone e endereço

2º criar a função de volTar ao menu principal

'''
from funcao import main

main()
