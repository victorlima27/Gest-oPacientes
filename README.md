# **Gestão de Pacientes**

Bem-vindo ao sistema de **Gestão de Pacientes**, uma aplicação web desenvolvida em **Python** utilizando o **Flask**. Este projeto foi criado para gerenciar dados de pacientes, médicos, consultas e muito mais. Ele inclui funcionalidades como cadastro, listagem e visualização detalhada de dados.

---

## **Funcionalidades**

- Cadastro e listagem de pacientes.
- Cadastro e listagem de médicos.
- Cadastro, listagem e consulta detalhada de consultas.
- API RESTful com rotas para interações no sistema.

---

## **Pré-requisitos**

Antes de começar, você precisará ter instalado:

- **Python 3.12.4**
- **pip** (gerenciador de pacotes do Python)

---

## **Como configurar o projeto**

### 1. Clone o repositório

```bash
git clone https://github.com/victorlima27/GestaoPacientes.git
cd gestao-pacientes
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

```bash
venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure as credenciais

- Renomeie ou copie cole o arquivo `config_example.py` e `env_example`:

  ```bash
  mv env_example env
  mv config_example.py config.py
  ```
- No arquivo `credemciais.py`, configure as variáveis de ambiente necessárias, como as credenciais do banco de dados. Exemplo:

  ```
  SGBD_cred = 'mariadb+mysqlconnector'
  #SGBD_cred = 'mysql+mysqlconnector'
  usuario_cred = 'root'
  senha_cred = ''
  servidor_cred = 'localhost'
  database_cred = 'bancodedados'

  SECRET_KEY_cred = 'Keys'
  ```
- No arquivo `config.py`, o sistema criará o banco automaticamente com base nas credenciais do `env`.

### 6. Execute as migrações do banco de dados

```bash
flask db upgrade
```

### 7. Insira dados iniciais (opcional)

Popule o banco de dados com dados iniciais:

```bash
flask seed create
```

### 8. Inicie o servidor

```bash
python app.py
```

---

## **Como usar**

1. Acesse o sistema no navegador:
   ```
   http://127.0.0.1:9090
   ```
2. Utilize as rotas da API para interagir com o sistema (exemplo: usando Postman ou cURL).

---

## **Rotas da API**

### Pacientes

- **GET** `/pacientes`: Lista todos os pacientes.
- **POST** `/pacientes`: Cadastra um novo paciente.

### Médicos

- **GET** `/medicos`: Lista todos os médicos.
- **POST** `/medicos`: Cadastra um novo médico.

### Consultas

- **GET** `/consultas`: Lista todas as consultas.
- **POST** `/consultas`: Cadastra uma nova consulta.
- **GET** `/consultas/<id>`: Detalhes de uma consulta pelo ID.

---

## **Exemplo de Configuração de Ambiente**

### Estrutura de Diretórios:

```
gestao-pacientes/
│
├── app.py                # Arquivo principal para rodar o servidor Flask
├── config_example.py     # Exemplo de configuração do projeto
├── requirements.txt      # Dependências do projeto
├── models.py             # Modelos do banco de dados
├── migrations/           # Arquivos de migração do banco
├── seed.py               # Script para popular o banco com dados iniciais
├── static/               # Arquivos estáticos (CSS, JS, imagens)
└── templates/            # Templates HTML do Flask
```

---

## **Contribuindo**

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/nome-da-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m "Adiciona nova funcionalidade"
   ```
4. Envie para a branch principal:
   ```bash
   git push origin feature/nome-da-feature
   ```
5. Abra um Pull Request.

---

## **Licença**

Este projeto está licenciado sob a licença **MIT**. Veja o arquivo `LICENSE` para mais detalhes.

---

Se precisar de ajuda, melhorias ou mais instruções específicas, é só avisar! 🚀
