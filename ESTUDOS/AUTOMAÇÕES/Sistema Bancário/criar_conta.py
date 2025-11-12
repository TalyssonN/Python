import sqlite3
from datetime import datetime

def criar_conta():
    # Conectar ao banco
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    #SOLICITANDO DADOS AO USUÁRIO
    print("===== Criação de Conta =====")
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
    finally:
        conexao.close()
    return criar_conta