from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, modelo, precio, capacidad_carga):
        super().__init__(marca, modelo, precio)
        self.capacidad_carga = capacidad_carga
        
    def descripcion(self):
        return f"Camion marca: {self.marca}, modelo: {self.modelo}, capacidad de carga: {self.capacidad_carga}"