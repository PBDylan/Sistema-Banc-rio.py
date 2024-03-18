import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo usuário
    [nc]\tNova conta
    [lc]\tListar contas
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def depositar(saldo, valor, extrato):
    saldo += valor
    extrato += f"Depósito: +{valor}\n"
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if saldo - valor >= -limite:
            saldo -= valor
            extrato += f"Saque: -{valor}\n"
            numero_saques += 1
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("Limite de saques excedido.")
    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("Extrato:")
    print(extrato)
    print(f"Saldo atual: {saldo}")

def criar_usuario(usuarios):
    nome = input("Informe o nome do novo usuário: ")
    usuarios.append(nome)
    print("Usuário criado com sucesso.")

def criar_conta(agencia, numero_conta, usuarios):
    if usuarios:
        print("Selecione o usuário para vincular à conta:")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario}")
        try:
            indice_usuario = int(input("Opção: ")) - 1
            if 0 <= indice_usuario < len(usuarios):
                return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuarios[indice_usuario]}
            else:
                print("Opção inválida.")
        except ValueError:
            print("Opção inválida.")
    else:
        print("Não há usuários cadastrados.")

def listar_contas(contas):
    print("Lista de Contas:")
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Número da Conta: {conta['numero_conta']} | Titular: {conta['usuario']}")

if __name__ == "__main__":
    main()
