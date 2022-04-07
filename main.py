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