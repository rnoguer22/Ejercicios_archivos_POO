import pandas as pd

def apartado1():
    datos = pd.read_csv("calificaciones.csv", header = 0)
    lista = []
    lista_parcial_1 = list(datos["Parcial1"])
    lista_parcial_2 = list(datos["Parcial2"])
    lista_asistencia = list(datos["Asistencia"])
    for i in range(1,17):
        diccionario = {["Parcial 1: " + lista_parcial_1[i], "Parcial 2: " + lista_parcial_2[i]] : lista_asistencia[i]}
        lista.append(diccionario)
    return lista

apartado1()