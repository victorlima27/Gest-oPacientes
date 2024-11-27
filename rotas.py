from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_bcrypt import check_password_hash
from app import app,db,csrf
from datetime import datetime

@app.route('/login', methods=['POST'])
@csrf.exempt
def login():
    from models import Usuario
    # Obtém os dados enviados no corpo da requisição (JSON)
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Requisição inválida"}), 400

    username = data.get('username')  # Obtém o username
    senha = data.get('senha')  # Obtém a senha

    # Validação básica
    if not username or not senha:
        return jsonify({"error": "Username e senha são obrigatórios"}), 400

    # Busca o usuário no banco de dados
    user = Usuario.query.filter_by(username=username).first()

    # Verifica se o usuário existe e a senha está correta
    if user and check_password_hash(user.senha, senha):
        return jsonify({"message": "Login realizado com sucesso", "user": username}), 200

    # Caso falhe a autenticação
    return jsonify({"error": "Credenciais inválidas"}), 401

@app.route('/pacientes', methods=['GET', 'POST'])
@csrf.exempt
def pacientes():
    from models import Paciente
    if request.method == 'GET':
        # LISTAR TODOS OS PACIENTES
        pacientes = Paciente.query.all()
        pacientes_list = [
            {
                "id": paciente.id,
                "nome": paciente.nome,
                "cpf": paciente.cpf,
                "data_nascimento": paciente.data_nascimento,
                "telefone": paciente.telefone,
                "historico_medico": paciente.historico_medico,
            }
            for paciente in pacientes
        ]
        return jsonify(pacientes_list), 200
    
    elif request.method == 'POST':
         # CADASTRAR UM NOVO PACIENTE
        data = request.get_json()
        
        print(data)

        if not data:
            return jsonify({"error": "Requisição inválida"}), 400

        nome = data.get('nome')
        cpf = data.get('cpf')
        data_nascimento = data.get('data_nascimento')  # Já no formato de data (ex: 'YYYY-MM-DD')
        telefone = data.get('telefone')
        historico_medico = data.get('historico_medico')

        # Validação básica
        if not all([nome, cpf, data_nascimento, telefone, historico_medico]):
            return jsonify({"error": "Todos os dados são obrigatórios"}), 400

        try:
            # Cria um novo paciente
            novo_paciente = Paciente(
                nome=nome,
                cpf=cpf,
                data_nascimento=data_nascimento,
                telefone=telefone,
                historico_medico=historico_medico
            )
            # Adiciona o paciente ao banco de dados
            db.session.add(novo_paciente)
            db.session.commit()

            return jsonify({"message": "Paciente cadastrado com sucesso!", "paciente": {
                "id": novo_paciente.id,
                "nome": novo_paciente.nome,
                "cpf": novo_paciente.cpf,
                "data_nascimento": novo_paciente.data_nascimento.isoformat(),  # Retorna em formato ISO 8601
                "telefone": novo_paciente.telefone,
                "historico_medico": novo_paciente.historico_medico
            }}), 201

        except Exception as e:
            # Erro genérico (ex: CPF duplicado)
            return jsonify({"error": "Erro ao cadastrar paciente", "details": str(e)}), 500
    
# @app.route('/pacientes2', methods=['GET'])
# @csrf.exempt
@app.route('/medicos', methods=['GET', 'POST'])
@csrf.exempt
def medicos():
    from models import Medico
    if request.method == 'GET':
        # LISTAR TODOS OS MÉDICOS
        medicos = Medico.query.all()
        medicos_list = [
            {
                "id": medico.id,
                "nome": medico.nome,
                "cpf": medico.cpf,
                "especializacao": medico.especializacao,
                "telefone": medico.telefone,
            }
            for medico in medicos
        ]
        return jsonify(medicos_list), 200

    elif request.method == 'POST':
        # CADASTRAR UM NOVO MÉDICO
        data = request.get_json()

        if not data:
            return jsonify({"error": "Requisição inválida"}), 400

        nome = data.get('nome')
        cpf = data.get('cpf')
        especializacao = data.get('especializacao')
        telefone = data.get('telefone')

        if not all([nome, cpf, especializacao, telefone]):
            return jsonify({"error": "Todos os dados são obrigatórios"}), 400

        try:
            novo_medico = Medico(
                nome=nome,
                cpf=cpf,
                especializacao=especializacao,
                telefone=telefone
            )

            db.session.add(novo_medico)
            db.session.commit()

            return jsonify({
                "message": "Médico cadastrado com sucesso!",
                "medico": {
                    "id": novo_medico.id,
                    "nome": novo_medico.nome,
                    "cpf": novo_medico.cpf,
                    "especializacao": novo_medico.especializacao,
                    "telefone": novo_medico.telefone,
                }
            }), 201

        except Exception as e:
            return jsonify({"error": "Erro ao cadastrar médico", "details": str(e)}), 500
        

@app.route('/consultas', methods=['GET', 'POST'])
@csrf.exempt
def consultas():
    from models import Consulta
    if request.method == 'GET':
        # LISTAR TODAS AS CONSULTAS
        consultas = Consulta.query.all()
        consultas_list = [
            {
                "id": consulta.id,
                "data_consulta": consulta.data_consulta.isoformat(),
                "motivo_consulta": consulta.motivo_consulta,
                "diagnostico": consulta.diagnostico,
                "prescricao": consulta.prescricao,
            }
            for consulta in consultas
        ]
        return jsonify(consultas_list), 200

    elif request.method == 'POST':
        # CADASTRAR UMA NOVA CONSULTA
        data = request.get_json()

        if not data:
            return jsonify({"error": "Requisição inválida"}), 400

        paciente_id = data.get('paciente_id')
        medico_id = data.get('medico_id')
        data_consulta = data.get('data_consulta')
        motivo_consulta = data.get('motivo_consulta')
        diagnostico = data.get('diagnostico')
        prescricao = data.get('prescricao')

        if not all([paciente_id, medico_id, data_consulta, motivo_consulta, diagnostico, prescricao]):
            return jsonify({"error": "Todos os campos são obrigatórios"}), 400

        try:
            # Converte a data_consulta para um objeto datetime
            data_consulta = datetime.strptime(data_consulta, '%Y-%m-%d').date()

            nova_consulta = Consulta(
                paciente_id=paciente_id,
                medico_id=medico_id,
                data_consulta=data_consulta,
                motivo_consulta=motivo_consulta,
                diagnostico=diagnostico,
                prescricao=prescricao
            )

            db.session.add(nova_consulta)
            db.session.commit()

            return jsonify({
                "message": "Consulta cadastrada com sucesso!",
                "consulta": {
                    "id": nova_consulta.id,
                    "data_consulta": nova_consulta.data_consulta.isoformat(),
                    "motivo_consulta": nova_consulta.motivo_consulta,
                    "diagnostico": nova_consulta.diagnostico,
                    "prescricao": nova_consulta.prescricao,
                }
            }), 201

        except Exception as e:
            return jsonify({"error": "Erro ao cadastrar consulta", "details": str(e)}), 500


@app.route('/consultas/<int:id>', methods=['GET'])
def consulta_by_id(id):
    from models import Consulta, Paciente, Medico
    # BUSCAR CONSULTA POR ID
    consulta = Consulta.query.get(id)

    if not consulta:
        return jsonify({"error": "Consulta não encontrada"}), 404

    medico = Medico.query.get(consulta.medico_id)
    paciente = Paciente.query.get(consulta.paciente_id)

    return jsonify({
        "id": consulta.id,
        "nomeMedico": medico.nome if medico else None,
        "nomePaciente": paciente.nome if paciente else None,
        "data_consulta": consulta.data_consulta.isoformat(),
        "motivo_consulta": consulta.motivo_consulta,
        "diagnostico": consulta.diagnostico,
        "prescricao": consulta.prescricao,
    }), 200
