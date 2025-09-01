# Importa la clase Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Definición de la clase Camion que hereda de Vehiculo
class Camion(Vehiculo):
    # Constructor que extiende el de Vehiculo, añadiendo el atributo capacidad de carga
    def __init__(self, marca, modelo, precio, capacidad_carga):
        super().__init__(marca, modelo, precio)       # Llama al constructor de la clase base Vehiculo
        self.capacidad_carga = capacidad_carga        # Capacidad de carga del camión (en kg, toneladas, etc.)

    # Método que sobrescribe la descripción del vehículo para incluir la capacidad de carga
    def descripcion(self):
        return f"Camion marca: {self.marca}, modelo: {self.modelo}, capacidad de carga: {self.capacidad_carga}"
        # Devuelve una cadena con la marca, modelo y capacidad de carga del camión
