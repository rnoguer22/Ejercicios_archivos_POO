import pandas as pd

class Apartado1:
    def __init__(self):
        pass

    def apartado1(self):
        datos = pd.read_csv("calificaciones.csv", header = 0)
        #Lista vacia en la que se almacenaran los futuros diccionarios
        lista = []
        #Creamos una lista con cada columna de los examenes parciales y la asistencia
        lista_parcial_1 = list(datos["Parcial1"])
        lista_parcial_2 = list(datos["Parcial2"])
        lista_asistencia = list(datos["Asistencia"])
        #Bucle para recorrer las celdas de las listas anteriores e ir generando el diccionario buscado
        for i in range(1,17):
            diccionario = {["Parcial 1: " + lista_parcial_1[i], "Parcial 2: " + lista_parcial_2[i]] : lista_asistencia[i]}
            lista.append(diccionario)
        return lista

#Creamos la variable resultado como instancia de clase de Apartado1
resultado = Apartado1()
#Mostramos el diccionario pedido por pantalla
print (resultado.apartado1())