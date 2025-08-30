from vehiculo import Vehiculo 
from camion import Camion 
from moto import Moto 
from auto import Auto
from concesionaria import Concesionaria

venta = Concesionaria()

mi_auto = Auto("Ford", "Focus", 25000000, 4)
mi_camion = Camion("Dynamo", "7050v", 75000000, "100Ton")
mi_moto = Moto("Honda", "P4v", 3100000, "1150cc")

# Correct way to change the price
mi_moto.set_precio(2900000)

venta.agregar_vehiculo(mi_auto)
venta.agregar_vehiculo(mi_moto)
venta.agregar_vehiculo(mi_camion)

venta.mostrar_venta()