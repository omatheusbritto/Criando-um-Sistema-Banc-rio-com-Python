class Operacao:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.registro = {}
        self.transacao = 0

class Usuario:
    def __init__(self,cpf,email,cpf,telefone,registro):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.registro = {}
        self.confirmar = confirmar
        if confirmar =="S":
            self.registro = {'CPF: ':cpf,
                             'Nome: ':nome,
                             'E-mail: ': email,
                             'Telefone: ':telefone}

class Endereco:
    def __init__(self,confirmar, cep,logradouro,numero,cidade,estado,pais,registro):
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.confirmar = confirmar
        if confirmar =="S"
            self.registro.apeend(
                                 {'CEP: ':cep,
                                  'Logradouro: ', logradouro,
                                  'Numero: ':numero,
                                  'Cidade: ':cidade,
                                  'Estado: ':estado,
                                  'País: ':pais}
        
