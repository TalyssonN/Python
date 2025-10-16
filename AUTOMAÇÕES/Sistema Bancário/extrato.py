import sqlite3
from fpdf import FPDF
from datetime import datetime

def gerar_extrato_pdf(cpf):
    # Conectar ao banco
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    # Buscar dados da conta
    cursor.execute('SELECT nome, saldo FROM contas WHERE cpf = ?', (cpf,))
    conta = cursor.fetchone()

    if not conta:
        print("Conta não encontrada.")
        return

    nome, saldo = conta

    # Buscar movimentações
    cursor.execute('SELECT tipo, valor, data FROM movimentacoes WHERE cpf = ? ORDER BY id DESC', (cpf,))
    movimentacoes = cursor.fetchall()

    conexao.close()

    # Criar o PDF
    pdf = FPDF()
    pdf.add_page()

    # Cabeçalho
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Extrato Bancário", ln=True, align="C")
    pdf.ln(10)

    # Dados da conta
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Nome: {nome}", ln=True)
    pdf.cell(0, 10, f"CPF: {cpf}", ln=True)
    pdf.cell(0, 10, f"Saldo atual: R$ {saldo:.2f}", ln=True)
    pdf.ln(10)

    # Título da seção de movimentações
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Movimentações:", ln=True)
    pdf.ln(5)

    # Corpo das movimentações
    pdf.set_font("Arial", '', 11)
    if movimentacoes:
        for tipo, valor, data in movimentacoes:
            pdf.cell(0, 8, f"{data} - {tipo}: R$ {valor:.2f}", ln=True)
    else:
        pdf.cell(0, 8, "Nenhuma movimentação registrada.", ln=True)

    # Rodapé
    pdf.ln(10)
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(0, 10, f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", ln=True, align="R")

    # Salvar o PDF
    nome_arquivo = f"extrato_{cpf}.pdf"
    pdf.output(nome_arquivo)
    print(f"✅ PDF gerado com sucesso: {nome_arquivo}")
    return nome_arquivo