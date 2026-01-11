from flask import Blueprint, request, jsonify
import time

api = Blueprint('api', __name__, url_prefix='/api')

# Simula o array "veiculos" do JavaScript
veiculos = []
@api.route('/veiculos', methods=['POST'])
def cadastrar_veiculo():
    dados = request.json

    veiculo = {
        'id': int(time.time() * 1000),  # equivalente ao Date.now()
        'placa': dados.get('placa'),
        'modelo': dados.get('modelo'),
        'tipo': dados.get('tipo'),
        'status': 'Ocupada'
    }

    veiculos.append(veiculo)
    return jsonify(veiculo), 201


@api.route('/veiculos', methods=['GET'])
def listar_veiculos():
    return jsonify(veiculos), 200


@api.route('/veiculos/<int:id>/saida', methods=['PUT'])
def dar_saida(id):
    for v in veiculos:
        if v['id'] == id:
            v['status'] = 'Livre'
            return jsonify(v), 200

    return jsonify({'erro': 'Veículo não encontrado'}), 404



@api.route('/veiculos/<int:id>', methods=['DELETE'])
def excluir_veiculo(id):
    global veiculos
    veiculos = [v for v in veiculos if v['id'] != id]
    return jsonify({'mensagem': 'Veículo excluído'}), 200
