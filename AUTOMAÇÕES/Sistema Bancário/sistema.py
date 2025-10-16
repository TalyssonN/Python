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

#FUNÇÃO PARA CRIAR CONTA
def criar_conta():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    #VALIDANDO CPF. DEVE CONTER 11 DÍGITOS NUMÉRICOS E NÃO SER CADASTRADO NA TABELA
    if cpf.isdigit() == False or len(cpf) != 11:
        print("CPF inválido. Deve conter 11 dígitos numéricos.")
        return
    #CASO NÃO SEJA VÁLIDO, VERIFICA SE JÁ ESTÁ CADASTRADO
    else:

        #SELECIONA NA TABELA SE JÁ EXISTE O CPF
        cursor.execute('SELECT * FROM contas WHERE cpf = ?', (cpf,))
        if cursor.fetchone():
            print("CPF já cadastrado. Tente novamente.")
            return

    nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")

    senha = input("Crie uma senha: ")
    #VALIDANDO SENHA, DEVE TER NO MÍNIMO 6 CARACTERES
    if len(senha) < 6:
        print("Senha muito curta. Deve ter no mínimo 6 caracteres.")
        return
    

    #LISTA DE DADOS DA CONTA, UNIFICAR FACILITA A INSERÇÃO NA TABELA
    conta = {
        "nome": nome,
        "cpf": cpf,
        "nascimento": nascimento,
        "senha": senha,
        "saldo": 0,
        "extrato": []
    }
    #LANÇA OS DADOS NA TABELA, PROCURANDO COLUNA E LINHA ESPECÍFICA
    #TENTATIVA E EXCEÇÃO
    try:
        cursor.execute('INSERT INTO contas (nome, cpf, nascimento, senha, saldo, extrato) VALUES (?, ?, ?, ?, ?, ?)',
                    (conta["nome"], conta["cpf"], conta["nascimento"], conta["senha"], conta["saldo"], str(conta["extrato"])))
        cursor.connection.commit()
        print("Conta criada com sucesso!")
        #TRATANDO ERROS
    except sqlite3.Error as e:
        print(f"Erro ao criar conta: {e}")


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
            valor = float(input("Digite o valor do depósito: "))
            if valor <= 0:
                print("Valor inválido. Deve ser maior que zero.")
            else:
                novo_saldo = conta[5] + valor
                cursor.execute('UPDATE contas SET saldo = ? WHERE cpf = ?', (novo_saldo, cpf))
                cursor.connection.commit()

                cursor.execute('INSERT INTO movimentacoes (cpf, tipo, valor, data) VALUES (?, ?, ?, ?)',
                               (conta[2], 'Depósito', valor, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                
                cursor.connection.commit()

                # Atualiza a variável local
                conta = list(conta)
                conta[5] = novo_saldo

                print(f"Depósito realizado com sucesso. Novo saldo: R$ {novo_saldo:.2f}")

                
        #SAQUE
        elif escolha == '2':
            valor = int(input("Digite o valor do saque: "))
            if valor <= 0:
                print("Valor inválido. Deve ser maior que zero.")
            elif valor > conta[5]:
                print("Saldo insuficiente.")
            else:
                #ATUALIZA O SALDO NA TABELA               
                novo_saldo = conta[5] - valor
                cursor.execute('UPDATE contas SET saldo = ? WHERE cpf = ?', (novo_saldo, cpf))
                cursor.connection.commit()

                cursor.execute('INSERT INTO movimentacoes (cpf, tipo, valor, data) VALUES (?, ?, ?, ?)',
                               (conta[2], 'Saque', valor, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                
                cursor.connection.commit()

                # Atualiza a variável local
                conta = list(conta)
                conta[5] = novo_saldo

                print(f"Saque realizado com sucesso. Novo saldo: R$ {novo_saldo:.2f}")
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
    criar_conta()
elif escolha == '2':
    acessar_conta()
elif escolha == '3':
    print("Saindo...")
else:
    print("Opção inválida.")