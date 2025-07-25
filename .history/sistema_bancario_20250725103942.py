""" 
1. realizar até 3 saques diários 
2. limite máx de cada saque é de R$500,00
3. usuário sem saldo: 
    sistema deverá informar que não há saldo disponível e não permitir o saque
4. todos os saques deverão ser armazenados em uma variável e exibidos no 
extrato
5. valores exibidos no formato R$__.__
    
"""
menu = input
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
    menu(int(input("Digite a opção desejada: ")))
                      
