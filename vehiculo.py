class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio
        
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que 0")
            
    def descripcion(self):
        return f"Vehículo marca: {self.marca}, modelo: {self.modelo}"