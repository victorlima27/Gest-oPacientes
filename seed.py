from app import app, db, seed_cli

@seed_cli.command('create')
def seed_data():
    from flask_bcrypt import generate_password_hash
    from models import Paciente, Medico, Usuario
    """Popula o banco de dados com dados iniciais."""
    paciente1 = Paciente(nome="João Silva", cpf="12345678901", data_nascimento="1985-10-15", telefone="999999999", historico_medico="Nenhum")
    medico1 = Medico(nome="Dr. Carlos", cpf="11122233344", telefone="777777777", especializacao="Cardiologia")
    usuario1 = Usuario(username="admin", senha=generate_password_hash("admin123").decode('utf-8'), nome_completo="Administrador", perfil="admin")

    db.session.add_all([paciente1, medico1, usuario1])
    db.session.commit()
    print("Seed data inserida com sucesso!")

# Registrar o grupo de comandos no Flask CLI
app.cli.add_command(seed_cli)