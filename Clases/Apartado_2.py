import pandas as pd
from Clases.Apartado_1 import Apartado1

class Apartado2(Apartado1):
    #Constructor heredado de Apartado1
    def __init__(self, file):
        super().__init__(file)
    
    def apartado2(self):
        datos = pd.read_csv(self.file, header = 0)
        lista = self.apartado1()
        nota_final = 0.3*datos["Parcial1"] + 0.3*datos["Parcial2"] + 0.4*datos["OrdinarioPracticas"]
        for i in range(1,17):
            nuevo_par = list(nota_final)[i]
            lista[i][0].append(nuevo_par)
        return lista