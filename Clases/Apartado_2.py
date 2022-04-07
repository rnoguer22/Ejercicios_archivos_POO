import pandas as pd
from Clases.Apartado_1 import Apartado1

class Apartado2(Apartado1):
    #Constructor heredado de Apartado1
    def __init__(self, file):
        super().__init__(file)
    
