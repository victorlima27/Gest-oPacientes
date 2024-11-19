from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from app import app

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Obtém os dados enviados no corpo da requisição (JSON)
    login = data.get('login')  # Obtém o login
    senha = data.get('senha')  # Obtém a senha

    # Validação básica
    if not login or not senha:
        return jsonify({"error": "Login e senha são obrigatórios"}), 500

    # # Verifica se o login e senha são válidos
    # if users.get(login) == senha:
    #     return jsonify({"message": "Login realizado com sucesso", "user": login}), 200
    # else:
    #     return jsonify({"error": "Credenciais inválidas"}), 401
