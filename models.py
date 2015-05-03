# -*- coding: utf-8 -*-

# - pedidos.
# - devoluciones.
# - distribuidores.
# - supervisores.
# - producto.
# - reclamos.

class Pedido:
    def __init__(self, fecha_publicacion=None, producto=None, cantidad=None):
        self.__fecha_publicacion = fecha_publicacion
        self.__producto = producto
        self.__cantidad = cantidad
    
    def get_fecha_publicacion(self):
        return self.__fecha_publicacion

    def set_fecha_publicacion(self, fecha_publicacion):
        self.__fecha_publicacion = fecha_publicacion

    def get_producto(self):
        return self.__producto

    def set_producto(self, producto):
        self.__producto = producto

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad


    
    

