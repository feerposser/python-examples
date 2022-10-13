from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Olá, mundo! Participe do Google Developer Groups Passo Fundo -> <a href='https://www.instagram.com/gdg.pf/' target='_BLANK'>clicando aqui.</a>"

@app.route("/teste")
def teste():
    return "Você também pode participar direto <a href='https://www.youtube.com/watch?v=oT-4we1FMPI' target='_BLANK'>clicando aqui</a>"

@app.route("/<nome>")
def nome(nome):
    return "{}, não esqueça que dia 23 e 30 do 10 tem GDG Passo Fundo!".format(nome)


if __name__ == "__main__":
    app.run(host="0.0.0.0")