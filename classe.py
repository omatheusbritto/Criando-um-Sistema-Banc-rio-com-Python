class Operacao:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.registro = {}
        self.transacao = 0

class Usuario:
    def __init__(self):
        self.nome = str('')
        self.email = str('')
        self.cpf = str('')
        self.telefone = int('')

class Endereco:
    def __init__(self):
        self.cep = int()
        self.logradouro = str('')
        self.numero = int('')
        self.cidade = str('')
        self.estado = str('')
        self.pais = str('')
