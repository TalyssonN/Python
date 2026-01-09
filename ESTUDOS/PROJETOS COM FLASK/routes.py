# from flask import Blueprint, render_template, request, redirect, url_for
from flask import Blueprint, render_template
# from main import db, Usuario

routes = Blueprint('routes', __name__)

@routes.route('/home')
def homepage():
    return render_template('site.html')

# @routes.route('/cadastrar', methods=['POST'])
# def cadastrar_usuario():
#     nome = request.form.get('nome')
#     email = request.form.get('email')

#     # Evita erro de email duplicado
#     usuario_existente = Usuario.query.filter_by(email=email).first()
#     if usuario_existente:
#         return "Email já cadastrado", 400

#     novo_usuario = Usuario(
#         nome=nome,
#         email=email
#     )

#     db.session.add(novo_usuario)
#     db.session.commit()

#     return redirect(url_for('routes.homepage'))
