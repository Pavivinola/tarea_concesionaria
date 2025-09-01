# Importa la clase Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Definición de la clase Auto que hereda de Vehiculo
class Auto(Vehiculo):
    # Constructor que extiende el de Vehiculo, añadiendo el atributo puertas
    def __init__(self, marca, modelo, precio, puertas):
        super().__init__(marca, modelo, precio)  # Llama al constructor de la clase base Vehiculo
        self.puertas = puertas                   # Número de puertas del auto

    # Método que sobrescribe la descripción del vehículo para incluir el número de puertas
    def descripcion(self):
        descripcion_padre = super().descripcion()      # Obtiene la descripción básica desde la clase base
        return f"{descripcion_padre} con {self.puertas} puertas"  # Agrega información específica del auto
