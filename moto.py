from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio, cilindrada):
        super().__init__(marca, modelo, precio)
        self.cilindrada = cilindrada
        
    def descripcion(self):
        return f"La moto marca {self.marca} tiene de cilindrada: {self.cilindrada}"