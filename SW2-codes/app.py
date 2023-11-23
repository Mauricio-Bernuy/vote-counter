from flask import Flask
from random import random
from random import randint
import csv
import os
import names


app = Flask(__name__)


@app.route("/")
def hello():
    depas = {}
    with open(
        "ubigeo_peru_2016_departamentos.csv", "r", encoding="utf-8-sig"
    ) as file:
        next(file)
        csvreader = csv.reader(file, delimiter=",")
        for row in csvreader:
            candidatos = randint(4, 10)
            opcionescandidatos = {}
            for j in range(1, candidatos + 1):
                opcionescandidatos[j] = names.get_full_name()
            print(opcionescandidatos)
            depas[row[0]] = {
                "name": row[1],
                "provincias": {},
                "candidatos": opcionescandidatos,
                "numcandidatos": candidatos,
            }
    with open(
        "ubigeo_peru_2016_provincias.csv", "r", encoding="utf-8-sig"
    ) as file:
        next(file)
        csvreader = csv.reader(file, delimiter=",")
        for row in csvreader:
            depas[row[2]]["provincias"][row[0]] = {"name": row[1], "distritos": {}}
    provinciaanterior = ""
    file2 = ""
    with open(
        "ubigeo_peru_2016_distritos.csv", "r", encoding="utf-8-sig"
    ) as file:
        next(file)
        csvreader = csv.reader(file, delimiter=",")
        for row in csvreader:
            directory = row[3] + "/"
            if not os.path.exists(directory):
                os.makedirs(directory)
            if provinciaanterior != row[2]:
                if file2 != "":
                    file2.close()
                file2 = open(
                    directory + row[2] + ".csv", "w", encoding="utf-8-sig", newline=""
                )
                writer = csv.writer(file2)
                header = [
                    "region",
                    "provincia",
                    "ciudad",
                    "dni",
                    "candidato",
                    "esvalido",
                ]
                writer.writerow(header)

            depas[row[3]]["provincias"][row[2]]["distritos"][row[0]] = {"name": row[1]}
            votantes = randint(20, 2000)
            for i in range(1, votantes):
                data = [
                    depas[row[3]]["name"],
                    depas[row[3]]["provincias"][row[2]]["name"],
                    row[1],
                    randint(10000000, 89999999),
                    depas[row[3]]["candidatos"][
                        randint(1, depas[row[3]]["numcandidatos"])
                    ],
                    randint(0, 1),
                ]
                writer.writerow(data)
            provinciaanterior = row[2]
    return "<h1>Hello, World!</h1>"


app.run(host="127.0.0.1", port=8000, debug=True)
