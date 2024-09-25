# Menu de opções do banco
menu_banco = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo_conta = 0  # Saldo inicial da conta
limite_saque = 500  # Limite máximo para cada saque
historico_transacoes = ""  # Histórico das transações
qtd_saques_realizados = 0  # Contador de saques realizados
LIMITE_SAQUES_DIARIO = 3  # Limite de saques diários

while True:
    opcao_menu = input(menu_banco)  # Recebe a opção escolhida no menu

    if opcao_menu == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))  # Valor do depósito

        if valor_deposito > 0: # Se menor que 0
            saldo_conta += valor_deposito  # Adiciona o valor ao saldo
            historico_transacoes += f"Depósito: R$ {valor_deposito:.2f}\n"  # Registra a transação no extrato
        else:
            print("Operação falhou! O valor informado é inválido.")  # Valor inválido para depósito

    elif opcao_menu == "s":
        valor_saque = float(input("Informe o valor do saque: "))  # Valor do saque

        saldo_insuficiente = valor_saque > saldo_conta  # Verifica se o saldo é suficiente
        saque_acima_limite = valor_saque > limite_saque  # Verifica se o saque excede o limite
        saques_excedidos = qtd_saques_realizados >= LIMITE_SAQUES_DIARIO  # Verifica se excedeu o limite de saques

        if saldo_insuficiente:
            print("Operação falhou! Você não tem saldo suficiente.")  # Saldo insuficiente
        elif saque_acima_limite:
            print("Operação falhou! O valor do saque excede o limite.")  # Saque acima do limite permitido
        elif saques_excedidos:
            print("Operação falhou! Número máximo de saques excedido.")  # Limite de saques diários atingido
        elif valor_saque > 0:
            saldo_conta -= valor_saque  # Deduz o valor do saldo
            historico_transacoes += f"Saque: R$ {valor_saque:.2f}\n"  # Registra o saque no extrato
            qtd_saques_realizados += 1  # Incrementa o contador de saques
        else:
            print("Operação falhou! O valor informado é inválido.")  # Valor inválido para saque

    elif opcao_menu == "e":
        # Mostra o extrato ou mensagem padrão se não houver transações
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not historico_transacoes else historico_transacoes)
        print(f"\nSaldo: R$ {saldo_conta:.2f}")
        print("==========================================")

    elif opcao_menu == "q":
        break  # Sai do loop while e encerra o programa!

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")  # Opção inválida
