class Conta:

    def __init__(self, numero, titular, saldo=0.0, limite = 1000):
        self.__numero  = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print(f'O saldo do {self.__titular} é R$ {self.__saldo}')

    def depositar(self, valor):
        self.__saldo += valor
        print(f'Depositando R$ {valor} na conta de {self.__titular}')
        print(f'Novo saldo R$ {self.__saldo}')

    def __podeSacar(self, valor_do_saque):
        valor_disponivel_para_saque = self.__saldo + self.__limite 
        return valor_do_saque <= valor_disponivel_para_saque
    
    def sacar(self, valor):
        print(f'Valor do Saque R$ {valor}')
        if(self.__podeSacar(valor)):
            self.__saldo -= valor
            print(f'Novo Saldo R$ {self.__saldo}')
        else:
            print('Saldo insuficiente...')
            
            
    
    def transferir(self, valor, destino):
        if self.__saldo >= valor:     
            self.sacar(valor)
            destino.depositar(valor)
        else:
            print('Saldo insuficiente para transferencia')
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigoBanco():
        return '001'

    @staticmethod
    def codigosBancos():
        return {'BB':'001', 'Bradesco': '237', 'Caixa': '034'}



conta = Conta(1, 'marcelo', 90.50)
conta2 = Conta(2, 'neymar', 1500, 25000)

conta.extrato()
conta.depositar(500) 
conta.sacar(600)

conta2.extrato()
conta2.depositar(500)
conta2.sacar(350)

conta.transferir(2000, conta2)

a = conta.codigoBanco()
print(a)

b = conta.codigosBancos()
print(b)
'''for k, v in b.items:
    print(f'{k} {v}')'''