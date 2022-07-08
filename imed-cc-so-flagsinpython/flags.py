import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--firstname", help="primeiro nome")
parser.add_argument("-l", "--lastname", help="Sobrenome")
parser.add_argument("-a", "--age", type=int, help="idade")

parametros = parser.parse_args()

print("nome: {}\nsobrenome: {}\nidade: {}".format(
    parametros.firstname, parametros.lastname, parametros.age
))
