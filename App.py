import math

def restart():
    res = input("Souhaitez-vous faire un nouveau calcul ? o/n")
    if res == "o":
        work()
    elif res == "n":
        print("Très bien, à bientôt")
    else:
        print("Je n'ai pas compris...")
        restart()


def work():
    print("Saisissez une équation sous la forme AX² + BX + C = 0")
    a = float(input("Saisissez A :"))
    b = float(input("Saisissez B :"))
    c = float(input("Saisissez A :"))

    delta = math.pow(b, 2) - (4 * a * c)

    if delta < 0:
        print("l'équation n'a pas de solution")
    elif delta == 0:
        x0 = -b / (2 * a)
        print("L'équation a une seule solution :" + x0)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("L'équation a deux solutions : ")
        print("Première solution : " + x1)
        print("Deuxième solution : " + x2)
    restart()


print("Bienvenue dans ce programme de résolution des équations du second degrés")
work()

