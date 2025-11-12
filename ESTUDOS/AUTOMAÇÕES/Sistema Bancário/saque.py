
import sqlite3
from fpdf import FPDF
from datetime import datetime

def realizar_saque(cpf, conta):
    # Conectar ao banco
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    # Solicitar valor do saque
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
    conexao.close()
    return realizar_saque
    
    