from flask import Flask
from random import random
from random import randint
import csv
import os
import names
import pandas as pd

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
        # df aqui
        header = [
            "region",
            "provincia",
            "ciudad",
            "dni",
            "candidato",
            "esvalido",
        ]
        dataframe = pd.DataFrame(columns = header)
        for row in csvreader:
            directory = row[3] + "/"
            if not os.path.exists(directory):
                os.makedirs(directory)
            if provinciaanterior != row[2]:
                if file2 != "":
                    print("writing")
                    dataframe.to_excel(directory + row[2] + ".xlsx", index=False)
            #     #     file2.close()
                # file2 = open(
                #     directory + row[2] + ".csv", "w", encoding="utf-8-sig", newline=""
                # )

                # writer = csv.writer(file2)
                # writer.writerow(header)

            depas[row[3]]["provincias"][row[2]]["distritos"][row[0]] = {"name": row[1]}
            votantes = randint(20, 2000)
            for i in range(1, votantes):
                # print(row[3])
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
                rows = pd.DataFrame([data], columns=header)
                dataframe = pd.concat([dataframe, rows], ignore_index=True,axis=0)
                # print(dataframe)
            provinciaanterior = row[2]
            # dataframe.columns = header
            print("comp")
            print("writingfinal")
            dataframe.to_excel(directory + row[2] + ".xlsx", index=False)
    return "<h1>Hello, World!</h1>"


app.run(host="127.0.0.1", port=8000, debug=True)

