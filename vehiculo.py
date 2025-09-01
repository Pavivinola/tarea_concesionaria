class Vehiculo:
    # Método constructor que inicializa los atributos marca, modelo y precio
    def __init__(self, marca, modelo, precio):
        self.marca = marca              # Marca del vehículo (ej. Toyota, Ford)
        self.modelo = modelo            # Modelo del vehículo (ej. Corolla, Mustang)
        self.__precio = precio          # Precio del vehículo (atributo privado)

    # Método getter para obtener el precio del vehículo
    def get_precio(self):
        return self.__precio            # Retorna el valor del atributo privado __precio

    # Método setter para modificar el precio del vehículo
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:            # Verifica que el nuevo precio sea mayor que cero
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que 0")  # Mensaje de error si el precio no es válido

    # Método que retorna una descripción del vehículo
    def descripcion(self):
        return f"Vehículo marca: {self.marca}, modelo: {self.modelo}"  # Devuelve una cadena con marca y modelo
