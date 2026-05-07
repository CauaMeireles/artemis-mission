from flask import Flask, render_template

# Criando a aplicação Flask
app = Flask(__name__)

# Rota principal — abre a página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Rodando o servidor localmente
if __name__ == "__main__":
    app.run(debug=True)
    