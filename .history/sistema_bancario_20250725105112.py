""" 
1. realizar até 3 saques diários 
2. limite máx de cada saque é de R$500,00
3. usuário sem saldo: 
    sistema deverá informar que não há saldo disponível e não permitir o saque
4. todos os saques deverão ser armazenados em uma variável e exibidos no 
extrato
5. valores exibidos no formato R$__.__
    
"""
saldo = 0.0
depositar = [1]
sacar = [2]
extrato = [3]


while True:
    print("Bem-vindo ao sistema bancário")
    print("Escolha uma opção: "
                      "\n1. Depositar"
                      "\n2. Sacar"
                      "\n3. Extrato"
                      "\n4. Sair"
    )
    menu = int(input("Digite a opção desejada: "))

    if menu == 1:
        valor_depositado = float(input("Digite o valor a ser depositado: R$ "))
        saldo += valor_depositado
        print(f"Depósito realizado com sucesso."
              f"\nO saldo atual é de R$ {saldo:.2f}")
    elif menu == 2:
        valor_sacado = float(input("Digite o valor a ser sacado: R$ "))
        if valor_sacado > 500:
            print("O valor ultrapassa o limite de R$500,00 por saque")
        elif valor_sacado > saldo:
            print("Saldo insuficiente. Não é possível realizar o saque")
        elif valor_sacado <= saldo:
                print(f"Saque realizado com sucesso."
                      f"\nO saldo atual é de R$ {saldo - valor_sacado:.2f}")
        else:
            print("Opção inválida. Tente novamente com uma opção válida.")")