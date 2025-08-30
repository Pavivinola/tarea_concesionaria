from vehiculo import Vehiculo

class Concesionaria:
    def __init__(self):
        self.pedidos = []
        
    def agregar_vehiculo(self, vehiculo):
        print(f"Agregado: {vehiculo.descripcion()} - Precio: ${vehiculo.get_precio()}")
        self.pedidos.append(vehiculo)
        
    def mostrar_venta(self):
        print("--- Recumen de la Venta ---")
        total = 0
        
        for vehiculo in self.pedidos:
            print(f"{vehiculo.descripcion()} | ${vehiculo.get_precio()}")
            total += vehiculo.get_precio()
            
        print(f"Total a pagar: ${total}")