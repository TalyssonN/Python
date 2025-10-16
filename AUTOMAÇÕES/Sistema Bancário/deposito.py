import sqlite3
from datetime import datetime

def realizar_deposito(cpf, conta):
    # Conectar ao banco
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

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
    conexao.close()
    return realizar_deposito