from flask import render_template, url_for, redirect
from projetosenac import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from projetosenac.models import Usuario, Foto, Tarefa
from projetosenac.forms import FormLogin, FormCriarConta, FormTarefa

# Página de login
@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('homepage.html', form=formlogin, usuario=current_user)

# Página de perfil (exibe as tarefas do usuário também)
@app.route("/perfil/<id_usuario>")
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        tarefas = Tarefa.query.filter_by(usuario_id=current_user.id).order_by(Tarefa.data_criacao.desc()).all()
        return render_template('perfil.html', usuario=current_user, tarefas=tarefas)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('perfil.html', usuario=usuario, tarefas=[])

# Página de cadastro de conta (login automático)
@app.route("/criar-conta", methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(
            username=formcriarconta.username.data,
            email=formcriarconta.email.data,
            senha=senha
        )

        database.session.add(usuario)
        database.session.commit()

        #Login automático após cadastro
        login_user(usuario, remember=True)

        return redirect(url_for('perfil', id_usuario=usuario.id))

    return render_template('criarconta.html', form=formcriarconta, usuario=current_user)

# Logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

# Cadastro de tarefas
@app.route("/cadastrar-tarefa", methods=["GET", "POST"])
@login_required
def cadastrar_tarefa():
    form = FormTarefa()
    if form.validate_on_submit():
        nova_tarefa = Tarefa(
            titulo=form.titulo.data,
            categoria=form.categoria.data,
            usuario_id=current_user.id
        )
        database.session.add(nova_tarefa)
        database.session.commit()
        return redirect(url_for("perfil", id_usuario=current_user.id))
    return render_template("cadastrar_tarefa.html", form=form)
