import os

pastas = ["Pasta1", "Pasta2"]


def func1():
    with open("E:\imed-cc-so-arquivos\Pasta2\\arq6.txt", 'r') as file:
        print("caminho: ", file.name)
        print(file.read())


def func2():
    print("Caminho:", os.getcwd())
    with open(os.path.join(str(os.getcwd()), "Pasta2", "arq6.txt")) as file:
        print("caminho: ", file.name)
        print(file.read())


def func3():
    for pasta in pastas:
        for arquivo in os.listdir(pasta):
            pasta = os.path.join(os.getcwd(), pasta)
            print("pasta: ", pasta)
            print("arquivo", arquivo)
            with open(os.path.join(pasta, arquivo), "r") as file:
                print(file.read())
            print("")
        print("-"*100)


# print(os.listdir()[-2:])

print("1: le arq6 windows\n2: mostra caminho global\n3:mostra os caminhos e le os arquivos")

opcao = int(input("opcao: "))

if opcao == 1:
    func1()
elif opcao == 2:
    func2()
elif opcao == 3:
    func3()