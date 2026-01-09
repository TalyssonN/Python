from api import app

@app.route('/home')
def homepage():
    return "Pagina Inicial Teste"

@app.route('/blog')
def blog():
    return "Bem vindo ao meu blog!"