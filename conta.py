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

    def sacar(self, valor):
        print(f'Valor do Saque R$ {valor}')
        if (self.__saldo + self.__limite) < valor:
            print('Saldo insuficiente...')
        else:
            (self.__saldo + self.__limite) - valor 
            print(f'Sacando R$ {valor} na conta de {self.__titular}')
            
    
    def transferir(self, valor, destino):
        if valor <= self.__saldo:
            self.sacar(valor)
            destino.depositar(valor)
        else:
            print('Saldo insuficiente para tranferencia')
        
    
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





conta = Conta(1, 'marcelo', 90.50)
conta2 = Conta(2, 'neymar', 1500, 25000)

conta.extrato()
conta.depositar(500) 
conta.sacar(600)

conta2.extrato()
conta2.depositar(500)
conta2.sacar(350)

conta.transferir(2000, conta2)
