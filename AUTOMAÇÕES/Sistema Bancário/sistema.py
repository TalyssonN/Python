import sqlite3
from fpdf import FPDF
import extrato

from datetime import datetime
sqlite3.connect('banco.db')


cursor = sqlite3.connect('banco.db').cursor()
#CRIANDO BANCO DE DADOS / TABELA
cursor.execute('''CREATE TABLE IF NOT EXISTS contas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf TEXT NOT NULL UNIQUE,
                    nascimento TEXT NOT NULL,
                    user_id INTEGER NOT NULL,
                    senha TEXT NOT NULL,
                    saldo REAL NOT NULL,
                    extrato TEXT NOT NULL
                )''')
cursor.connection.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS movimentacoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT NOT NULL,
                    valor REAL NOT NULL,
                    data TEXT NOT NULL,
                    cpf TEXT NOT NULL,
                    FOREIGN KEY (cpf) REFERENCES contas(cpf)
                )''')

cursor.connection.commit()


#MENU DA APLICAÇÃO
print("===== Sistema Bancário =====")
print("{1} - Criar Conta")
print("{2} - Acessar Conta")
print("{3} - Sair")
escolha = input("Escolha uma opção: ")



def acessar_conta():
    #ACESSO À CONTA
    print("===== Acesso à Conta =====")
    cpf = input("Digite seu CPF: ")
    cursor.execute('SELECT * FROM contas WHERE cpf = ?', (cpf,))
    #VALIDANDO A EXISTÊNCIA DO CPF
    conta = cursor.fetchone()
    if not conta:
        print("Conta não encontrada.")
        return

    senha = input("Digite sua senha: ")
    if senha != conta[4]:
        print("Senha incorreta.")
        return

    print("Acesso concedido!")
    #MENU DA CONTA
    def menu_conta():
        print("===== Menu da Conta =====")
        print("{1} - Depositar")
        print("{2} - Sacar")
        print("{3} - Extrato")
        print("{4} - Sair")
        menu_escolha = input("Escolha uma opção: ")
        return menu_escolha
    #LAÇO PARA PERMANECER NO MENU ATÉ O USUÁRIO SAIR
    #MENU DE INTERAÇÃO COM A CONTA
    while True:
        escolha = menu_conta()
        #DEPÓSITO
        if escolha == '1':
            deposito = __import__('deposito')
            deposito.realizar_deposito(cpf, conta)

                
        #SAQUE
        elif escolha == '2':
            saque = __import__('saque')
            saque.realizar_saque(cpf, conta)

        #EXTRATO
        elif escolha == '3':
            print("===== Extrato =====")
            arquivo_pdf = extrato.gerar_extrato_pdf(cpf)
            print(f"Extrato salvo em: {arquivo_pdf}")

        elif escolha == '4':
            print("Saindo da conta...")
            break
        else:
            print("Opção inválida.")
            continue
#CHAMADA DAS FUNÇÕES DE ACORDO COM A ESCOLHA DO USUÁRIO

if escolha == '1':
    criar = __import__('criar_conta')
    criar.criar_conta()
    
elif escolha == '2':
    acessar_conta()
elif escolha == '3':
    print("Saindo...")
else:
    print("Opção inválida.")