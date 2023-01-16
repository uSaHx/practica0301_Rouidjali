import csv
import cProfile

nif_dict = {"0":"T", "1":"R", "2":"W", "3":"A", "4":"G", "5":"M", "6":"Y", "7":"F", "8":"P", "9":"D", "10":"X",
            "11":"B", "12":"N", "13":"J", "14":"Z", "15":"S", "16":"Q", "17":"V", "18":"H", "19":"L", "20":"C",
            "21":"K", "22":"E"}
def check_DGT(ruta):
    with open(ruta, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", dialect=csv.excel)
        lista = []
        lista_corregida = []
        for persona in reader:
            lista.append(persona)
        for x in lista:
            f = []
            nombre = check_username(x[0])
            dni = check_nif(x[1])
            f.append(nombre)
            f.append(dni)
            lista_corregida.append(f)
    with open(ruta, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=" ")
        for x in lista_corregida:
            writer.writerow(x)
    return
def check_username(name):
    return name.title()
def check_nif(nif):
    return str(nif[0:8] + nif_dict[str(int(nif[0:8]) % 23)])

cProfile.run("check_DGT('C:\datos\Documents\GIT_Oussama\practica0301_Rouidjali/1000 - copia.csv')")