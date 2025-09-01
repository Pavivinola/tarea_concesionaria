# Importa la clase Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Definición de la clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    # Constructor que extiende el de Vehiculo, añadiendo el atributo cilindrada
    def __init__(self, marca, modelo, precio, cilindrada):
        super().__init__(marca, modelo, precio)     # Llama al constructor de la clase base Vehiculo
        self.cilindrada = cilindrada                # Cilindrada de la moto (ej. 150cc, 600cc)

    # Método que sobrescribe la descripción del vehículo para incluir la cilindrada
    def descripcion(self):
        return f"La moto marca {self.marca} tiene de cilindrada: {self.cilindrada}"
        # Devuelve una cadena con la marca y la cilindrada de la moto
