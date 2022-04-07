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
        lista_suspensos = []
        lista_aprobados = []
        lista_apellidos = list(dato["Apellidos"])
        for i in range (1,17):
            if dato["Asistencia"]>=75 and (dato["Parcial1"] and dato["Parcial2"] and dato["Practicas"])>=4 and self.apartado2()[i][2]>=5:
                lista_aprobados.append(lista_apellidos[i])
            else:
                lista_suspensos.append(lista_apellidos[i])
        return lista_aprobados, lista_suspensos


#Creamos la variable resultado como instancia de clase de Apartado1
resultado1 = Apartado1("calificaciones.csv")
#Mostramos el diccionario pedido por pantalla
print (resultado1.apartado1())

resultado2 = Apartado2("calificaciones.csv")
print (resultado2.apartado2())

