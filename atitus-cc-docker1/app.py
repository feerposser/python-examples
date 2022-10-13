from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Olá, mundo! Você tem acesso aos meus links <a href='https://linktr.ee/imedposser' target='_BLANK'>clicando aqui.</a>"

@app.route("/gdg")
def gdg():
    return "Você pode conhecer o GDG <a href='https://instagram.com/gdg.pf' target='_BLANK'>clicando aqui</a>"

@app.route("/<nome>")
def nome(nome):
    return "{}, não esqueça da votação da chapa do DASIC".format(nome)


if __name__ == "__main__":
    app.run(host="0.0.0.0")