# Importación de las clases necesarias desde sus respectivos módulos
from vehiculo import Vehiculo
from camion import Camion
from moto import Moto
from auto import Auto
from concesionaria import Concesionaria

# Se crea una instancia de la clase Concesionaria
venta = Concesionaria()

# Se crean instancias de diferentes tipos de vehículos
mi_auto = Auto("Ford", "Focus", 25000000, 4)               # Auto con 4 puertas
mi_camion = Camion("Dynamo", "7050v", 75000000, "100Ton")  # Camión con capacidad de carga de 100 toneladas
mi_moto = Moto("Honda", "P4v", 3100000, "1150cc")          # Moto con cilindrada de 1150cc

# Se modifica el precio de la moto
mi_moto.set_precio(2900000)

# Se agregan los vehículos a la concesionaria
venta.agregar_vehiculo(mi_auto)
venta.agregar_vehiculo(mi_moto)
venta.agregar_vehiculo(mi_camion)

# Se muestra el resumen de la venta
venta.mostrar_venta()
