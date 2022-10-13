
import os


def mostraVAs():
    for var in os.environ:
        print("variável: {}\nvalor: {}\n{}".format(var, os.getenv(var), "-"*100))


mostraVAs()

os.environ["nome"] = "posser"

print("--> ", os.environ.get("nome"))
print("--> ", os.environ["nome"])
print("--> ", os.getenv("nome"))