from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

clientes = [{'id': 1, 'nome': 'João', 'email': 'joao@email.com'}, {'id': 2, 'nome': 'Maria', 'email': 'maria@email.com'}]
medicos = [{'id': 1, 'nome': 'Dr. José', 'especialidade': 'Cardiologia'}, {'id': 2, 'nome': 'Dr. Ana', 'especialidade': 'Dermatologia'}]
consultas = [{'id': 1, 'cliente': 'João', 'medico': 'Dr. José', 'data': '2024-11-15'}, {'id': 2, 'cliente': 'Maria', 'medico': 'Dr. Ana', 'data': '2024-11-16'}]

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
            return redirect(url_for('dashboard', username=username))
        else:
            flash('Usuário ou senha inválidos', 'error')
    return render_template('login.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    user = {'email': 'admin@exemplo.com'} 
    return render_template('dashboard.html', user=user)

@app.route('/clientes')
def clientes_page():
    return render_template('clientes.html', clientes=clientes)

@app.route('/medicos')
def medicos_page():
    return render_template('medicos.html', medicos=medicos)

@app.route('/consultas')
def consultas_page():
    return render_template('consultas.html', consultas=consultas)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_page():
    if request.method == 'POST':
        tipo = request.form['tipo']
        nome = request.form['nome']
        if tipo == 'cliente':
            clientes.append({'id': len(clientes) + 1, 'nome': nome, 'email': request.form['email']})
        elif tipo == 'medico':
            medicos.append({'id': len(medicos) + 1, 'nome': nome, 'especialidade': request.form['especialidade']})
        flash(f'{tipo.capitalize()} cadastrado com sucesso!', 'success')
    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
