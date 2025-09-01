# Importa la clase Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Definición de la clase Concesionaria
class Concesionaria:
    # Constructor que inicializa la lista de pedidos (vehículos agregados)
    def __init__(self):
        self.pedidos = []  # Lista que almacenará los vehículos agregados a la venta

    # Método para agregar un vehículo a la concesionaria
    def agregar_vehiculo(self, vehiculo):
        # Muestra en consola la descripción y el precio del vehículo agregado
        print(f"Agregado: {vehiculo.descripcion()} - Precio: ${vehiculo.get_precio()}")
        self.pedidos.append(vehiculo)  # Agrega el vehículo a la lista de pedidos

    # Método para mostrar el resumen de la venta
    def mostrar_venta(self):
        print("--- Recumen de la Venta ---")  # Encabezado del resumen
        total = 0  # Variable para acumular el total a pagar
        for vehiculo in self.pedidos:
            # Muestra la descripción y el precio de cada vehículo
            print(f"{vehiculo.descripcion()} \n ${vehiculo.get_precio()}")
            total += vehiculo.get_precio()  # Suma el precio al total
        print(f"Total a pagar: ${total}")  # Muestra el total acumulado
