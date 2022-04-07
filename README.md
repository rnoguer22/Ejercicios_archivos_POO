# Ejercicios_archivos_POO

[Pincha aqui para acceder al link del repositorio](https://github.com/rnoguer22/Ejercicios_archivos_POO.git)

Queda resuelto el ejercicio de archivos de POO de python. No obstante hay un inconveniente, se trata de un error el cual no deberia aparecer, por lo que la resolucion de este ejercicio se ha realizado a ciegas, es decir, sin poder comprobar que el codigo ejecutado es lo que realmente se pide

:(

## Ejercicio

```Python3
import pandas as pd

class Apartado1:
    def __init__(self, file):
        self.file = file

    def apartado1(self):
        datos = pd.read_csv(self.file, header = 0)
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

class Apartado2(Apartado1):
    #Constructor heredado de Apartado1
    def __init__(self, file):
        super().__init__(file)
    
    def apartado2(self):
        datos = pd.read_csv(self.file, header = 0)
        lista = self.apartado1()
        #Creamos la variable nota_final segun los datos que nos proporciona el ejercicio
        nota_final = 0.3*datos["Parcial1"] + 0.3*datos["Parcial2"] + 0.4*datos["OrdinarioPracticas"]
        #Bucle para añadir a la lista que devuelve apartado1 la nota final
        for i in range(1,17):
            nuevo_par = list(nota_final)[i]
            lista[i][0].append(nuevo_par)
        return lista

class Apartado3(Apartado2):
    def __init__(self, file):
        super().__init__(file)

    def apartado3(self):
        lista = self.apartado2()
        #Creamos una lista en la que se almacenaran los apellidos de los suspensos y otra con los aprobados
        lista_suspensos = []
        lista_aprobados = []
        lista_apellidos = list(dato["Apellidos"])
        #Bucle para añadir los alumnos aprobados y suspensos a sus correspondientes listas
        for i in range (1,17):
            if dato["Asistencia"]>=75 and (dato["Parcial1"] and dato["Parcial2"] and dato["Practicas"])>=4 and self.apartado2()[i][2]>=5:
                #El alumno estara aprobado, por lo que añadimos sus apellidos en lista_aprobados
                lista_aprobados.append(lista_apellidos[i])
            else:
                #El alumno estara suspenso, por lo que añadimos sus apellidos en lista_suspensos
                lista_suspensos.append(lista_apellidos[i])
        #La funcion devuelve una lista de listas, la lista de los alumnos aprobados y suspensos
        return lista_aprobados, lista_suspensos
```

## main

```Python3
from Clases.Archivos import *

if __name__ == '__main__':

    #Creamos la variable resultado como instancia de clase de Apartado1
    resultado1 = Apartado1("calificaciones.csv")
    #Mostramos el diccionario pedido por pantalla
    print (resultado1.apartado1())

    resultado2 = Apartado2("calificaciones.csv")
    print (resultado2.apartado2())

    resultado3 = Apartado3("calificaciones.csv")
    print (resultado3.apartado3())
```
