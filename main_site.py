from flask import Flask, render_template

app = Flask(__name__)

# route -> link EX: meudominio.com/ # função -> O que voce vai mostrar na sua pagina
# template

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/endereco')
def endereco():
    return render_template("endereco.html")

@app.route('/usuario/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku
