from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, precio, puertas):
        super().__init__(marca, modelo, precio)
        self.puertas = puertas
        
    def descripcion(self):
        parent_desc = super().descripcion()
        return f"{parent_desc} con {self.puertas} puertas"