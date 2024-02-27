class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.saques_diarios = 3
        self.limite_saque = 500
        self.extrato = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito: R$ {valor:.2f}')

    def saque(self, valor):
        if self.saques_diarios > 0 and valor <= self.limite_saque and valor <= self.saldo:
            self.saldo -= valor
            self.saques_diarios -= 1
            self.extrato.append(f'Saque: R$ {valor:.2f}')
        elif valor > self.saldo:
            print("Erro: Saldo insuficiente para o saque.")
        else:
            print("Erro: Limite de saques diários atingido ou valor de saque inválido.")

    def gerar_extrato(self):
        for operacao in self.extrato:
            print(operacao)
        print(f'Saldo Atual: R$ {self.saldo:.2f}')


# Exemplo de uso do sistema
banco = SistemaBancario()

banco.deposito(1000)
banco.saque(200)
banco.saque(600)  # Tentando sacar mais do que o limite diário
banco.deposito(500)
banco.saque(300)
banco.gerar_extrato()
