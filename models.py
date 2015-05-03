# -*- coding: utf-8 -*-

# - pedidos.
# - devoluciones.
# - distribuidores.
# - supervisores.
# - producto.
# - reclamos.

class Distribuidor:
    def __init__(self, cod, ruc, nombre, direccion, supervisor):
        self.__cod = cod
        self.__ruc = ruc
        self.__nombre = nombre
        self.__direccion = direccion
        self.__supervisor = supervisor

    def get_cod(self):
        return self.__cod

    def set_cod(self, cod):
        self.__cod = cod

    def get_ruc(self):
        return self.__ruc

    def set_ruc(self, ruc):
        self.__ruc = ruc

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_supervisor(self):
        return self.__supervisor

    def set_supervisor(self, supervisor):
        self.__supervisor = supervisor


class Pedido:
    def __init__(self, cod=None, fecha_publicacion=None, producto=None, cantidad=None):
        self.__cod = cod
        self.__fecha_publicacion = fecha_publicacion
        self.__producto = producto
        self.__cantidad = cantidad

    def get_cod(self):
        return self.__cod

    def set_cod(self, cod):
        self.__cod = cod

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

