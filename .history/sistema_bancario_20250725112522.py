""" 
1. realizar até 3 saques diários 
2. limite máx de cada saque é de R$500,00
3. usuário sem saldo: 
    sistema deverá informar que não há saldo disponível e não permitir o saque
4. todos os saques deverão ser armazenados em uma variável e exibidos no 
extrato
5. valores exibidos no formato R$__.__
    
"""
saldo = 2000.00
depositar = [1]
sacar = [2]
extrato = [3]
limite_saque_diario = 3 
contador_saques_diarios = 0 
# Antes do 1º saque, contador_saques = 0 → permitido
#    Depois do 1º saque → contador_saques = 1
#    Depois do 2º saque → contador_saques = 2
#    Depois do 3º saque → contador_saques = 3
#    Agora contador_saques >= 3 → bloqueia ✔️ 


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
        if contador_saques_diarios >= limite_saque_diario:
            print("Você já atingiu o limite de saques diários (3)."
                "Tente novamente amanhã.")
        else:
            valor_sacado = float(input("Digite o valor a ser sacado: R$ "))
            if valor_sacado > 500:
                print("O valor ultrapassa o limite de R$500,00 por saque")
            elif valor_sacado > saldo:
                print("Saldo insuficiente. Não é possível realizar o saque")
            else:
                saldo -= valor_sacado # atualiza saldo subtraindo valor_sacado
                contador_saques_diarios += 1 # atualiza saques diários até lim
                print(f"Saque realizado com sucesso."
                    f"\nO saldo atual é de R$ {saldo - valor_sacado:.2f}")
            
    elif menu == 3:
        print(f"Extrato da conta: R$ {saldo:.2f}")
        
    
    elif menu == 4:
        print("Saindo do sistema. Até a próxima!")
        break
    
    else:
        print("Opção inválida. Tente novamente com uma opção válida.")