
#  PyAtt

## Sobre o Projeto

**PyAtt** é uma aplicação web desenvolvida com Python e Flask que permite o cadastro de usuários, gerenciamento de tarefas e exibição de perfil pessoal. O projeto possui integração com banco de dados SQLite e oferece uma interface simples baseada em HTML.

---

## Funcionalidades

- Cadastro de novos usuários
- Criação de tarefas
- Visualização de tarefas e perfil do usuário
- Upload de imagens para o perfil (imagem padrão incluída)

---

## Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLite
- HTML/CSS
- Jinja2 (templates)
- Werkzeug (segurança de senha)

---

## Estrutura de Pastas

```
PyAtt/
│
├── main.py                  # Arquivo principal para iniciar a aplicação
├── criar_banco.py          # Script para criação do banco de dados
├── chave.py                # Chave secreta para o Flask
├── requirements.txt        # Dependências do projeto
├── instance/comunidade.db  # Banco de dados SQLite
│
├── projetosenac/
│   ├── __init__.py         # Configuração da aplicação Flask
│   ├── forms.py            # Formulários WTForms
│   ├── models.py           # Modelos do banco de dados
│   ├── routes.py           # Rotas da aplicação
│   ├── static/
│   │   └── defalt.png      # Imagem padrão de perfil
│   └── templates/          # Templates HTML
│       ├── homepage.html
│       ├── criarconta.html
│       ├── cadastrar_tarefa.html
│       └── perfil.html
```

---

## Como Rodar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/pyatt.git
cd pyatt
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Crie o banco de dados
```bash
python criar_banco.py
```

### 5. Execute a aplicação
```bash
python main.py
```

Acesse o app via: [http://localhost:5000](http://localhost:5000)

---

## Autor

Desenvolvido por **Robson Calheira**.
